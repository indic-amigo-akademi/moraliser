<script setup lang="ts">
import { computed, reactive, type PropType } from 'vue';
import { validator, type MFormInputRulesType, type MFormInputType } from '@/atoms/MFormInput/MFormInputType'

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    inputType: {
        type: String as PropType<MFormInputType>,
        default: "text"
    },
    label: {
        type: String,
        default: "Name"
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

function validateInput() {
    const rulesArr = props.rules.length > 0 ? props.rules : props.rule.split(',').map(rule => rule.trim());
    const rules = rulesArr.map(rule => ({
        type: rule.split(':')[0] as MFormInputRulesType,
        value: rule.split(':')[1]
    }));
    validator(value.value, rules);
}

</script>

<template>
    <div class="form-group">
        <label :for="name">
            <span>{{ label }}</span>
            <span v-if="isMandatory" class="text-danger">*</span>
        </label>
        <div class="input-group mb-3">
            <span class="input-group-text" v-if="prependIcon">
                <m-icon :icon="prependIcon" />
            </span>
            <input :type="state.inputType" v-model="value" :name="name" class="form-control"
                :class="{ 'is-invalid': errorValue }" :placeholder="placeholder" v-bind="$attrs" />
            <span class="invalid-tooltip" v-if="errorValue">
                {{ errorValue }}
            </span>
            <!-- Password Toggler -->
            <span class="input-group-text" v-if="props.inputType === 'password'" @click="togglePassword">
                <m-icon v-if="state.inputType === 'password'" icon="carbon:view" />
                <m-icon v-else icon="carbon:view-off" />
            </span>
            <span class="input-group-text" v-if="appendIcon">
                <m-icon :icon="appendIcon" />
            </span>
        </div>
    </div>
</template>