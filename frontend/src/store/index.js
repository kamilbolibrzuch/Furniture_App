import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
        username: '',
        id: '',
        isAuthenticated: false,
        token: '',
    },
    search: {
        query: '',
    }
    
    
  },
  getters: {
  },
  mutations: { //nie możemy w state zmienić danych i robimy to w mutations
    initializeStore(state) { //funkcja inicjalizujaca nasz local Storage
        if (localStorage.getItem('token')) { //token użytkownika bedzie zapisany w localstorage gdyby wył przeglądarke itd..
            state.user.token = localStorage.getItem('token') // przypisanie tokenu
            state.user.isAuthenticated = true //jeli mamy token to mamy autoryzacje
        } else {
            state.user.token = '' //upewniamy się że token jest napewno pusty  
            state.user.isAuthenticated = false //brak autoryzacji
        }
        if (localStorage.getItem('username')) {
            state.user.username = localStorage.getItem('username')

        } else {
            state.user.username = ''
        }
        if (localStorage.getItem('id')) {
            state.user.id = localStorage.getItem('id')

        } else {
            state.user.id = ''
        }},
        setToken(state, token) { //funkcja przypisująca token przy zalogowaniu
          state.user.token = token
          state.user.isAuthenticated = true
      },

      removeToken(state) { //funkcja usuwajaca token przy wylogowaniu
          state.user.token = ''
          state.user.isAuthenticated = false
      },

      setUserId(state, id) {
          state.user.id = id
      },
      setUserName(state, username) {
          state.user.username = username
      },

      setQuery(state, query){//podczas korzystania z wyszukiwarki
        state.search.query = query
      },
      removeQuery(state) {
        state.search.query = ''
      },



      LogOutUser(state){
        state.user.username='';
        state.user.id=0;
        state.user.token = '';
        state.user.isAuthenticated=false;
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        localStorage.removeItem('profile_slug')
        localStorage.removeItem('id')
      }

  },
  actions: {
  },
  modules: {
  }
})
