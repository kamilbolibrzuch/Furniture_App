import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/account/SignUp.vue'
import LogIn from '../views/account/LogIn.vue'
import LogOut from '../views/account/LogOut.vue'
import HomeView from '../views/HomeView.vue'
import AddPost from '../views/posts/AddPost.vue'
import store from '../store' //importujemy store aby sprawdzić nasz state -> czyli czy jesteśmy zalogowani
import PostDetail from '../views/posts/PostDetail.vue'
import Posts from '../views/posts/Posts.vue'

const routes = [

  { path: '/sign-up', name: 'SignUp', component: SignUp},                             //REJESTRACJA
  { path: '/log-in', name: 'LogIn', component: LogIn},                                //LOGOWANIE
  { path: '/log-out', name: 'LogOut', component: LogOut},                             //WYLOGOWYWANIE
  { path: '/', name: 'home', component: HomeView,                                     //STRONA GŁÓWNA
    meta: { requireLogin: true }//aby wejść wymagane jest zalogowanie się
  },
  { path: '/add-post', name: 'AddPost', component: AddPost,                           //DODAWANIE POSTU
    meta: {requireLogin: true }
  },
  { path: '/:post_slug', name: 'PostDetail', component: PostDetail,                   //DETALE POSTU
    meta: { requireLogin: true }
  },
  { path: '/posts/:pagenumber/:order_by', name: 'Posts', component: Posts,            //POSTY Z PAGINACJĄ
    meta: { requireLogin: true }
  },
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
