<template>
  <v-app>
    <v-main>
      <AppBar/>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
import AppBar from '/components/AppBar'
export default {
  components:{
    AppBar
  },
  data(){
    return {
    }
  },

}
</script>