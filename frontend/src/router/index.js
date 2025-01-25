import { createRouter, createWebHistory } from "vue-router";
import CreateArticle from "@/views/CreateArticle.vue";
import Login from "@/views/account/Login.vue";
import Signup from "@/views/account/Signup.vue";
import Layout from "@/components/Layout.vue";
import Dashboard from "@/views/Dashboard.vue";
import Home from "@/views/Home.vue";
import ArticlePage from "@/views/ArticlePage.vue";


const account = [
  {
    path: "/account",
    children: [
      {
        path: "login",

        name: "Login",
        component: Login,
      },
      {
        path: "signup",

        name: "Signup",
        component: Signup,
      },
    ],
  },
];

const app = [
  {
    path: '/', 
    redirect: {name:"Home"},
  },
  {
    path: "/app",
    component: Layout,
    children: [
      {
        path: "home",
        name: "Home",
        component: Home,
      },
      {
        path: "create-article",
        name: "CreateArticle",
        component: CreateArticle,
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard ,
      },
      {
        path: "article/:articleId",
        name: "ArticlePage",
        component: ArticlePage ,
        props: true,
      },
    ],
  },
];

const routes = [...account, ...app];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
