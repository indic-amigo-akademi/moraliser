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
import { postData } from "@/utils/fetchUtils";
import { useAppStore } from "@/store";
import { mapActions } from "pinia";
import type { UserInfo, FetchResponseJSON } from "@/types/Models";

export default {
  name: "m-app",
  components: {
    MHeader,
  },
  methods: {
    ...mapActions(useAppStore, ["setAuthUser"]),
  },
  mounted() {
    postData<{ [key: string]: UserInfo | null }>(
      "/api/current",
      null,
      (res: FetchResponseJSON<{ [key: string]: UserInfo | null }>) => {
        // console.log(res);
        this.setAuthUser(res.data.user as UserInfo | null);
      }
    );
  },
};
</script>
