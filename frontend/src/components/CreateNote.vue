<template>
  <form>
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Añadir Nota</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Texto">
          <b-input
            type="textarea"
            v-model="newText"
            placeholder="Ingrese Texto"
            minlength="5"
            maxlength="100"
            use-html5-validation
          />
        </b-field>
        <b-field label="Completado">
          <b-checkbox v-model="newCompleted" />
        </b-field>
      </section>
      <footer class="modal-card-foot">
        <div>
          <b-button @click="$parent.close()">Close</b-button>
          <b-button @click="addNote()" class="button is-primary"
            >Añadir Nota</b-button
          >
        </div>
      </footer>
    </div>
  </form>
</template>

<script lang="ts">
import Vue from "vue";
import { NoteType } from "@/types";

export default Vue.extend({
  name: "CreateNote",
  data() {
    return {
      newText: "",
      newCompleted: false
    };
  },
  methods: {
    addNote() {
      if (this.newText.length >= 5) {
        const newNote: NoteType = {
          text: this.newText,
          completed: this.newCompleted
        };
        this.$store.dispatch("addNote", newNote);
        this.newText = "";
        this.newCompleted = false;
        this.$parent.close();
      }
    }
  }
});
</script>

<style scoped></style>
