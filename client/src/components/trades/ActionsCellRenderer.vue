<template>
  <div class="flex flex-row">
    <app-dropdown :options="actions" @option-clicked="optionClicked">
      <template #trigger="{ open }">
        <a href="#" @click="open">Actions</a>
      </template>
    </app-dropdown>
  </div>
</template>

<script lang="ts">
  import DropdownItem from "@/types/components/app-dropdown-item";
  import Trade from "@/data/models/trade";
  import { defineComponent, ref, PropType } from "vue";
  import AppButton from "@/components/AppButton.vue";
  import AppDropdown from "@/components/AppDropdown.vue";
  import { ICellRendererParams } from "@ag-grid-community/all-modules";

  interface RendererParams extends ICellRendererParams {
    click(action: DropdownItem, trade: Trade): void;
  }

  export default defineComponent({
    components: {
      AppButton,
      AppDropdown,
    },
    props: {
      params: {
        type: Object as PropType<RendererParams>,
        required: false,
      },
    },
    setup() {
      const actions = ref<Array<Array<DropdownItem>>>([]);
      return {
        actions,
      };
    },
    mounted() {
      const orderStatus = this.params!.data.orderStatus;
      if (orderStatus === "complete") {
        // The order has been filled so we can trim it down
        this.actions.push([
          { label: "Trim 1/3", action: "TRIM_THIRD" },
          { label: "Trim 1/2", action: "TRIM_HALF" },
          { label: "Close", action: "CLOSE" },
        ]);
      } else {
        this.actions.push([{ label: "Cancel order", action: "CANCEL" }]);
      }

      this.actions.push([
        {
          label: "Delete",
          action: "DELETE",
          confirm:
            "Are you sure you want to delete this trade? Deleting an open trade will keep the position open.",
        },
      ]);
    },
    methods: {
      optionClicked(option: DropdownItem) {
        if (option.confirm) {
          let confirmed = confirm(option.confirm);
          if (!confirmed) return;
        }

        this.params!.click(option.action, this.params!.data);
      },
    },
  });
</script>
