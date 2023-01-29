import store from "@/store";

export type FetchMethodType = "POST" | "GET" | "PUT" | "DELETE";

const locationURL = {
  dev: "http://localhost:4545",
  prod: "",
};

export interface FetchResponseJSON<T> {
  success: boolean;
  message: string;
  data: T;
}

export function toHeaders(headersJson: { [key: string]: string | null }) {
  const headers = new Headers();
  (Object.keys(headersJson) as (keyof typeof headersJson)[]).forEach((key) =>
    headers.append(key as string, headersJson[key] as string)
  );
  return headers;
}

export function getUrl(route: string) {
  const environ = import.meta.env.DEV ? "dev" : "prod";
  return locationURL[environ].concat(route);
}

export function fetchData<T>(
  route: string,
  data: { [key: string]: string } | null,
  method: FetchMethodType,
  callback: Function
) {
  const csrfToken: string | null = store.state.csrf_token;
  const headers = {};
  //   const headers = {
  //     "X-CSRF-TOKEN": csrfToken,
  //   };

  //   const URL = window.location.origin.concat(route);
  const URL = getUrl(route);
  if (method === "POST") {
    const formData = new FormData();
    formData.append("csrf_token", csrfToken as string);
    if (data) for (const i in data) formData.append(i, data[i] || "");

    fetch(URL, {
      body: formData,
      headers: toHeaders(headers),
      method,
      mode: "cors",
    })
      .then((res) => {
        if (res.status !== 200) {
          throw Error(res.statusText);
        }
        return res.json();
      })
      .then((resJson: FetchResponseJSON<T>) => callback(resJson))
      .catch((err) => {
        if (import.meta.env.DEV) console.log(err);
      });
  } else if (method == "GET") {
    // URL.concat(new URLSearchParams(data).toString());
    fetch(URL, {
      mode: "cors",
    })
      .then((res) => {
        if (res.status !== 200) {
          throw Error(res.statusText);
        }
        return res.json();
      })
      .then((resJson: FetchResponseJSON<T>) => callback(resJson))
      .catch((err) => {
        if (import.meta.env.DEV) console.log(err);
      });
  }
}

export function postData<T>(
  route: string,
  data: { [key: string]: string } | null,
  callback: Function
) {
  fetchData<T>(route, data, "POST", callback);
}

export function getData<T>(
  route: string,
  data: { [key: string]: string } | null,
  callback: Function
) {
  fetchData<T>(route, data, "GET", callback);
}
