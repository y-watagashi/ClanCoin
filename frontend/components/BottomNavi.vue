<template>
  <div>
    <v-bottom-navigation absolute rounded v-model="value" shift class="rounded-pill">
      <v-btn value="recent">
        <span>履歴</span>

        <v-icon>mdi-history</v-icon>
      </v-btn>

      <v-btn x-large fab value="favorites">
        <span>ホーム</span>

        <v-icon>mdi-home</v-icon>
      </v-btn>


      <v-btn value="nearby">
        <span>アカウント</span>

        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </div>
</template>
<script>
export default {
  data: () => ({ value: 'recent' }),
}
</script>
