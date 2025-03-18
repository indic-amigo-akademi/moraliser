// import * as moment from "moment";

// export class MomentDate {
//   public getMonth(): Number {
//     return moment().month();
//   }
// }

export interface UserType {
  id: number;
  username: string;
  email: string;
  phone: string;
}

export interface ChatType {
  sender: UserType;
  message: string;
  date: string | Date;
  isCurrentUser: boolean;
}
