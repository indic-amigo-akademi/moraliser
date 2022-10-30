<style lang="scss">
body,
#app {
    display: flex;
    width: 100%;
    height: 100vh;
    flex-direction: column;
}

main {
    padding: 0;
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto;
    overflow: hidden;
}

header,
footer {
    flex-shrink: 0;
    border-radius: 0px;
}
</style>

<template>
    <div id="app">
        <m-header></m-header>
        <main>
            <router-view />
        </main>
    </div>
</template>

<script>
import MHeader from "@/components/MHeader";
import store from "@/store";

export default {
    name: "m-app",
    components: {
        MHeader
    },
    mounted() {
        const data = new FormData();
        const csrfToken = document.querySelector("meta[name='csrf_token']").getAttribute("content");

        data.append("csrf_token", csrfToken);

        fetch(`http://${location.hostname}:${location.port}/api/current`, {
            method: "POST",
            body: data
        })
            .then((res) => {
                if (res.status !== 200) {
                    throw Error(res.statusText);
                }
                return res.json();
            })
            .then((res) => {
                console.log(res);
                store.commit("setAuthUser", { user: res.user });
            })
            .catch((err) => {
                console.error(err);
            });
    }
};
</script>
