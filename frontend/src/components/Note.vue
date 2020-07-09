<template>
  <b-message :type="{ 'is-success': completed, 'is-light': !completed }">
    <div class="level">
      <span>{{ text }}</span>
      <b-tooltip label="Completar" type="light">
        <b-button
          v-if="!completed"
          type="is-success"
          size="is-small"
          @click="$emit('complete-note')"
        >
          <b-icon icon="check" />
        </b-button>
      </b-tooltip>
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
  }
});
</script>

<style scoped></style>
