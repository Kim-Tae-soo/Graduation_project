<template>
  <v-app>
    <v-navigation-drawer v-model="menu" app>
      <v-list>
        <v-list-item @click="button1Click">
          <v-list-item-title>Main</v-list-item-title>
        </v-list-item>
        <v-list-item @click="button3Click">
          <v-list-item-title>User BPM history</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="!isLoggedIn" @click="button5Click">

        <v-list-item-title>User temperature history</v-list-item-title>
        </v-list-item>
        </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="green" dense>
      <v-app-bar-nav-icon @click.stop="menu = !menu"></v-app-bar-nav-icon>
      
      <v-spacer></v-spacer><v-spacer></v-spacer>
      <a href="/" style="display: inline-block; padding: 10px 20px;  color: white; text-decoration: none; font-size: 30px; text-align: center;">ATP MOUSE&nbsp;</a>
      <v-spacer></v-spacer><v-spacer></v-spacer>
      <v-btn icon v-if="isLoggedIn" class="mr-2" @click="logout">
      <v-avatar size="32" :tile="false">
        <img :src="user.photoURL" :alt="user.displayName">
      </v-avatar>
       </v-btn>
      <v-btn icon v-else @click="button4Click">
        <v-icon left>mdi-account</v-icon> 
      </v-btn> 
    </v-app-bar>
    <v-main>
      <v-content>
        <router-view :isLoggedIn="isLoggedIn" :loginInfo="loginInfo" @login="login" @logout="logout">
        </router-view>
      </v-content>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      menu: false,
      isLoggedIn: false,
      user: null,
      loginInfo: null
    }
  },
  methods: {
    // 버튼 클릭 시 페이지 이동
    button1Click() {
      this.$router.push('/');
    },
    button3Click() {
      this.$router.push('/bpm');
    },
    button4Click() {
      if (this.isLoggedIn) {
        this.$router.push('/SellerSelect');
      } else {
        this.$router.push('/userlogin');
      }
    },
    button5Click() {
      this.$router.push('/temp');
    },
    login(user) {
      this.isLoggedIn = true;
      this.user = user;
    },
    logout() {
      this.isLoggedIn = false;
      this.user = null;
      this.$router.push('/');
    }
  }
}
</script>
