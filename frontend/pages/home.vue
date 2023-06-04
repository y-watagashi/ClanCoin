<template>
  <div>
    <v-row>
      <v-col>
        <QRCode class="mt-10" />
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
