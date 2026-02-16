import { MColorVariantBase } from "./MBase";

export type MButtonType = "button" | "submit" | "reset";

export interface MButtonVariantBase extends MColorVariantBase {
  link: unknown;
  "outline-primary": unknown;
  "outline-secondary": unknown;
  "outline-success": unknown;
  "outline-danger": unknown;
  "outline-warning": unknown;
  "outline-info": unknown;
  "outline-light": unknown;
  "outline-dark": unknown;
}

export type MButtonVariant = keyof MButtonVariantBase;
