<template>
  <div>
    <br>
    <h1 style="text-align: center">Temperature Information</h1>
    <br>
    <div v-if="user && temperatureData" style="text-align: center">

      <h4>User UID&nbsp;: {{ user.uid }}</h4>
      <br>
      <h4>User e-mail&nbsp;: {{ user.email }}</h4>
      <br>
      <div v-if="displayedTemperatureData.length > 0" class="graph-container"
        style="display: flex; justify-content: center;">
        <div v-for="(tempItem, key) in displayedTemperatureData" :key="key" class="bar"
          :style="{ height: (tempItem.temperature * 2) + 'px' }"></div>
      </div>
      <br>
      <ul>
        <li v-for="(tempItem, key) in displayedTemperatureData" :key="key">
          <a @click="showTemperature(tempItem.temperature)">Measured Temperature&nbsp;: {{ tempItem.temperature }} °C</a>
        </li>
      </ul>
      <br>
      <p v-if="temperatureData">Average Temperature&nbsp;: {{ calculateAverageTemperature(displayedTemperatureData).toFixed(2) }} °C</p>
      <br>
      <div v-if="totalTempPages > 1">
        <button v-for="page in totalTempPages" :key="page" @click="changeTempPage(page)">{{ page }}</button>
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
  // Firebase project configuration
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
  name: 'TemperatureInfo',
  data() {
    return {
      user: null,
      temperatureData: null,
      selectedTemperature: null,
      currentTempPage: 1,
      tempItemsPerPage: 10,
    };
  },
  mounted() {
    this.getUserTemperatureData();
  },
  methods: {
    async getUserTemperatureData() {
      const auth = getAuth();
      const user = auth.currentUser;
      if (user) {
        this.user = user;
        const db = getDatabase();
        const tempRef = ref(db, `users/${user.uid}/temperature`);
        onValue(tempRef, (snapshot) => {
          const temperatureData = snapshot.val();
          if (temperatureData) {
            this.temperatureData = Object.entries(temperatureData).map(([key, value]) => ({
              id: key,
              temperature: value.temperature
            }));
          } else {
            this.temperatureData = null;
          }
        });
      }
    },
    showTemperature(temperature) {
      this.selectedTemperature = temperature;
    },
    calculateAverageTemperature(temperatureData) {
      if (temperatureData) {
        const sum = temperatureData.reduce((total, tempItem) => total + tempItem.temperature, 0);
        return sum / temperatureData.length;
      }
      return null;
    },
    // Remaining methods...
    // ...

    changeTempPage(page) {
      this.currentTempPage = page;
    },
  },
  computed: {
    displayedTemperatureData() {
      const startIndex = (this.currentTempPage - 1) * this.tempItemsPerPage;
      const endIndex = startIndex + this.tempItemsPerPage;
      const sortedData = this.temperatureData
        .filter(tempItem => tempItem.temperature >= 0)
        .reverse();
      return sortedData.slice(startIndex, endIndex);
    },
    totalTempPages() {
      if (this.temperatureData) {
        return Math.ceil(this.temperatureData.length / this.tempItemsPerPage);
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
