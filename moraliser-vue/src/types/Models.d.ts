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

export interface Link {
  title: string;
  description: string;
  image: string;
  url: string;
  site: string;
  embed: boolean;
}

export interface Chat {
  content: string;
  links: Link[];
  author: UserInfo;
  created_at: string;
  updated_at: string;
}
