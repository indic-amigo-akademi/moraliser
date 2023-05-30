import store from "@/store";
import {
  postData,
  type FetchResponseJSON,
  redirectTo,
  getData,
} from "./fetchUtils";
import type { UserInfo } from "@/types/Models";

export function logoutUser() {
  type FetchReqType = { [key: string]: null };
  postData<FetchReqType>(
    "/api/logout",
    {},
    (res: FetchResponseJSON<FetchReqType>) => {
      if (res.success) {
        redirectTo("/");
        store.commit("setAuthUser", { user: null });
      } else console.log(res.message);
    }
  );
}

export function updateCurrentUser() {
  type FetchReqType = { [key: string]: UserInfo | string | null };
  getData<FetchReqType>(
    "/api/current",
    null,
    (res: FetchResponseJSON<FetchReqType>) => {
      if (res.success)
        store.commit("setAuthUser", {
          user: res.data.user as UserInfo | null,
          csrf_token: res.data.csrf_token,
        });
      else console.log(res.message);
    }
  );
}
