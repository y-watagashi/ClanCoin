export const state = () => ({
  is_login: false,
  refresh_token: null,
  access_token: '',
})

export const getters = {
  getLoginState(state){
    return state.is_login;
  },
  getRefreshToken(state) {
    return state.refresh_token
  },
  getAccessToken(state) {
    return state.access_token
  },
}

export const mutations = {
    updateLoginState(state, value){
        state.is_login = value
    },
    updateAccessToken(state, value){
      state.access_token = value
    }
}

export const actions = {
}