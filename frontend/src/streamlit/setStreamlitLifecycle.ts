import { onMount, afterUpdate } from "svelte";
import { Streamlit } from "./streamlit";

export const setStreamlitLifecycle = (): void => {
  onMount((): void => {
    Streamlit.setFrameHeight();
  });

  afterUpdate((): void => {
    Streamlit.setFrameHeight();
  });
};
