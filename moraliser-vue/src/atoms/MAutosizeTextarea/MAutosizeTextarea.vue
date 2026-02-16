<template>
  <textarea
    ref="textarea"
    rows="3"
    v-model="value"
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
    modelValue: {
      type: String,
      required: true,
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
    value: {
      get() {
        return this.modelValue;
      },
      set(value: string) {
        this.$emit("update:modelValue", value);
      },
    },
  },
  methods: {
    resizeTextarea() {
      //   console.log(this.textarea.scrollHeight);
      this.textarea.style.height = "auto"; // Reset the height
      if (this.textarea.scrollHeight > this.maxHeight) {
        this.textarea.style.height = `${this.maxHeight}px`;
        // console.log(this.maxHeight);
        // this.textarea.style.paddingLeft = "";
        // this.textarea.style.paddingRight = "";
      } else {
        this.textarea.style.height = `${this.textarea.scrollHeight}px`; // Set the height to match the content
        // console.log(this.textarea.scrollHeight);
        // this.textarea.style.paddingLeft = "";
        // this.textarea.style.paddingRight = "";
      }
    },
  },
};
</script>
