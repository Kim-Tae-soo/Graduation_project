<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
      </v-col>
      <v-col class="mb-4">
        
        <h1>
          Welcome ATP MOUSE
          <br><br>
        </h1>
        <div style="display: flex; justify-content: center;">
          <v-img src="@/assets/logo.png" style="max-width: 20%;"></v-img>
          
        </div>

      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-5">
          <br>
          Temperature & Heart rate <br>
          measurement Mouse
        </h2>
        <br><br><br><br>
        <br>

        <h6 class="headline font-weight-bold mb-5" style="text-align: center;">
          <br><br><br>
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

    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'HelloWorld',

  data: () => ({
    CoustomerCenter: [
      {
        text: '',
      },

    ],
  }),
}
</script>
