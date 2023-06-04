import colors from 'vuetify/es5/util/colors'

export default {
  router: {
    middleware: ['auth'],
  },
  auth: {
    redirect: {
      login: '/signin',
      logout: '/signin',
      callback: false,
      home: '/home',
    },
    localStorage: false,
    //strategiesの中身に認証ロジックを書いていく
    strategies: {
      //localという認証方法を使う場合
      local: {
        token: {
          type: 'JWT',
          property: 'access'
        },
        //axiosでアクセスする際の設定
        endpoints: {
          login: {
            url: 'http://localhost:8000/api/auth/jwt/create/', //ログインするときにアクセスするurl
            method: 'post',
            propertyName: 'access', //サーバーから帰ってくるトークンの名前
          },
          // user: {
          //   url: 'http://localhost:8000/api/auth/users/me/', method: 'get', propertyName: false
          // },
          user: false,
          logout: false,
        },
      },
    },
  },
  server: {
    port: 3000, // default: 3000
    host: '0.0.0.0', // default: localhost
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - frontend',
    title: 'frontend',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    '@nuxtjs/composition-api/module',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/auth-next',
    '@nuxtjs/axios',
    'vue-sweetalert2/nuxt',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        light: {
          primary: '#00C9A8',
          accent: '#F97B22',
          secondary: '#BAA89B',
        },
        dark: {
          primary: '#F97B22',
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
