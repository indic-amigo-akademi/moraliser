<template>
  <div class="chatbox" :class="{ current: isCurrentUser }">
    <div class="chatbox-header">
      <h3>{{ isCurrentUser ? "You" : sender.name }}</h3>
    </div>
    <div
      class="chatbox-body"
      :class="isCurrentUser ? 'chat-secondary' : 'chat-primary'"
    >
      <div class="msg">{{ msg }}</div>
    </div>
    <div class="chatbox-footer">
      <div>
        {{ fromNow(date) }}
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'MCChatBox',
  props: {
    sender: {
      type: Object,
      default: function () {
        return { name: 'Hello' }
      }
    },
    msg: String,
    date: { type: String, default: new Date().toISOString() },
    isCurrentUser: { type: Boolean, default: false }
  },
  methods: {
    fromNow: function (date) {
      return moment(date).fromNow()
    }
  }
}
</script>

<style lang="scss">
.chatbox {
  float:left;
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
    border-radius: 1.5rem;
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
