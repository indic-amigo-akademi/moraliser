<template>
  <textarea
    ref="textarea"
    rows="3"
    @input="resizeTextarea"
    style="width: 100%; resize: none"
  ></textarea>
</template>

<script lang="ts">
export default {
  name: "MAutosizeTextarea",
  props: {
    maxHeight: {
      type: Number,
      default: 100,
    },
  },
  data() {
    return {
      text: "",
    };
  },
  mounted() {},
  computed: {
    textarea(): HTMLTextAreaElement {
      return this.$refs.textarea as HTMLTextAreaElement;
    },
  },
  methods: {
    resizeTextarea() {
      console.log(this.textarea.scrollHeight);
      this.textarea.style.height = "auto"; // Reset the height
      if (this.textarea.scrollHeight > this.maxHeight)
        this.textarea.style.height = `${this.maxHeight}px`;
      else this.textarea.style.height = `${this.textarea.scrollHeight}px`; // Set the height to match the content
    },
  },
};
</script>
