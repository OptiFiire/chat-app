<script setup>
import { cn } from '@/misc/utils';
import { useVModel } from '@vueuse/core';

const props = defineProps({
  class: { type: null, required: false },
  defaultValue: { type: [String, Number], required: false },
  modelValue: { type: [String, Number], required: false },
});

const emits = defineEmits(['update:modelValue']);

const modelValue = useVModel(props, 'modelValue', emits, {
  passive: true,
  defaultValue: props.defaultValue,
});
</script>

<template>
  <textarea
    v-model="modelValue"
    id="textarea"
    :class="
      cn(
        'flex min-h-max w-full rounded-2xl border border-input bg-transparent px-3 text-sm shadow-sm py-2 placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50',
        props.class,
      )
    "
  />
</template>
