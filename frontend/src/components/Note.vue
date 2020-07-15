<template>
  <b-message :type="noteType">
    <div class="level">
      <span>{{ text }}</span>
      <div class="level-right">
        <b-tooltip label="Completar" type="is-light">
          <b-button
            v-if="!completed"
            type="is-success"
            size="is-small"
            @click="$emit('complete-note')"
          >
            <b-icon icon="check" />
          </b-button>
        </b-tooltip>
        <b-tooltip label="Detalles" type="is-light">
          <b-button
            v-if="!completed"
            type="is-light"
            size="is-small"
            @click="$emit('select-note')"
          >
            <b-icon icon="dots-horizontal" />
          </b-button>
        </b-tooltip>
      </div>
    </div>
  </b-message>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Note",
  props: {
    text: {
      type: String,
      required: true
    },
    completed: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    noteType(): string {
      return this.completed ? "is-success" : "is-light";
    }
  }
});
</script>

<style scoped></style>
