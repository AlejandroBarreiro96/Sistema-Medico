<template>
    <div>
      <form @submit.prevent="submitForm">
        <div>
          <label for="username">Username</label>
          <input id="username" type="text" v-model="username" />
        </div>
        <div>
          <label for="password">Password</label>
          <input id="password" type="password" v-model="password" />
        </div>
        <button type="submit">Login</button>
      </form>
      <div v-if="responseMessage">{{ responseMessage }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        responseMessage: '',
      }
    },
    methods: {
      submitForm() {
        // Enviar los datos a la API
        axios.post('/api/login', {
          username: this.username,
          password: this.password,
        }).then((response) => {
          // Mostrar el mensaje de respuesta
          this.responseMessage = response.data.message;
        }).catch((error) => {
          // Mostrar el mensaje de error
          this.responseMessage = error.response.data.message;
        });
      },
    },
  };
  </script>