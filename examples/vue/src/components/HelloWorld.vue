<script setup lang="ts">
import { nextTick, onMounted, ref, watch } from "vue";
import { SwitchKeys,  ISwitchKeysEnvironmentFeaturesResponse, SwitchKeysEnvironmentServices} from "@switchkeys/ts-client";

// State variables
const design = ref<ISwitchKeysEnvironmentFeaturesResponse>();
const chat = ref<ISwitchKeysEnvironmentFeaturesResponse>();
const loading = ref<boolean>(false);
const v1Enabled = ref<boolean>(false);
const chatEnabled = ref<boolean>(false);
const switchKeys = new SwitchKeys();
const environment = ref<SwitchKeysEnvironmentServices>();

// Function to load or initialize the design feature
const loadDesignFeature = async () => {
  if (environment.value?.hasFeature("design")) {
    design.value = environment.value.getFeature("design");
  } else {
    design.value = await environment.value?.addFeature({
      name: "design",
      value: "v1.2",
    });
  }
  v1Enabled.value = design.value?.value !== "v1.2";
};

// Function to load or initialize the chat feature
const loadChatFeature = async () => {
  if (environment.value?.hasFeature("chat")) {
    chat.value = environment.value.getFeature("chat");
  } else {
    chat.value = await environment.value?.addFeature({
      name: "chat",
      value: "false",
    });
  }
  chatEnabled.value = chat.value?.value === "true";
};

// Function to update the chat component's position
const updateChatComponentPlace = () => {
  const el = document.getElementById("chat");
  if (el) {
    el.style.bottom = chat.value?.value === "true" ? "30px" : "-500px";
  }
};

// On component mount, login and load the features
onMounted(async () => {
  loading.value = true;
  try {
    await switchKeys.auth.login({
      email: "admin@gmail.com",
      password: "0000",
    });

    environment.value = await switchKeys.environments.load(
      "a525176d-3344-4ce0-abd9-7e6b04eff0b8"
    );
    await loadDesignFeature();
    await loadChatFeature();
  } catch (error) {
    console.error("Error loading features:", error);
  } finally {
    loading.value = false;
    nextTick(() => {
      updateChatComponentPlace();
    });
  }
});

// Watchers to update the features when the switches are toggled
watch(
  v1Enabled,
  async (newVal) => {
    if (design.value) {
      design.value = await environment.value?.updateFeature({
        name: "design",
        newName: "design",
        newValue: newVal ? "v1.1" : "v1.2",
      });
    }
  },
  { deep: true }
);

watch(
  chatEnabled,
  async (newVal) => {
    chat.value = await environment.value?.updateFeature({
      name: "chat",
      newName: "chat",
      newValue: String(newVal),
    });
    updateChatComponentPlace();
  },
  { deep: true }
);
</script>

<template>
  <section v-if="loading">
    <v-row class="h-screen w-100">
      <v-col cols="12" class="d-flex justify-center align-end">
        <v-progress-circular color="primary" indeterminate :size="50" />
      </v-col>
      <v-col cols="12" class="d-flex justify-center align-start">
        Loading default design...
      </v-col>
    </v-row>
  </section>
  <section v-else>
    <v-container>
      <v-app-bar :elevation="2">
        <template v-slot:prepend>
          <v-app-bar-nav-icon />
        </template>
        <v-app-bar-title>VueJs Example</v-app-bar-title>
        <v-spacer />
        <v-chip color="primary" class="mr-15">
          Version: <strong>{{ design?.value }}</strong>
        </v-chip>
      </v-app-bar>

      <!-- Design Version v1.2 -->
      <template v-if="design?.value === 'v1.2'">
        <v-carousel show-arrows="hover">
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            cover
          />
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg"
            cover
          />
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            cover
          />
        </v-carousel>
        <div class="pa-5">
          <v-row>
            <v-col cols="4" v-for="card in [1, 2, 3]" :key="card">
              <v-toolbar height="35" color="#cd9542" variant="tonal" />
              <v-card class="pa-5">
                <v-card-title class="d-flex justify-center">
                  <v-chip color="primary"> Card {{ card }} </v-chip>
                </v-card-title>
              </v-card>
            </v-col>
          </v-row>
        </div>
      </template>

      <!-- Design Version v1.1 -->
      <template v-else>
        <v-carousel hide-delimiters>
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg"
            cover
          />
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
            cover
          />
          <v-carousel-item
            src="https://cdn.vuetifyjs.com/images/carousel/bird.jpg"
            cover
          />
        </v-carousel>
        <div class="pa-5">
          <v-row>
            <v-col cols="4" v-for="card in [1, 2, 3]" :key="card">
              <v-toolbar height="35" color="#ab4949" variant="tonal" />
              <v-card class="pa-5" :title="'Card' + card" />
            </v-col>
          </v-row>
        </div>
      </template>

      <!-- Switches for toggling design version and chat feature -->
      <div class="w-100 d-flex justify-center">
        <v-card
          variant="tonal"
          color="white"
          class="w-25"
          title="SwitchKeys Switches"
          prepend-icon="mdi-nintendo-switch"
        >
          <v-card-text>
            <div class="pa-4">
              <v-alert class="mb-2">
                <v-row>
                  <v-col cols="8" class="d-flex justify-start align-center">
                    <strong>Change Design Version</strong>
                  </v-col>
                  <v-col cols="4" class="d-flex justify-end align-center">
                    <v-tooltip
                      location="bottom center"
                      text="Want to change the design?"
                    >
                      <template #activator="{ props }">
                        <v-switch
                          inset
                          hide-details
                          v-model="v1Enabled"
                          v-bind="props"
                        />
                      </template>
                    </v-tooltip>
                  </v-col>
                </v-row>
              </v-alert>

              <v-alert class="mb-2">
                <v-row>
                  <v-col cols="8" class="d-flex justify-start align-center">
                    <strong>Display Chat Component</strong>
                  </v-col>
                  <v-col cols="4" class="d-flex justify-end align-center">
                    <v-tooltip
                      location="bottom center"
                      text="Toggle chat component"
                    >
                      <template #activator="{ props }">
                        <v-switch
                          inset
                          hide-details
                          v-model="chatEnabled"
                          v-bind="props"
                        />
                      </template>
                    </v-tooltip>
                  </v-col>
                </v-row>
              </v-alert>

              <v-alert class="mb-2" variant="tonal" color="warning">
                <div class="d-flex justify-center">
                  <v-chip color="primary" class="ml-2 mr-2">
                    Design version {{ design?.value }}
                  </v-chip>
                  <v-chip color="success" class="ml-2 mr-2">
                    Chat {{ chat?.value === "true" ? "ON" : "OFF" }}
                  </v-chip>
                </div>
              </v-alert>
            </div>
          </v-card-text>
        </v-card>
      </div>

      <!-- Chat icon -->
      <div class="d-flex justify-end align-end">
        <div class="chat" id="chat">
          <v-icon size="35" icon="mdi-chat" />
        </div>
      </div>
    </v-container>
  </section>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
.chat {
  position: fixed;
  bottom: 30px;
  width: 65px;
  height: 65px;
  background: #7a5927;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  content: "";
  margin-top: 25px;
  cursor: pointer;
  transition: 0.5s;
  font-weight: 700;
}

.chat:hover {
  scale: 1.05;
}
</style>
