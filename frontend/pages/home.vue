<template>
  <div>
    <p>this is a home page</p>
    is_login: {{ is_login }} user: {{ user }}
    <p></p>
    <v-btn @click="logout">logout</v-btn>
    <v-btn @click="fetchuser">fetch user</v-btn>
    <QRCode/>
  </div>
</template>
<script>
import QRCode from '@/components/QRCode'
import axios from 'axios'
export default {
  name: 'home',
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
      axios.get('http://localhost:8000/api/auth/users/me/', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token
        }
      }).then((res) => {
        console.log(res.data)
      });
    },
  },
}
</script>
