<template>
  <div class="container mt-5">
    <div class="level">
      <b-button @click="openModal">Añadir Nota</b-button>
      <b-modal :active.sync="modal" has-modal-card :destroy-on-hide="false">
        <CreateNote />
      </b-modal>
    </div>
    <div class="columns is-multiline">
      <div v-for="(note, i) in notes" :key="note.text" class="column is-half">
        <note
          :completed="note.completed"
          :text="note.text"
          @complete-note="note.completed = true"
          @select-note="
            $router.push({
              name: 'NoteDetails',
              params: { note: notes[i], id: i }
            })
          "
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Note from "@/components/Note.vue";
import { NoteType } from "@/types";
import CreateNote from "@/components/CreateNote.vue";

export default Vue.extend({
  name: "Home",
  components: { CreateNote, Note },
  data(): {
    notes: NoteType[];
    selectedNote: null | number;
    modal: boolean;
  } {
    return {
      notes: this.$store.state.notes,
      selectedNote: this.$store.state.selectedNote,
      modal: false
    };
  },
  methods: {
    openModal() {
      this.modal = !this.modal;
    }
  }
});
</script>

<style scoped></style>
