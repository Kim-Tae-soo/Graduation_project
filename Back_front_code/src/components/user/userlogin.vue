<template>
  <div>
    <br><br>
    <div style="display: flex; justify-content: center;">
      <v-img src="@/assets/logo.png" style="max-width: 12%;"></v-img>
    </div>
    <div class="login-container">
      <br><br>
      <h1>Welcome to ATP MOUSE</h1>
      <br>
      <div v-if="!user">
        <!-- 사용자가 로그인되어 있지 않은 경우 -->
        <form @submit.prevent="login">
          <div class="input-wrapper">
            <label for="email" class="label"></label>
            <input type="email" id="email" v-model="email" class="input" required placeholder="e-mail">
          </div>
          <div class="input-wrapper">
            <label for="password" class="label"></label>
            <input type="password" id="password" v-model="password" class="input" required placeholder="password">
          </div>
          <br>
          <button type="submit">LOGIN</button><br>
          <p><router-link to="/userjoin">JOIN</router-link></p>
        </form>
      </div>
      <div v-else>
        <!-- 사용자가 로그인되어 있는 경우 -->

        <div>
          <div class="text-center">
            <p>
              <v-icon left>mdi-account</v-icon>
              <span> : &nbsp;Hello,&nbsp; </span>
              <span class="username">{{ user.email }}&nbsp;!!</span>&nbsp;&nbsp;&nbsp;
              <v-btn class="mr-3 text-center" color="success" dark @click="logout">
                <v-icon left>mdi-logout</v-icon>
                LOGOUT
              </v-btn>
              <br><br><br>
              <v-img src="@/assets/qrcode.png" style="max-width: 40%; border: 2px solid green;" class="mx-auto"></v-img>
              <br>
              APP DOWNLOAD
            </p>     
          </div>  
        </div>
      </div>     
    </div>   
    <div class="text-center">

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-5">
          <br>
          Temperature & Heart rate <br>
          measurement Mouse
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
 </div>
</template>

<script>
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";

export default {
  name: 'SellerLogin',
  data() {
    return {
      email: "",
      password: "",
      user: {
        email: "",
        name: "",
      },
      errorMessage: null,
    };
  },
  created() {
    // Firebase에서 로그인 정보가 변경될 때마다 user 변수를 업데이트합니다.
    const auth = getAuth();
    onAuthStateChanged(auth, (user) => {
      this.user = user;

    });
  },
  methods: {
    async login() {
      const auth = getAuth();
      try {
        const userCredential = await signInWithEmailAndPassword(auth, this.email, this.password);
        this.$store.commit("setUser", userCredential.user); // Vuex store의 setUser 변이를 호출합니다.
        this.user = userCredential.user; // 사용자 정보를 업데이트한다.
        alert('로그인에 성공하였습니다!');
        this.$router.push("/userlogin");
      } catch (error) {
        console.log(error.code, error.message); // 오류 로그를 콘솔에 출력합니다.
        this.errorMessage = "다양한 서비스를 이용하려면 회원가입을 진행해주세요!";
        alert('비밀번호가 일치하지 않습니다.');
      }
    },
    async logout() {
      const auth = getAuth();
      try {
        await auth.signOut();
        alert('로그아웃하였습니다.');
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>


    
<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.greeting {
  background-color: #f8f8f8;
  padding: 10px;
  border-radius: 5px;
}

.username {
  color: #010306;
  font-weight: bold;
  font-size: 18px;
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