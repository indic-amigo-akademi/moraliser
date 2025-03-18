<style lang="scss" scoped>
.chat {
    height: calc(100vh - 60px);
    display: block;
}

.chatbox-input-container {
    padding: 0.75rem 0.5rem;
    height: 6rem;
    width: 100%;

    form.message-form {
        .form-group {
            display: flex;

            .send-btn {
                display: inline-block;
                height: 45px;
                width: 45px;
                margin-left: 0.5rem;
            }

            .text-msg-input {
                display: inline-block;
                width: calc(100% - 55px);
                resize: none;
                border-radius: 4rem;
            }
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

<template>
    <div class="chat">
        <div class="chatbox-container" id="chatboxContainer">
            <m-chat-box v-for="(chat, index) in chats" :key="index" :sender="chat.sender" :message="chat.message"
                :date="chat.date" :isCurrentUser="chat.isCurrentUser" />
        </div>

        <div class="chatbox-input-container">
            <form class="message-form" @submit.prevent="sendMessage">
                <div class="form-group">
                    <autosize-textarea cols="1" rows="1" class="form-control p-2 px-5 text-msg-input" name="message"
                        v-model="message" :max-height="200" placeholder="Type a message..."></autosize-textarea>
                    <input class="d-none" type="file" name="image" multiple />
                    <button class="btn btn-primary rounded-circle send-btn" type="submit">
                        <send-icon />
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script lang="ts">
import MAutosizeTextarea from "@/atoms/MAutosizeTextarea/MAutosizeTextarea.vue";
import MChatbox from "@/components/MChatBox.vue";
import { postData, type FetchResponseJSON } from "@/utils/fetchUtils";
import MdSend from "vue-material-design-icons/Send.vue";
import type { ChatType } from "@/types/Models"
// import NotifyTune from "@/assets/notify.mp3";
// import { postData } from "@/utils/fetchUtils";

export default {
    name: "m-chat",
    data() {
        return {
            chats: [] as ChatType[],
            message: "",
        };
    },
    updated() {
        this.$nextTick(() => {
            const chatboxContainer = document.getElementById(
                "chatboxContainer"
            ) as HTMLElement;
            chatboxContainer.scrollTop = chatboxContainer.scrollHeight;
        });
    },
    components: {
        "m-chat-box": MChatbox,
        "send-icon": MdSend,
        "autosize-textarea": MAutosizeTextarea,
    },
    methods: {
        async sendMessage() {
            console.log("Send Message");

            type FetchReqType = { [key: string]: null };

            //   postData<FetchReqType>(
            //     "/api/send-message",
            //     { message: this.message },
            //     (res: FetchResponseJSON<FetchReqType>) => {
            //       if (res.success) {
            //         console.log(res.data);
            //         this.message = "";
            //       } else console.log(res.message);
            //     }
            //   );
            //   const audio = new Audio(this.NotifyTune);
            //   if (this.message.trim() === "") {
            //     return;
            //   }
            //   let newChat = {
            //     sender: {
            //       name: "Purbayan",
            //       userid: 12,
            //     },
            //   };

            //   postData(
            //     "/api/text-validate",
            //     {
            //       message: this.message,
            //     },
            //     (res: Response) => {
            //       newChat.message = this.message;
            //       this.message = "";
            //       newChat.date = new Date().toISOString();
            //       newChat.isCurrentUser = true;
            //       this.chats.push(newChat);
            //       if (res.status === "success") {
            //         newChat = {
            //           sender: {
            //             name: "damarin",
            //             userid: 1,
            //           },
            //         };
            //         newChat.msg = `${res.spam_text} ${res.prof_text}`;
            //         this.message = "";
            //         newChat.date = new Date().toISOString();
            //         newChat.isCurrentUser = false;
            //         this.chats.push(newChat);
            //         audio.play();
            //       }
            //     }
            //   );
        },
    },
};
</script>
