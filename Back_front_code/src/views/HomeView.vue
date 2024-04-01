<template>
  <div class="home">
    <ATPMOSE msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import ATPMOSE from '@/components/welcomATP.vue'

export default {
  name: 'HomeMarket',
  components: {
    ATPMOSE
  }
}
</script>
