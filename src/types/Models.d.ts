// import * as moment from "moment";

// export class MomentDate {
//   public getMonth(): Number {
//     return moment().month();
//   }
// }

export interface UserInfo {
  id: number;
  username: string;
  email: string;
  phone: string;
}

export interface FetchResponseJSON<T> {
  success: boolean;
  message: string;
  data: T;
}

export type ErrorType = { [key: string]: { [key: string]: Array<string> } };
