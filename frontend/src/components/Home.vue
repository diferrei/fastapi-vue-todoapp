<template>
  <div class="container mt-5">
    <div class="level">
      <b-button @click="addNote">Añadir Nota</b-button>
    </div>
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
      notes: this.$store.state.notes,
      selectedNote: this.$store.state.selectedNote
    };
  },
  methods: {
    addNote() {
      const newNote: NoteType = { text: "Nada", completed: false };

      this.$store.dispatch("addNote", newNote);
    }
  }
});
</script>

<style scoped></style>
