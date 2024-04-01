<template>
  <div>
    <br>
    <h1 style="text-align: center">BPM Information</h1>
    <br>
    <div v-if="user && bpmData" style="text-align: center">
      
      <h4>User UID&nbsp;: {{ user.uid }}</h4>
      <br>
      <h4>User e-mail&nbsp;: {{ user.email }}</h4>
      <br>
      <div v-if="displayedBPMData.length > 0" class="graph-container" style="display: flex; justify-content: center;">
        <div v-for="(bpmItem, key) in displayedBPMData" :key="key" class="bar" :style="{ height: (bpmItem.bpm * 2) + 'px' }"></div>
      </div>
      <br>
      <ul>
        <li v-for="(bpmItem, key) in displayedBPMData" :key="key">
          <a @click="showBPM(bpmItem.bpm)">Measured BPM&nbsp;: {{ bpmItem.bpm }} bpm</a>
        </li>
      </ul>
      <br>
      <p v-if="bpmData">Average BPM&nbsp;: {{ calculateAverageBPM(displayedBPMData).toFixed(2) }} bpm</p>
      <br>
      <div v-if="totalPages > 1">
        <button v-for="page in totalPages" :key="page" @click="changePage(page)">{{ page }}</button>
      </div>
      <br>
    </div>
    <div v-else style="text-align: center">
      <p>Loading data...</p>
      <p>Please log in if you haven't done so.</p>
    </div>
  </div>
</template>

<script>
import { getAuth } from 'firebase/auth';
import { getDatabase, ref, onValue } from 'firebase/database';
import { initializeApp } from 'firebase/app';

const firebaseConfig = {
  // Firebase 프로젝트의 구성 정보를 입력하세요.
  apiKey: "AIzaSyBQtOBghGbgHpDYG3WLwjMZePxp0k4FFzE",
  authDomain: "atpproject-885d7.firebaseapp.com",
  databaseURL: "https://atpproject-885d7-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "atpproject-885d7",
  storageBucket: "atpproject-885d7.appspot.com",
  messagingSenderId: "943299899143",
  appId: "1:943299899143:web:a4e3d23d8389764353dfa2",
  measurementId: "G-M07E5QRW2N"
};

export default {
  name: 'BPMInfo',
  data() {
    return {
      user: null,
      bpmData: null,
      selectedBPM: null,
      currentPage: 1,
      itemsPerPage: 10,
    };
  },
  mounted() {
    this.getUserBPMData();
  },
  methods: {
    async getUserBPMData() {
      const auth = getAuth();
      const user = auth.currentUser;
      if (user) {
        this.user = user;
        const db = getDatabase();
        const bpmRef = ref(db, `users/${user.uid}/bpm`);
        onValue(bpmRef, (snapshot) => {
          const bpmData = snapshot.val();
          if (bpmData) {
            this.bpmData = Object.entries(bpmData).map(([key, value]) => ({
              id: key,
              bpm: value.bpm
            }));
          } else {
            this.bpmData = null;
          }
        });
      }
    },
    showBPM(bpm) {
      this.selectedBPM = bpm;
    },
    calculateAverageBPM(bpmData) {
      if (bpmData) {
        const sum = bpmData.reduce((total, bpmItem) => total + bpmItem.bpm, 0);
        return sum / bpmData.length;
      }
      return null;
    },
    // 이전 코드 생략...

    changePage(page) {
      this.currentPage = page;
    },
  },
  computed: {
    displayedBPMData() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      const sortedData = this.bpmData
        .filter(bpmItem => bpmItem.bpm >= 0) // 음수 값을 필터링하여 배열 생성
        .reverse(); // BPM 데이터를 역순으로 정렬한 배열 생성
      return sortedData.slice(startIndex, endIndex);
    },
    totalPages() {
      if (this.bpmData) {
        return Math.ceil(this.bpmData.length / this.itemsPerPage);
      }
      return 0;
    },
  },
  created() {
    // Firebase 앱 초기화
    initializeApp(firebaseConfig);
  },
};
</script>

<style scoped>
button {
  /* 버튼 크기 조정 */
  width: 100px;
  height: 40px;

  /* 사각형 테두리 스타일 */
  border: 2px solid black;
  border-radius: 4px;

  /* 기타 스타일 */
  margin: 5px;
  padding: 10px;
}
.graph-container {
  display: flex;
  align-items: flex-end;
  justify-content: flex-end; /* 그래프를 오른쪽으로 정렬 */
}

.bar {
  width: 20px;
  background-color: green;
  margin: 0 5px;
}
</style>
