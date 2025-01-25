import { createRouter, createWebHistory } from "vue-router";
import Login from "@/views/account/Login.vue";
import SignUp from "@/views/account/SignUp.vue";
import EmailConfirmation from "@/views/account/EmailConfirmation.vue";
import ForgetPassword from "@/views/account/ForgetPassword.vue";
import Info from "@/views/app/me/Info.vue";
import ResetPassword from "@/views/account/ResetPassword.vue";
import ChangePassword from "@/views/account/ChangePassword.vue";
import ChangeEmail from "@/views/account/ChangeEmail.vue";
import Home from "@/views/app/Home.vue";
import Layout from "@/components/Layout.vue";
import CreateCourse from "@/views/app/me/CreateCourse.vue";
import Dashboard from "@/views/app/Dashboard.vue";
import InfoCourse from "@/views/app/InfoCourse.vue";
import InfoMyCourse from "@/views/app/me/InfoMyCourse.vue";
import EditCourse from "@/views/app/me/EditCourse.vue";
import Settings from "@/views/app/Settings.vue";
import EnrollCourses from "@/views/app/EnrollCourses.vue";
import MyModule from "@/views/app/me/MyModule.vue";
import Module from "@/views/app/Module.vue";
import LessonDetails from "@/views/app/LessonDetails.vue";
import MyLessonDetails from "@/views/app/me/MyLessonDetails.vue";
import StudentsList from "@/views/app/me/StudentsList.vue";


const account = [
  {
    path:"/account",
    children: [
      {
        path: "signup",
    
        name: "signup",
        component: SignUp,
      },
      {
        path: "login",
        name: "login",
        component: Login,
      },
      {
        path: "email-confirmation/:key",
        name: "emailConfirmation",
        component: EmailConfirmation,
      },
      {
        path: "forget-password",
        name: "forgetPassword",
        component: ForgetPassword,
      },
      {
        path: "reset-password/:uid/:token",
        name: "resetPassword",
        component: ResetPassword,
      },
      {
        path: "chnage-password",
        name: "changePassword",
        component: ChangePassword,
      },
      {
        path: "change-email",
        name: "changeEmail",
        component: ChangeEmail,
      },

    ]
  }
  
];
import Video from "@/views/app/Video.vue";
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
        path: "video",
        name: "Video",
        component: Video,
      },
      {
        path: "home",
        name: "Home",
        component: Home,
      },
      {
        path: "info",
        name: "Info",
        component: Info,
      },
      {
        path: "create-course",
        name: "CreateCourse",
        component: CreateCourse,
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: Dashboard,
      },
      {
        path: "info-course/:id",
        name: "InfoCourse",
        component: InfoCourse,
        props: true,
      },
      {
        path: "info-my-course/:id",
        name: "InfoMyCourse",
        component: InfoMyCourse,
        props: true,
      },
      {
        path: "edit-course",
        name: "EditCourse",
        component: EditCourse,
      },
      {
        path: "settings",
        name: "Settings",
        component: Settings,
      },
      {
        path: "enroll-courses",
        name: "EnrollCourses",
        component: EnrollCourses,
      },
      {
        path: "my-module/:id",
        name: "MyModule",
        component: MyModule,
        props: true,
      },
      {
        path: "module/:id",
        name: "Module",
        component: Module,
        props: true,
      },
      {
        path: "lesson-details/:lesson_id/:module_id",
        name: "LessonDetails",
        component: LessonDetails,
        props: true,
      },
      {
        path: "my-lesson-details/:lesson_id/:module_id",
        name: "MyLessonDetails",
        component: MyLessonDetails,
        props: true,
      },
      {
        path: "students-list/:id",
        name: "StudentsList",
        component: StudentsList,
        props: true,
      },

    ]
  },

  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/AboutView.vue"),
  },
];

const routes = [...account, ...app]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;