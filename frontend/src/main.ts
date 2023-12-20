import { WithStreamlitConnection } from "./streamlit";
import BMCComponent from "./BMCComponent.svelte";

const bmcComponent = new WithStreamlitConnection({
  target: document.body,
  props: {
    
    component: BMCComponent,
    spreadArgs: true,
  },
});

export default bmcComponent;
