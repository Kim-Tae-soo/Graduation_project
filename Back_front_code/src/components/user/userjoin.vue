<template>
  <div class="text-center">
    <br>
    <v-img src="@/assets/logo.png" style="max-width: 12%;" class="mx-auto"></v-img>
    <br>
    <h1>Welcome to ATP MOUSE</h1>
  </div>
  
  <div class="signup-container">
    <br>
    
    <h1>JOIN</h1>
    <br>
    <form @submit.prevent="register">
      <div class="input-wrapper">
        <input type="text" id="username" v-model="username" class="input" required placeholder="name">
      </div>
      <div class="input-wrapper">
        <input type="email" id="email" v-model="email" class="input" required placeholder="e-mail">
      </div>
      <div class="input-wrapper">
        <input type="password" id="password" v-model="password" class="input" required placeholder="password">
      </div>
      <button type="submit">JOIN</button>
    </form>
    
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
  </div>
  <div class="text-center">
    
    <v-col class="mb-5" cols="12">
      <h2 class="headline font-weight-bold mb-5">
        Temperature & Heart rate <br>
        measurement Mouse
        <br>
      </h2>


      <h6 class="headline font-weight-bold mb-5" style="text-align: center;">
        <br>
        Mokwon University <br> Department of Information and Communication Engineering <br> Department of Industrial
        Design <br>
        2023 Fusion 2 trillion
      </h6>

      <v-row justify="center">
        <a v-for="(next, i) in CoustomerCenter" :key="i" :href="next.href" class="subheading mx-3" target="_blank">
          {{ next.text }}
        </a>
      </v-row>
    </v-col>
  </div>

</template>
<script>
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";

const firebaseConfig = {
  // Your Firebase configuration goes here
  apiKey: "AIzaSyBQtOBghGbgHpDYG3WLwjMZePxp0k4FFzE",
  authDomain: "atpproject-885d7.firebaseapp.com",
  databaseURL: "https://atpproject-885d7-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "atpproject-885d7",
  storageBucket: "atpproject-885d7.appspot.com",
  messagingSenderId: "943299899143",
  appId: "1:943299899143:web:a4e3d23d8389764353dfa2",
  measurementId: "G-M07E5QRW2N"
};

initializeApp(firebaseConfig);

export default {
  name: 'SellerSignup',
  data() {
    return {
      email: "",
      password: "",
      username: "",
      errorMessage: null,
      successMessage: null,
    };
  },
  methods: {
    async register() {
      const auth = getAuth();
      try {
        const result = await createUserWithEmailAndPassword(
          auth,
          this.email,
          this.password
        );
        const user = result.user;
        const userInfo = result.additionalUserInfo;
        if (userInfo && userInfo.isNewUser) {
          await user.updateProfile({
            displayName: this.username,
          });
        }
        this.successMessage = "Member registration has been completed successfully.";
        this.errorMessage = null; // 에러 메시지 초기화
      } catch (error) {
        const errorMessages = {
          "auth/email-already-in-use": "This e-mail address is already registered.",
          "auth/invalid-email": "Invalid email address.",
          "auth/weak-password": "Password must be at least 6 digits long.",
          default: "Member registration failed. please try again.",
        };
        this.errorMessage = errorMessages[error.code] || errorMessages.default;
        this.successMessage = null; // 성공 메시지 초기화
      }
    },
  },
};
</script>

<style scoped>
.error-message {
  color: red;
}

.success-message {
  color: green;
}

.signup-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-wrapper {
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-bottom: 1rem;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 300px;
}

.form-group {
  margin-bottom: 1rem;
}

.input {
  width: 100%;
  padding: 0.5rem;
  border-radius: 5px;
  border: 1px solid #ccc;
  text-align: left;
}

button[type="submit"] {
  padding: 0.5rem 1rem;
  border-radius: 5px;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
}
</style>