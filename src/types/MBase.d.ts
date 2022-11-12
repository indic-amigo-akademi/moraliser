export type Booleanish = "true" | "false" | "" | boolean;

export interface MColorVariantBase {
    primary: unknown;
    secondary: unknown;
    success: unknown;
    danger: unknown;
    warning: unknown;
    info: unknown;
    light: unknown;
    dark: unknown;
}

export type MColorVariant = keyof MColorVariantBase;
