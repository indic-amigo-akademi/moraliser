<style lang="scss" scoped>
.btn {
}
</style>

<template lang="html">
    <button class="btn" :class="computedClasses" v-bind="computedAttrs"></button>
</template>

<script lang="ts">
import { PropType } from "vue";
import { Booleanish } from "@/types/MBase";
import { MButtonType, MButtonVariant } from "@/types/MButton";

export default {
    components: {},
    props: {
        active: {
            type: [Boolean, String] as PropType<Booleanish>,
            default: false
        },
        type: { type: String as PropType<MButtonType>, default: "button" },
        variant: { type: String as PropType<MButtonVariant>, default: "secondary" }
    },
    computed: {
        computedClasses() {
            return [[`btn-${this.$props.variant}`]];
        },
        computedAttrs() {
            return {};
        }
    }
};
</script>
