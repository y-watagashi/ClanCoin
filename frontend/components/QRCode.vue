<template>
  <v-app>
    <v-row>
      <v-col align="center">
        <v-card rounded elevation="10" width="90%">
          <v-row>
            <v-col align="center" cols="6" class="mt-8">
              <p style="font-size: 15pt;" class="font-weight-bold">利用可能額</p>
              <span style="font-size: 25pt">{{ balance }} </span>
              <span style="font-size: 15pt; color: #424242;">PPC</span>
            </v-col>
            <v-col cols="5">
              <qrcode value="test message" :options="{ width: 160 }" />
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>
<script>
export default {
  data() {
    return {
      balance: 100,
    }
  },
}
</script>
