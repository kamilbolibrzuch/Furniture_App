import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/account/SignUp.vue'
import LogIn from '../views/account/LogIn.vue'
import HomeView from '../views/HomeView.vue'
import AddPost from '../views/posts/AddPost.vue'
import store from '../store' //importujemy store aby sprawdzić nasz state -> czyli czy jesteśmy zalogowani
import PostDetail from '../views/posts/PostDetail.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requireLogin: true //aby wejść wymagane jest zalogowanie się
  }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
      path: '/log-in',
      name: 'LogIn',
      component: LogIn
  },
  {
    path: '/add-post',
    name: 'AddPost',
    component: AddPost,
    meta: {
      requireLogin: true //aby wejść wymagane jest zalogowanie się
  }
  },
  {
    path: '/:post_slug/',
    name: 'PostDetail',
    component: PostDetail,
    meta: {
      requireLogin: true //aby wejść wymagane jest zalogowanie się
  }
  },



  {
    path: '/about',
    name: 'about',
    meta: {
      requireLogin: true //aby wejść wymagane jest zalogowanie się
  },

    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => { //zanim router wykonana jakieś przekierowanie na inną stronę
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) { //jeśli strona wymaga logowania i nie jesteśmy authentykowwani
      next('/log-in') //to przenieś nas z automatu na stronę logowania
  } else {
      next() //jeśli jesteśmy zalogowani to przenieś na stronę docelową
  }
})

export default router
