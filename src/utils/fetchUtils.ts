import type { FetchResponseJSON } from "./../types/Models.d";
export type FetchMethodType = "POST" | "GET" | "PUT" | "DELETE";

export function fetchData<T>(
  route: string,
  data: { [key: string]: string } | null,
  method: FetchMethodType,
  callback: Function
) {
  const URL = window.location.origin.concat(route);
  const formData = new FormData();
  if (method === "POST") {
    const csrfToken: string =
      document
        .querySelector("meta[name='csrf_token']")
        ?.getAttribute("content") || "";
    formData.append("csrf_token", csrfToken);
  }

  if (data) for (const i in data) formData.append(i, data[i] || "");

  fetch(URL, {
    body: formData,
    method,
  })
    .then((res) => {
      if (res.status !== 200) {
        throw Error(res.statusText);
      }
      return res.json();
    })
    .then((resJson: FetchResponseJSON<T>) => callback(resJson))
    .catch((err) => {
      console.error(err);
    });
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
