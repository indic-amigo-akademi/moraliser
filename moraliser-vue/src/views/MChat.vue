

<style lang="scss" scoped>
.chat {
    height: 100%;

    .chatbox-output-container {
        overflow-x: hidden;
        overflow-y: auto;
    }

    .chatbox-input-container {
        width: 100%;

        form.message-form {
            .form-group {
                .send-btn {
                    display: inline-block;
                    height: 40px;
                    width: 40px;
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
}
</style>

<script setup lang="ts">
import MFormInput from "@/atoms/MForm/MFormInput.vue";
import MChatbox from "@/components/MChatBox.vue";
import { postData, type FetchResponseJSON } from "@/utils/fetchUtils";
import type { ChatType } from "@/types/Models"
import { reactive } from "vue";
import NotifyTune from "@/assets/notify.mp3";
// import { postData } from "@/utils/fetchUtils";


//     updated() {
//         this.$nextTick(() => {
//             const chatboxContainer = document.getElementById(
//                 "chatboxContainer"
//             ) as HTMLElement;
//             chatboxContainer.scrollTop = chatboxContainer.scrollHeight;
//         });
//     },
//     components: {
//         "m-chat-box": MChatbox,
//         MFormInput
//     },

const state = reactive({
    message: "",
    chats: [] as ChatType[],
});


async function sendMessage() {
    // console.log("Send Message");

    type FetchReqType = { [key: string]: null };

    postData<FetchReqType>(
        "/api/send-message",
        { message: state.message },
        (res: FetchResponseJSON<FetchReqType>) => {
            if (res.success) {
                console.log(res.data);
                state.message = "";
            } else console.log(res.message);
        }
    );
    const audio = new Audio(NotifyTune);
    if (state.message.trim() === "") {
        return;
    }
    let newChat = {
        sender: {
            name: "Purbayan",
            userid: 12,
        },
    };

    // postData(
    //     "/api/text-validate",
    //     {
    //         message: state.message,
    //     },
    //     (res: Response) => {
    //         newChat.message = state.message;
    //         state.message = "";
    //         newChat.date = new Date().toISOString();
    //         newChat.isCurrentUser = true;
    //         state.chats.push(newChat);
    //         if (res.status === "success") {
    //             newChat = {
    //                 sender: {
    //                     name: "damarin",
    //                     userid: 1,
    //                 },
    //             };
    //             newChat.msg = `${res.spam_text} ${res.prof_text}`;
    //             state.message = "";
    //             newChat.date = new Date().toISOString();
    //             newChat.isCurrentUser = false;
    //             state.chats.push(newChat);
    //             audio.play();
    //         }
    //     }
    // );
};

</script>

<template>
    <div class="chat d-flex flex-column">
        <div class="chatbox-output-container flex-grow-1 p-2" id="chatboxContainer">
            <m-chatbox v-for="(chat, index) in state.chats" :key="index" :sender="chat.sender" :message="chat.message"
                :date="chat.date" :isCurrentUser="chat.isCurrentUser" />
        </div>

        <div class="chatbox-input-container p-2">
            <form class="message-form" @submit.prevent="sendMessage">
                <div class="form-group d-flex gap-2">
                    <m-form-input prepend-icon="simple-line-icons:emotsmile"
                        container-classname="flex-grow-1 rounded-pill" input-type="textarea" name="message"
                        v-model="state.message" cols="1" rows="1" placeholder="Type a message..." />
                    <input class="d-none" type="file" name="image" multiple />
                    <button class="btn btn-primary rounded-circle send-btn" type="submit">
                        <m-icon icon="carbon:send-filled" class="h4" />
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
