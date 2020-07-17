import Vue from "vue";
import Vuex from "vuex";
import { NoteType } from "@/types";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    notes: [
      { text: "Ir a comprar pan", completed: true },
      { text: "Terminar el Zelda", completed: false },
      { text: "Aprender Vue", completed: false },
      { text: "Terminar el Semestre", completed: false },
      { text: "Derrocar a Dani", completed: false },
      { text: "Crear una máquina para viajar en el tiempo", completed: false }
    ],
    selectedNote: null
  },
  mutations: {
    addNote(state, note: NoteType) {
      state.notes.push(note);
    },
    selectNote(state, noteIdx) {
      state.selectedNote = noteIdx;
    },
    unselectNote(state) {
      state.selectedNote = null;
    }
  },
  actions: {
    addNote({ commit }, note: NoteType) {
      commit("addNote", note);
    }
  },
  modules: {}
});
