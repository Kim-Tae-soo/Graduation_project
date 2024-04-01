import { createApp } from 'vue'
import { initializeApp } from 'firebase/app'
import { getDatabase } from 'firebase/database'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

// Firebase 구성 정보...
const firebaseConfig = {
  apiKey: "AIzaSyBQtOBghGbgHpDYG3WLwjMZePxp0k4FFzE",
  authDomain: "atpproject-885d7.firebaseapp.com",
  databaseURL: "https://atpproject-885d7-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "atpproject-885d7",
  storageBucket: "atpproject-885d7.appspot.com",
  messagingSenderId: "943299899143",
  appId: "1:943299899143:web:a4e3d23d8389764353dfa2",
  measurementId: "G-M07E5QRW2N"
};

// Firebase 초기화
initializeApp(firebaseConfig);

// 데이터베이스 참조
const database = getDatabase();

loadFonts();

createApp(App)
  .use(store)
  .use(router)
  .use(vuetify)
  .provide('database', database)
  .mount('#app');
