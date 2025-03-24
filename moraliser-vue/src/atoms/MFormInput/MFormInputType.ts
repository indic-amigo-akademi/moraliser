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
    field: { name: string; value: any },
    rules: { type: MFormInputRulesType; value: string }[],
): string[] {
    const errors: string[] = [];
    rules.forEach((rule) => {
        switch (rule.type as MFormInputRulesType) {
            case 'required':
                if (field.value !== '') errors.push(`${field.name} is required`);
                break;
            case 'digits':
                if (field.value.toString().length !== rule.value)
                    errors.push(`${field.name} must be ${rule.value} digits`);
                break;
            case 'minlength':
                if (field.value.toString().length < rule.value)
                    errors.push(`${field.name} must be at least ${rule.value} characters`);
                break;
            case 'maxlength':
                if (field.value.toString().length > rule.value)
                    errors.push(`${field.name} must be less than ${rule.value} characters`);
                break;
            //   case "pattern":
            //     if (!rule.value.test(field.value.toString()))
            //       errors.push(`${field.name} must match the pattern ${rule.value}`);
            //     break;
            case 'phone':
                if (!/^[0-9]{10}$/.test(field.value.toString()))
                    errors.push(`${field.name} must be a valid phone number`);
                break;
            case 'email':
                if (
                    !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
                        field.value.toString(),
                    )
                )
                    errors.push(`${field.name} must be a valid email address`);
                break;
            case 'url':
                if (!/^(http|https):\/\/[^ "]+$/.test(field.value.toString()))
                    errors.push(`${field.name} must be a valid url`);
                break;
            default:
                break;
        }
    });
    return errors;
}
