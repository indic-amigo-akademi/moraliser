<template>
  <div class="chat">
    <div class="chatbox-container">
      <MCChatbox v-for="(item, index) in chats" :key="index" v-bind="item" />
    </div>

    <div class="chatbox-input-container">
      <form class="message-form" @submit.prevent="sendMessage">
        <div class="form-group">
          <input
            class="form-control rounded-pill text-msg"
            type="name"
            name="message"
            v-model="message"
            placeholder="Type a message..."
          />
          <input class="d-none" type="file" name="image" multiple>
          <button class="btn btn-primary rounded-circle" type="submit">
            <MdSend />
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import MCChatbox from '@/components/MCChatBox.vue'
import MdSend from 'vue-material-design-icons/Send.vue'

export default {
  name: 'chat',
  data () {
    return {
      chats: [
        {
          sender: {
            name: 'purbun',
            userid: 12
          },
          msg: 'Hi! How are you?',
          date: new Date().toISOString(),
          isCurrentUser: true
        }
      ],
      message: ''
    }
  },
  components: {
    MCChatbox,
    MdSend
  },
  methods: {
    sendMessage () {
      if (this.message.trim() === '') { return }
      let newChat = { sender: {
        name: 'purbun',
        userid: 12
      } }
      newChat['msg'] = this.message
      this.message = ''
      newChat['date'] = new Date().toISOString()
      newChat['isCurrentUser'] = true
      this.chats.push(newChat)
    }
  }
}
</script>

<style lang="scss">
.chat {
  height: calc(100vh - 60px);
  display: block;
}
.chatbox-input-container {
  padding: 0.75rem 0.5rem;
  height: 70px;
  width: 100%;
  form.message-form {
    button {
      display: inline-block;
      height: 45px;
      width: 45px;
      margin-left: 0.5rem;
    }
    input.text-msg {
      display: inline-block;
      width: calc(100% - 55px);
      padding: 1.3rem;
    }
  }
}
.chatbox-container {
  padding: 0.5rem;
  overflow-x: hidden;
  overflow-y: auto;
  height: calc(100% - 70px);
}
</style>
