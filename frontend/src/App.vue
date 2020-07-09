<template>
  <div id="app">
    <b-navbar type="is-dark" wrapper-class="container">
      <template slot="start">
        <b-navbar-item href="#">
          Home
        </b-navbar-item>
        <b-navbar-dropdown label="Info">
          <b-navbar-item href="#">
            About
          </b-navbar-item>
          <b-navbar-item href="#">
            Contact
          </b-navbar-item>
        </b-navbar-dropdown>
      </template>

      <template slot="end">
        <b-navbar-item tag="div">
          <div class="buttons">
            <a class="button is-primary">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light">
              Log in
            </a>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>

    <section>
      <home />
    </section>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Home from "@/components/Home.vue";

export default Vue.extend({
  name: "App",
  components: { Home }
});
</script>

<style lang="scss"></style>
