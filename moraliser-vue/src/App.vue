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

<script lang="ts">
import MHeader from "@/components/MHeader.vue";
import { getData, type FetchResponseJSON } from "@/utils/fetchUtils";
import { mapMutations } from "vuex";
import type { UserInfo } from "@/types/Models";

export default {
  name: "m-app",
  components: {
    MHeader,
  },
  methods: {
    ...mapMutations(["setAuthUser"]),
  },
  mounted() {
    type FetchReqType = { [key: string]: UserInfo | string | null };
    getData<FetchReqType>(
      "/api/current",
      null,
      (res: FetchResponseJSON<FetchReqType>) => {
        // console.log(res);
        if (res.success)
          this.setAuthUser({
            user: res.data.user as UserInfo | null,
            csrf_token: res.data.csrf_token,
          });
        else console.log(res.message);
      }
    );
  },
};
</script>
