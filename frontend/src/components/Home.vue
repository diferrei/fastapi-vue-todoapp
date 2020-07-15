<template>
  <div class="container mt-5">
    <div v-if="selectedNote === null" class="columns is-multiline">
      <div v-for="(note, i) in notes" :key="note.text" class="column is-half">
        <note
          :text="note.text"
          :completed="note.completed"
          @complete-note="note.completed = true"
          @select-note="selectedNote = i"
        />
      </div>
    </div>
    <div v-else>
      <note-details
        :note="notes[selectedNote]"
        @go-back="selectedNote = null"
      />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Note from "@/components/Note.vue";
import { NoteType } from "@/types";
import NoteDetails from "@/components/NoteDetails.vue";

export default Vue.extend({
  name: "Home",
  components: { NoteDetails, Note },
  data(): {
    notes: NoteType[];
    selectedNote: null | number;
  } {
    return {
      notes: [
        { text: "Ir a comprar pan", completed: true },
        { text: "Terminar el Zelda", completed: false },
        { text: "Aprender Vue", completed: false },
        { text: "Terminar el Semestre", completed: false },
        { text: "Derrocar a Dani", completed: false },
        { text: "Crear una máquina para viajar en el tiempo", completed: false }
      ],
      selectedNote: null
    };
  }
});
</script>

<style scoped></style>
