<template>
  <div>
    <b-button @click="$emit('go-back')">
      Volver
    </b-button>
    <b-field label="Texto">
      <b-input v-model="note.text" />
    </b-field>
    <b-field label="Completado">
      <b-checkbox v-model="note.completed" />
    </b-field>
  </div>
</template>

<script lang="ts">
export default {
  name: "NoteDetails",
  props: {
    note: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped></style>
