<template>
  <v-container class="fill-height" style="background-color: #DFE0DF">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="8" md="6" lg="4" class="mx-auto" align="center">
        <v-card elavation="12">
          <v-card-text class="mb-n8">
            <p class="text-h4 font-weight-bold black--text">Sign in to ClanCoin</p>
            <br />
          </v-card-text>

          <!-- login form -->
          <v-card-text>
            <v-form @submit.prevent>
              <v-text-field
                v-model="email"
                outlined
                label="Email"
                placeholder="email"
                hide-details="auto"
                class="mb-6"
              >
              </v-text-field>

              <v-text-field
                v-model="password"
                outlined
                :type="isPasswordVisible ? 'text' : 'password'"
                label="Password"
                placeholder="Password"
                :append-icon="
                  isPasswordVisible
                    ? icons.mdiEyeOffOutline
                    : icons.mdiEyeOutline
                "
                hide-details="auto"
                class="mb-2"
                @click:append="isPasswordVisible = !isPasswordVisible"
              ></v-text-field>

              <div class="d-flex align-center justify-space-between flex-wrap">
                <v-checkbox hide-details label="Remember Me" class="mt-0">
                </v-checkbox>

                <!-- forget link -->
                <a class="ms-3 blue--text" href="#"> パスワードをお忘れですか? </a>
              </div>

              <v-btn block color="accent" type="submit" class="mt-6 font-weight-bold">
                Sign in
              </v-btn>
            </v-form>
          </v-card-text>

          <!-- create new account  -->
          <v-card-text
            class="d-flex align-center justify-center flex-wrap mt-2"
          >
            <p class="mb-0 me-2">初めてですか?</p>
            <a href="#" class="blue--text"> アカウントを新規作成 </a>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { mdiEyeOutline, mdiEyeOffOutline } from '@mdi/js'
import { ref } from '@nuxtjs/composition-api'
import themeConfig from '../themeConfig'

export default {
  middleware: 'authenticator',
  name: 'signin',
  layout: 'signin',
  setup() {
    const isPasswordVisible = ref(false)

    const email = ref('')
    const password = ref('')

    return {
      isPasswordVisible,
      email,
      password,

      // Icons
      icons: {
        mdiEyeOutline,
        mdiEyeOffOutline,
      },

      // themeConfig
      appName: themeConfig.app.name,
      appLogo: themeConfig.app.logo,
    }
  },
}
</script>
