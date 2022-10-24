<template>
    <div class="chat">
        <div class="chatbox-container" id="chatboxContainer">
            <m-chat-box v-for="(item, index) in chats" :key="index" v-bind="item" />
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
                    <input class="d-none" type="file" name="image" multiple />
                    <button class="btn btn-primary rounded-circle" type="submit">
                        <send-icon />
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import MCChatbox from "@/components/MCChatBox.vue";
import MdSend from "vue-material-design-icons/Send.vue";
// import NotifyTune from '@/assets/notify.mp3';

export default {
    name: "m-chat",
    data() {
        return {
            chats: [
                // {
                //   sender: {
                //     name: 'purbun',
                //     userid: 12
                //   },
                //   msg: 'Hi! How are you?',
                //   date: new Date().toISOString(),
                //   isCurrentUser: true
                // }
            ],
            message: ""
        };
    },
    updated() {
        // this.$nextTick(function () {
        //     const chatboxContainer = document.getElementById('chatboxContainer');
        //     chatboxContainer.scrollTop = chatboxContainer.scrollHeight;
        // });
    },
    components: {
        "m-chat-box": MCChatbox,
        "send-icon": MdSend
        // NotifyTune
    },
    methods: {
        // async sendMessage() {
        //     const audio = new Audio(NotifyTune);
        //     if (this.message.trim() === '') {
        //         return;
        //     }
        //     let newChat = {
        //         sender: {
        //             name: 'purbun',
        //             userid: 12
        //         }
        //     };
        //     const data = new FormData();
        //     data.append('message', this.message);
        //     newChat['msg'] = this.message;
        //     this.message = '';
        //     newChat['date'] = new Date().toISOString();
        //     newChat['isCurrentUser'] = true;
        //     this.chats.push(newChat);
        //     const res = await fetch(`http://${location.hostname}:${location.port}/api/text-validate`, {
        //         method: 'POST',
        //         body: data
        //     });
        //     if (res.status !== 200) {
        //         console.error(res.status + ' ' + res.statusText);
        //         return;
        //     }
        //     const jsonData = await res.json();
        //     if (jsonData['status'] === 'success') {
        //         newChat = {
        //             sender: {
        //                 name: 'damarin',
        //                 userid: 1
        //             }
        //         };
        //         newChat['msg'] = `${jsonData['spam_text']} ${jsonData['prof_text']}`;
        //         this.message = '';
        //         newChat['date'] = new Date().toISOString();
        //         newChat['isCurrentUser'] = false;
        //         this.chats.push(newChat);
        //         audio.play();
        //     }
        // }
    }
};
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
