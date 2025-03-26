<script setup lang="ts">
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

defineProps({
    msg: String
})

const store = useStore();
const router = useRouter()

const isGuest = computed(() => store.getters.isGuest);
function gettingStarted() {
    console.log(store.state.auth);
    if (isGuest.value) {
        store.dispatch('openLoginModal');
    }
    else {
        router.push('/chat')
    }
}
</script>

<template>
    <section class="hello-section p-4 bg-gray-200 rounded-3">
        <div class="container-fluid py-5 text-center">
            <h1>{{ msg }}</h1>
            <p class="lead">A new safe and filtered messaging app.</p>

            <button class="btn btn-primary" @click.prevent="gettingStarted"> Getting Started </button>
        </div>
    </section>
</template>
