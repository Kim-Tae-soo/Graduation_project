// firebase.js

import firebase from 'firebase/app';
import 'firebase/database';
import 'firebase/auth';

const firebaseConfig = {
    // Firebase 구성 정보...
    apiKey: "AIzaSyBQtOBghGbgHpDYG3WLwjMZePxp0k4FFzE",
    authDomain: "atpproject-885d7.firebaseapp.com",
    databaseURL: "https://atpproject-885d7-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "atpproject-885d7",
    storageBucket: "atpproject-885d7.appspot.com",
    messagingSenderId: "943299899143",
    appId: "1:943299899143:web:a4e3d23d8389764353dfa2",
    measurementId: "G-M07E5QRW2N"
};

if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

export default firebase;
