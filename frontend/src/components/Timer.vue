<template>
  <div>
    <span>
      {{ countDown }}
    </span>
  </div>
</template>

<script>
let interval = null;

export default {
  name: "Timer",
  props: {
    end: {
      type: String
    }
  },
  data() {
    return {
      now: Math.trunc(new Date().getTime() / 1000),
      date: null,
      diff: 0,
      state: "is-light"
    };
  },
  created() {
    this.date = Math.trunc(Date.parse(this.end.replace(/-/g, "/")) / 1000);

    interval = setInterval(() => {
      this.now = Math.trunc(new Date().getTime() / 1000);
    });
  },
  computed: {
    countDown() {
      const seconds = this.twoDigits(Math.trunc(this.diff) % 60);
      const minutes = this.twoDigits(Math.trunc(this.diff / 60) % 60);
      const hour = Math.trunc(this.diff / 60 / 60) % 60;

      if (hour < 24 && hour >= 6) this.emitState("is-warning");
      if (hour <= 6) this.emitState("is-danger");

      return `${hour}:${minutes}:${seconds}`;
    }
  },
  methods: {
    startTimer() {
      if (this.timeLeft > 0)
        this.timeInterval = setInterval(() => (this.timePassed += 1), 1000);
      else clearInterval(this.timeInterval);
    },
    onTimeUp() {
      clearInterval(this.timeInterval);
    },
    twoDigits(digit) {
      if (digit < 10) {
        digit = `0${digit}`;
      }
      return digit;
    },
    emitState(value) {
      this.state = value;
      this.$emit("state-time", this.state);
    }
  },
  watch: {
    now() {
      this.diff = this.date - this.now;
      if (this.diff <= 0) {
        this.diff = 0;
        clearInterval(interval);
      }
    }
  },
  destroyed() {
    clearInterval(interval);
  }
};
</script>
