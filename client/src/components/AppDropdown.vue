<template>
  <slot name="trigger" v-if="!isOpen" :open="openDropdown" />
  <div
    v-else
    class="
      origin-top-right
      absolute
      right-0
      mt-2
      w-56
      rounded-md
      shadow-lg
      bg-white
      ring-1 ring-black ring-opacity-5
      divide-y divide-gray-100
      focus:outline-none
    "
    role="menu"
    aria-orientation="vertical"
    aria-labelledby="menu-button"
    tabindex="-1"
    v-click-away="closeDropdown"
  >
    <div
      v-for="(group, index) in options"
      :key="index"
      class="py-1"
      role="none"
    >
      <a
        v-for="(option, optIndex) in group"
        :key="optIndex"
        href="#"
        class="text-gray-700 block px-4 py-2 text-sm"
        role="menuitem"
        tabindex="-1"
        @click.prevent="$emit('option-clicked', option)"
        >{{ option.label }}</a
      >
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent, ref, PropType } from "vue";
  import { directive } from "vue3-click-away";
  import DropdownItem from "@/types/components/app-dropdown-item";

  export default defineComponent({
    name: "Dropdown",
    directives: {
      clickAway: directive,
    },
    props: {
      options: {
        type: Array as PropType<Array<Array<DropdownItem>>>,
        required: true,
      },
    },
    emits: ["option-clicked"],
    setup() {
      let isOpen = ref(false);
      let openDropdown = () => (isOpen.value = true);
      let closeDropdown = () => (isOpen.value = false);

      return {
        isOpen,

        closeDropdown,
        openDropdown,
      };
    },
  });
</script>
