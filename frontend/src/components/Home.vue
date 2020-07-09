<template>
  <div class="container mt-5">
    <div class="columns is-multiline">
      <div v-for="note in notes" :key="note.text" class="column is-half">
        <note
          :text="note.text"
          :completed="note.completed"
          @complete-note="note.completed = true"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Note from "@/components/Note.vue";

export default Vue.extend({
  name: "Home",
  components: { Note },
  data() {
    return {
      notes: [
        { text: "Ir a comprar pan", completed: true },
        { text: "Terminar el Zelda", completed: false },
        { text: "Aprender Vue", completed: false },
        { text: "Terminar el Semestre", completed: false },
        { text: "Derrocar a Dani", completed: false },
        { text: "Crear una máquina para viajar en el tiempo", completed: false }
      ]
    };
  }
});
</script>

<style scoped></style>
