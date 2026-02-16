<script setup lang="ts">
import { reactive } from 'vue';

// const props = defineProps({

// })

const emit = defineEmits(['submit']);

const state = reactive({
    validate: false
})

function onSubmit() {
    state.validate = true;
    emit('submit');
}


</script>

<template>
    <form class="form" @submit.prevent="onSubmit" v-bind="$attrs">
        <slot :validate="state.validate"></slot>
    </form>
</template>