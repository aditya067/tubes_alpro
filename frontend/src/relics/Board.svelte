<script lang="ts">
  import { onMount } from 'svelte';

  interface Card {
    id: number;
    text: string;
    enabled: boolean;
  }

  export let title: string;
  export let className: string;
  export let notes: any;

  let cardState: Card[] = [];

  onMount(() => {
  });

  function toggleCardState(idx: number) {
    cardState[idx].enabled = !cardState[idx].enabled;
  }
</script>

<div class="model-item {className}">
  <div class="item-heading">
    <i class="icon icon-{className}" />
    <span>{title}</span>
  </div>
  <div class="cards">
    {#each notes as { id, text }, idx}
      <div id="{className}-{id}" class="note note-{className}">{text}</div>
    {/each}
  </div>
</div>
