<template>
  <div class="config flex justify-center">
    <app-panel class="w-1/2 p-8">
      <app-header>Welcome to KTrade</app-header>

      <p class="mb-8">
        Lets get setup. Fill in the details below and we can get started
      </p>

      <config-form></config-form>
    </app-panel>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import ConfigForm from "@/views/ConfigForm.vue";
  import AppHeader from "@/components/AppHeader.vue";
  import AppPanel from "@/components/AppPanel.vue";

  export default defineComponent({
    components: {
      ConfigForm,
      AppHeader,
      AppPanel,
    },
  });
</script>
