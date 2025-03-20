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
  value: any,
  rules: { type: MFormInputRulesType; value: string }[]
): boolean {
  return rules.reduce((acc, rule) => {
    switch (rule.type as MFormInputRulesType) {
      case "required":
        return acc && value !== "";
      case "digits":
        return acc && value.toString().length === rule.value;
      case "minlength":
        return acc && value.toString().length >= rule.value;
      case "maxlength":
        return acc && value.toString().length <= rule.value;
    //   case "pattern":
    //     return acc && rule.value.test(value.toString());
      case "phone":
        return acc && /^[0-9]{10}$/.test(value.toString());
      case "email":
        return (
          acc &&
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            value.toString()
          )
        );
      case "url":
        return acc && /^(http|https):\/\/[^ "]+$/.test(value.toString());
      default:
        return acc;
    }
  }, true);
}
