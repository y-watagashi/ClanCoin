<template>
    <div>
      <v-app-bar
        color="primary"
        dense
        dark
      >
        <v-avatar>
          <img :src="require(`assets/logo.svg`)" alt="">

        </v-avatar>
  
        <v-toolbar-title class="font-weight-bold">{{ appName }}</v-toolbar-title>

      </v-app-bar>
    </div>
  </template>

<script>
import themeConfig from '/themeConfig'
export default{
  data(){
    return{
      // themeConfig
      appName: themeConfig.app.name,
      appLogo: themeConfig.app.logo,
    }
  }
}
</script>