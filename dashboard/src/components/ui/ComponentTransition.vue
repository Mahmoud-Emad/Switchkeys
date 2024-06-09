<template>
  <div class="load-component" id="component">
    <slot name="component"/>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";

export default defineComponent({
  nbame: "ComponentTransition",
  setup(){
    onMounted(() => {
      const component = document.getElementById("component")
      if(component){
        setTimeout(() => {
          component.style.bottom = `0`
        }, 10)
      } 
    })
  }
})
</script>

<style>
.load-component{
  overflow: hidden;
  position: relative;
  bottom: -100%;
  transition: 0.3s;
}
</style>