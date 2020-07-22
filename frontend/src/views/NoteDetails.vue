<template>
  <div>
    <b-field label="Texto">
      <b-input v-model="note.text" />
    </b-field>
    <b-field label="Completado">
      <b-checkbox v-model="note.completed" />
    </b-field>
    <go-back></go-back>
  </div>
</template>

<script lang="ts">
import GoBack from "@/components/GoBack.vue";
export default {
  name: "NoteDetails",
  components: { GoBack },
  props: {
    note: {
      type: Object,
      required: true
    },
    id: {
      type: Number,
      required: true
    }
  }
};
</script>

<style scoped></style>
