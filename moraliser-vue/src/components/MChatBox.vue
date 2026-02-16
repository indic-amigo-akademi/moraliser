<style lang="scss">
.chatbox {
  float: left;
  clear: both;
  padding: 0.25rem 0.5rem;
  margin: 1rem 0;
  min-width: 100px;
  width: calc(100% - 2rem);
  max-width: 300px;

  .chatbox-header {
    h3 {
      font-weight: 700;
      font-size: 1rem;
    }
  }

  .chatbox-body {
    position: relative;
    width: 100%;
    padding: 0.5rem;
    // border-radius: 1.5rem;
    border-top-left-radius: 0;

    &:after {
      content: "";
      position: absolute;
      top: -11px;
      left: 0;
    }

    .msg {
      font-weight: 500;
      font-size: 0.85rem;
    }
  }

  .chatbox-footer {
    font-weight: 300;
    opacity: 0.75;
    font-size: 0.7rem;
    text-align: right;
  }

  &.current {
    float: right;

    .chatbox-header h3 {
      text-align: right;
    }

    .chatbox-body {
      border-radius: 1.5rem;
      border-top-right-radius: 0;

      &:after {
        content: "";
        position: absolute;
        left: initial;
        right: 0;
      }
    }

    .chatbox-footer {
      text-align: left;
    }
  }
}
</style>

<template>
  <div class="chatbox" :class="{ current: isCurrentUser }">
    <div class="chatbox-header">
      <h3>{{ isCurrentUser ? "You" : author.username }}</h3>
    </div>
    <div
      class="chatbox-body"
      :class="isCurrentUser ? 'chat-secondary' : 'chat-primary'"
    >
      <div class="msg">{{ content }}</div>
    </div>
    <div class="chatbox-footer">
      <div>
        {{ fromNow(created_at) }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
// import moment from "moment";
import type { UserInfo, Link } from "@/types/Models";
import type { PropType } from "vue";

export default {
  name: "m-chat-box",
  props: {
    author: {
      type: Object as PropType<UserInfo>,
      default: () => {
        return { username: "Hello" };
      },
    },
    content: String,
    links: {
      type: Array as PropType<Link[]>,
      default: () => {
        return [];
      },
    },
    created_at: { type: String, default: new Date().toISOString() },
    updated_at: { type: String, default: new Date().toISOString() },
  },
  computed: {
    isCurrentUser() {
      return true;
    },
  },
  methods: {
    fromNow(date: Date | string) {
      //   return moment(date).fromNow();
      return date;
    },
  },
};
</script>
