<template>
  <b-button @click="goBack">
    Volver
  </b-button>
</template>

<script>
export default {
  name: "GoBack",
  methods: {
    goBack() {
      return this.$router.back();
    }
  }
};
</script>

<style scoped></style>
