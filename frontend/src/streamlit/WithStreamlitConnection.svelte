<script lang="ts">
  import { onMount, afterUpdate, onDestroy } from "svelte";
  import { Streamlit } from "./streamlit";
  import type { RenderData } from "./streamlit";

  /**
   * Custom Streamlit component
   */
  export let component: any;
  export let spreadArgs: boolean = true;

  // State
  let renderData: RenderData;
  let args: any;

  /** The component's width. */
  let width: number;
  let disabled: boolean;

  const onRenderEvent = (event: Event): void => {
    // Update our state with the newest render data
    renderData = (event as CustomEvent<RenderData>).detail;
    args = renderData.args;
    disabled = renderData.disabled;
  };

  onMount((): void => {
    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent);
    Streamlit.setComponentReady();
  });

  onDestroy((): void => {
    // Remove our `onRender` handler to Streamlit's render event.
    Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent);
  });
</script>

<svelte:window bind:innerWidth={width} />
<!-- Don't render until we've gotten our first RENDER_EVENT from Streamlit. -->
{#if renderData}
  {#if spreadArgs}
    <svelte:component this={component} {...args} {disabled} {width} />
  {:else}
    <svelte:component this={component} {args} {disabled} {width} />
  {/if}
{/if}
