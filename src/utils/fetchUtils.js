export function fetchData(route, data, method, callback) {
    const URL = window.location.origin.concat(route);
    const formData = new FormData();
    if (method === "POST") {
        const csrfToken = document.querySelector("meta[name='csrf_token']").getAttribute("content");
        formData.append("csrf_token", csrfToken);
    }
    for (const i in data) formData.append(i, data[i]);

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

export function postData(route, data, callback) {
    fetchData(route, data, "POST", callback);
}

export function getData(route, data, callback) {
    fetchData(route, data, "GET", callback);
}
