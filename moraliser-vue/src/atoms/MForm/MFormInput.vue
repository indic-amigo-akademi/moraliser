<style lang="scss"></style>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, type PropType } from 'vue';
import { validator, type MFormInputRulesType, type MFormInputType } from '@/atoms/MForm/MFormInputType'
import MAutosizeTextarea from "@/atoms/MAutosizeTextarea/MAutosizeTextarea.vue";


const props = defineProps({
    name: {
        type: String,
        required: true
    },
    title: {
        type: String,
        default: ""
    },
    inputType: {
        type: String as PropType<MFormInputType>,
        default: "text"
    },
    label: {
        type: [String, Boolean],
        default: false
    },
    placeholder: {
        type: String,
        default: "Enter your Name"
    },
    prependIcon: {
        type: [String, Boolean]
    },
    appendIcon: {
        type: [String, Boolean]
    },
    modelValue: {
        type: String,
        required: true
    },
    errorValue: {
        type: String,
        default: ""
    },
    rules: {
        type: Array as PropType<string[]>,
        default: []
    },
    rule: {
        type: String,
        default: ""
    },
    containerClassname: {
        type: String,
        default: ""
    }
});

const state = reactive({
    inputType: props.inputType,
});

const emit = defineEmits(['update:modelValue', 'update:errorValue'])

const value = computed({
    get() {
        return props.modelValue;
    },
    set(value) {
        emit('update:modelValue', value);
    }
}), errorVal = computed({
    get() {
        return props.errorValue;
    },
    set(value) {
        emit('update:errorValue', value);
    }
}), isMandatory = computed(() => props.rules.includes('required'));

function togglePassword() {
    state.inputType = state.inputType === 'password' ? 'text' : 'password';
}

function validate() {
    const rulesArr = props.rules.length > 0 ? props.rules : props.rule.split(',').map(rule => rule.trim());
    const rules = rulesArr.map(rule => ({
        type: rule.split(':')[0] as MFormInputRulesType,
        value: rule.split(':')[1]
    }));
    const errors = validator({ value, name: props.title }, rules);

    if (errors.length > 0) {
        errorVal.value = errors[0];
        return false;
    }

    errorVal.value = "";
    return true;
}

defineExpose({
    validate
});

</script>

<template>
    <div class="form-group" :class="containerClassname">
        <label :for="name" v-if="label">
            <span>{{ label }}</span>
            <span v-if="isMandatory" class="text-danger">*</span>
        </label>
        <div class="input-group">
            <span class="input-group-text" v-if="prependIcon">
                <m-icon :icon="prependIcon" />
            </span>

            <!-- Textarea -->
            <m-autosize-textarea v-if="inputType === 'textarea'" v-model="value" class="form-control"
                :class="{ 'is-invalid': errorValue, 'border-start-0': prependIcon, 'border-end-0': appendIcon || props.inputType === 'password' }"
                :placeholder="placeholder" @blur="validate" v-bind="$attrs"></m-autosize-textarea>
            <!-- Input -->
            <input v-else :type="state.inputType" v-model="value" :name="name" class="form-control"
                :class="{ 'is-invalid': errorValue, 'border-start-0': prependIcon, 'border-end-0': appendIcon || props.inputType === 'password' }"
                :placeholder="placeholder" @blur="validate" v-bind="$attrs" />

            <span class="invalid-tooltip" v-if="errorVal">
                {{ errorVal }}
            </span>
            <!-- Password Toggler -->
            <span :class="['input-group-text', appendIcon ? 'border-end-0' : '']" v-if="props.inputType === 'password'"
                @click="togglePassword">
                <m-icon v-if="state.inputType === 'password'" icon="carbon:view" />
                <m-icon v-else icon="carbon:view-off" />
            </span>
            <span class="input-group-text" v-if="appendIcon">
                <m-icon :icon="appendIcon" />
            </span>
        </div>
    </div>
</template>