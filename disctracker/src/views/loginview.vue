<template>
    <div class="min-h-screen flex flex-col items-center justify-top bg-blue-500">
      <img src="../assets/logo.png" alt="Disctracker" class="mb-8"> 
      <div class="bg-white p-8 rounded shadow-md w-80 -mt-20">
        <h2 class="text-xl font-bold mb-4">{{mode=='signin' ? 'Log in': 'Sign up'}}</h2>
        <form v-if="mode === 'signin'" @submit.prevent="handleSignin">
          <div class="mb-4">
            <label for="username" class="block text-gray-700 font-bold mb-2">Username</label>
            <input type="text" v-model="username" id="username" name="username" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-4">
            <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
            <input type="password" v-model="password" id="password" name="password" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
        </form>
        <form v-if="mode === 'signup'" @submit.prevent="handleSignup">
          <div class="mb-4">
            <label for="username" class="block text-gray-700 font-bold mb-2">Username</label>
            <input type="text" v-model="username" id="username" name="username" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-4">
            <label for="email" class="block text-gray-700 font-bold mb-2">Email</label>
            <input type="email" v-model="email" id="email" name="email" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-4">
            <label for="gender" class="block text-gray-700 font-bold mb-2">Gender</label>
            <select v-model="gender" id="gender" name="gender" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
            <option value ="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
            </select>
          </div>
          <div class="mb-4">
            <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
            <input type="password" v-model="password" id="password" name="password" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-6">
            <label for="repeatpsw" class="block text-gray-700 font-bold mb-2">Repeat password</label>
            <input type="password" v-model="repeatpsw" id="repeatpsw" name="repeatpsw" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
        </form>
          <div class="flex items-center justify-between">
            <div class="flex items-center"> 
              <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600">{{mode=='signin' ? 'Log in': 'Sign up'}}</button>
              <a href="signup" class="ml-6 text-blue-500" @click.prevent="toggleMode">{{mode=='signin' ? 'Sign up': 'Log in'}}</a> 
            </div>
          </div>
        
      </div>
    </div>
  </template>
  
  
  
  
  <script>
  export default {

    data(){
      return{
        mode: 'signin'
      };
    },
    methods: {
      toggleMode(){
        this.mode = this.mode === 'signin' ? 'signup': 'signin';
      },
      handleSignin() {
        // Handle form submission here (e.g., send login request)
        console.log('Username:', this.username);
        console.log('Password:', this.password);
      },
      handleSignup() {
        // Handle form submission here (e.g., send login request)
        console.log('Username:', this.username);
        console.log('Password:', this.password);
      }
    }
  };
  </script>
  
  <style>
  /* Add your custom styles here */
  </style>
  