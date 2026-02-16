<style lang="scss" scoped>
// .btn {
// }</style>

<template>
    <button class="btn" :class="computedClasses" v-bind="computedAttrs"></button>
</template>

<script lang="ts">
import type { PropType } from "vue";
import type { Booleanish } from "@/types/MBase";
import type { MButtonType, MButtonVariant } from "./MButtonType";

export default {
    components: {},
    props: {
        active: {
            type: [Boolean, String] as PropType<Booleanish>,
            default: false,
        },
        type: { type: String as PropType<MButtonType>, default: "button" },
        variant: { type: String as PropType<MButtonVariant>, default: "secondary" },
    },
    computed: {
        computedClasses() {
            return [[`btn-${this.$props.variant}`]];
        },
        computedAttrs() {
            return {};
        },
    },
};
</script>
