export type FetchMethodType = "POST" | "GET" | "PUT" | "DELETE";

export function fetchData(route: string, data: Array<string>, method: FetchMethodType, callback: Function) {
    const URL = window.location.origin.concat(route);
    const formData = new FormData();
    if (method === "POST") {
        const csrfToken: string = document.querySelector("meta[name='csrf_token']")?.getAttribute("content") || "";
        formData.append("csrf_token", csrfToken);
    }
    for (const i in data) formData.append(i, data[i] || "");

    fetch(URL, {
        body: formData,
        method
    })
        .then((res) => {
            if (res.status !== 200) {
                throw Error(res.statusText);
            }
            return res.json();
        })
        .then((res) => callback(res))
        .catch((err) => {
            console.error(err);
        });
}

export function postData(route: string, data: Array<string>, callback: Function) {
    fetchData(route, data, "POST", callback);
}

export function getData(route: string, data: Array<string>, callback: Function) {
    fetchData(route, data, "GET", callback);
}
