<template>
    <div class="min-h-screen flex flex-col items-center justify-center bg-blue-500">
      <h1 class="text-5xl font-bold text-white mb-8">
        Disctracker
      </h1>  
      <div class="bg-white p-8 rounded shadow-md w-80">
        <h2 class="text-xl font-bold mb-4">Login</h2>
        <form @submit.prevent="handleSubmit">
          <div class="mb-4">
            <label for="username" class="block text-gray-700 font-bold mb-2">Username</label>
            <input type="text" v-model="username" id="username" name="username" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-6">
            <label for="password" class="block text-gray-700 font-bold mb-2">Password</label>
            <input type="password" v-model="password" id="password" name="password" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="flex items-center justify-between">
            <div class="flex items-center"> 
              <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600">Login</button>
              <a href="signup" class="ml-6 text-blue-500">Sign up</a> 
            </div>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  
  
  
  <script>
  export default {
    
    methods: {
      handleSubmit() {
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
  