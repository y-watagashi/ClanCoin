<template>
    <v-app>
      <v-main>
        <AppBar/>
        <Nuxt />
        <BottomNavi/>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import AppBar from '/components/AppBar'
  import BottomNavi from '@/components/BottomNavi'
  export default {
    components:{
      AppBar,
      BottomNavi,
    },
    data(){
      return {
      }
    },
  
  }
  </script>