<script setup lang="ts">
import { computed, useTemplateRef } from 'vue';

const props = defineProps({
    maxHeight: {
        type: Number,
        default: 100,
    },
    modelValue: {
        type: String,
        default: ""
    }
});

const emit = defineEmits(['update:modelValue']);

const textareaRef = useTemplateRef("textarea");

const textarea = computed(() => textareaRef.value as HTMLTextAreaElement),
 value = computed({
    get() {
        return props.modelValue;
    },
    set(value) {
        emit('update:modelValue', value);
    }
});

function resizeTextarea() {
    // console.log(textareaRef.scrollHeight);
    textarea.value.style.height = "auto"; // Reset the height
    if (textarea.value.scrollHeight > props.maxHeight)
        textarea.value.style.height = `${props.maxHeight}px`;
    else textarea.value.style.height = `${textarea.value.scrollHeight}px`; // Set the height to match the content
}
</script>

<template>
    <textarea ref="textarea" rows="3" v-model="value" @input="resizeTextarea" style="resize: none"></textarea>
</template>
