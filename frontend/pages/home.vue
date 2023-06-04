<template>
  <div>
    <v-row>
      <v-col>
        <QRCode class="mt-10" />
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <v-card color="primary" class="rounded-b-xl" height="100" width="91%">
          <v-row>
            <v-col cols="6" align="center">
              <v-btn x-large icon color="white"><v-icon>mdi-qrcode-scan</v-icon></v-btn>
              <p class="white--text font-weight-bold">スキャン</p>
            </v-col>
            <v-col cols="6" align="center">
              <v-btn x-large icon color="white"> <v-icon>mdi-send</v-icon> </v-btn>
              <p class="white--text font-weight-bold">送る</p>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import QRCode from '@/components/QRCode'
import axios from 'axios'
export default {
  name: 'home',
  layout: 'loggedin',
  components: {
    QRCode,
  },
  data() {
    return {
      is_login: null,
      user: null,
    }
  },
  created() {
    this.is_login = this.$auth.loggedIn
    this.fetchuser()
  },
  methods: {
    async logout() {
      await this.$auth.logout()
    },
    async fetchuser() {
      const token = this.$auth.strategy.token.get()
      axios
        .get('http://localhost:8000/api/auth/users/me/', {
          headers: {
            'Content-Type': 'application/json',
            Authorization: token,
          },
        })
        .then((res) => {
          console.log(res.data)
        })
    },
  },
}
</script>
