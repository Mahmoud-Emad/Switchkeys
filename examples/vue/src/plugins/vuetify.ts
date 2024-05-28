import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css";

import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";


const vuetify = createVuetify({
  defaults: {
  },
  components: {
    ...components,
  },
  directives,
  theme: {
  },
});

export default vuetify;
