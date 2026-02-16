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

<script setup lang="ts">
// import moment from "moment";
import type { UserType } from '@/types/Models';
import type { PropType } from 'vue';

// export default {
//   name: "m-chat-box",
//   props: {
//     sender: {
//       type: UserType,
//       default: () => {
//         return { name: "Hello" };
//       },
//     },
//     msg: String,
//     date: { type: String, default: new Date().toISOString() },
//     isCurrentUser: { type: Boolean, default: false },
//   },
//   methods: {
//     fromNow(date: Date | string) {
//       //   return moment(date).fromNow();
//       return date;
//     },
//   },
// };

const props = defineProps({
    sender: {
        type: Object as PropType<UserType>,
        default: () => {
            return {
                id: 0,
                username: "Username",
                email: "user@email.com",
                phone: "+1,1234567890"
            };
        },
    },
    msg: String,
    date: { type: [String, Date], default: new Date() },
    isCurrentUser: { type: Boolean, default: false },
})

function fromNow(date: Date | string) {
    return date
}
</script>



<template>
    <div class="chatbox" :class="{ current: isCurrentUser }">
        <div class="chatbox-header">
            <h3>{{ isCurrentUser ? "You" : sender.username }}</h3>
        </div>
        <div class="chatbox-body" :class="isCurrentUser ? 'chat-secondary' : 'chat-primary'">
            <div class="msg">{{ msg }}</div>
        </div>
        <div class="chatbox-footer">
            <div>
                {{ fromNow(date) }}
            </div>
        </div>
    </div>
</template>
