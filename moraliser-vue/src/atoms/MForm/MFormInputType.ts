import type { ComputedRef } from 'vue';

export interface MFormInputTypeBase {
    text: unknown;
    password: unknown;
    number: unknown;
    email: unknown;
    url: unknown;
    tel: unknown;
    date: unknown;
    month: unknown;
    week: unknown;
    time: unknown;
    datetime: unknown;
    phone: unknown;
    textarea: unknown;
}

export type MFormInputType = keyof MFormInputTypeBase;

export interface MFormInputRulesBase {
    required: boolean;
    digits: number;
    minlength: number;
    maxlength: number;
    pattern: RegExp;
    phone: boolean;
    email: boolean;
    url: boolean;
}

export type MFormInputRulesType = keyof MFormInputRulesBase;

export function validator(
    field: { name: string; value: ComputedRef<any> },
    rules: { type: MFormInputRulesType; value: string }[],
): string[] {
    const errors: string[] = [];
    const isOptional = rules.some((rule) => rule.type === 'required');
    rules.forEach((rule) => {
        const field_value = field.value.value;
        switch (rule.type as MFormInputRulesType) {
            case 'required':
                if (!field_value) errors.push(`${field.name} is required`);
                break;
            case 'digits':
                if (
                    (isOptional && !field_value) ||
                    (/^\d+$/.test(field.value.toString()) && field_value.length !== rule.value)
                )
                    errors.push(`${field.name} must be ${rule.value} digits`);
                break;
            case 'minlength':
                if ((isOptional && !field_value) || field_value.length < rule.value)
                    errors.push(`${field.name} must be at least ${rule.value} characters`);
                break;
            case 'maxlength':
                if ((isOptional && !field_value) || field_value.length > rule.value)
                    errors.push(`${field.name} must be less than ${rule.value} characters`);
                break;
            //   case "pattern":
            //     if (!rule.value.test(field.value.value))
            //       errors.push(`${field.name} must match the pattern ${rule.value}`);
            //     break;
            case 'phone':
                if ((isOptional && !field_value) || !/^[0-9]{10}$/.test(field_value.toString()))
                    errors.push(`${field.name} must be a valid phone number`);
                break;
            case 'email':
                if (
                    (isOptional && !field_value) ||
                    !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(field_value.toString())
                ) {
                    errors.push(`${field.name} must be a valid email address`);
                }
                break;
            case 'url':
                if ((isOptional && !field_value) || !/^(http|https):\/\/[^ "]+$/.test(field_value.toString()))
                    errors.push(`${field.name} must be a valid url`);
                break;
            default:
                break;
        }
    });

    return errors;
}
