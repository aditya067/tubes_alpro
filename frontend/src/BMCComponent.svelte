<script lang="ts">
  import { Streamlit, setStreamlitLifecycle } from './streamlit';
  import Board from './relics/Board.svelte';

  setStreamlitLifecycle();

  interface Card {
    id: number;
    text: string;
    enabled: boolean;
  }

  interface BmcType {
    visual: any;
    key_partners: { cards: Card[] };
    key_activities: { cards: Card[] };
    key_resources: { cards: Card[] };
    value_propositions: { cards: Card[] };
    customer_relationship: { cards: Card[] };
    channels: { cards: Card[] };
    customer_segments: { cards: Card[] };
    cost_structure: { cards: Card[] };
    revenue_streams: { cards: Card[] };
  }

  export let data: BmcType;
</script>

<!-- Main -->
<div class="container-fluid text-center">
  <h1 class="bmc-title">{data.visual.company_name} <br> <span>● Business Model Canvas ●</span></h1>
</div>
<div class="container-fluid grids">
  <div class="grid grid-top">
    <Board title="Key Partners" className="partner" notes={data.key_partners.cards} />
    <Board title="Key Activities" className="activities" notes={data.key_activities.cards} />
    <Board title="Key Resources" className="resources" notes={data.key_resources.cards} />
    <Board title="Value Propositions" className="value-p" notes={data.value_propositions.cards} />
    <Board title="Customer Relationship" className="customer-r" notes={data.customer_relationship.cards} />
    <Board title="Key Channels" className="channels" notes={data.channels.cards} />
    <Board title="Customer Segments" className="customer-s" notes={data.customer_segments.cards} />
  </div>
  <div class="grid grid-bottom grid-vertical">
    <Board title="Cost Structure" className="cost" notes={data.cost_structure.cards} />
    <Board title="Revenue Streams" className="revenue" notes={data.revenue_streams.cards} />
  </div>
</div>
<div class="pr text-right">Kelompok 9</div>
