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
            <div class="mb-4">
            <label for="realname" class="block text-gray-700 font-bold mb-2">Name (first & last)</label>
            <input type="text" v-model="real" id="realname" name="realname" class="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-blue-500" required>
          </div>
          <div class="mb-4"></div>
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
              <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600" @click="mode === 'signin' ? handleSignin() : handleSignup()">{{mode=='signin' ? 'Log in': 'Sign up'}}</button>
              <a href="signup" class="ml-6 text-blue-500" @click.prevent="toggleMode">{{mode=='signin' ? 'Sign up': 'Log in'}}</a> 
            </div>
          </div>
      </div>
    </div>
    <button type="submit" class=""> <router-link to="/dashboard"> LINK</router-link></button>
    <div>{{backendString}}</div>
  </template>
  
  
  
  
  <script setup>
  import { ref, onMounted, inject} from 'vue'
  import { useRouter } from 'vue-router';

  // Define reactive variables
  const username = ref('');
  const realname = ref('');
  const email = ref('');
  const password = ref('');
  const repeatpsw = ref('');
  const gender = ref('');
  const mode = ref('signin');
  const backendString = ref('standard');

  // Define methods
  const toggleMode = () => {
    mode.value = mode.value === 'signin' ? 'signup' : 'signin';
  };
  const handleSignup = () => {
    // Handle form submission here (e.g., send login request)
    console.log('Username:', username.value);
    console.log('Password:', password.value);
    console.log('Realname:', realname.value);
    console.log('Email:', email.value);
    console.log('Gender', gender.value);


    
    if (password.value !== repeatpsw.value) {
      console.log("Passwords didn't match");
    } else {
      console.log('Username:', username.value);
      console.log('Password:', password.value);
    }
    const formData = {
    username: username.value,
    realname: realname.value,
    passwd: password.value,   
    email: email.value,
    gender: gender.value
    };
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
            
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            // Handle successful response from the backend
            console.log('Signup successful');
            handleSignin();
            return response.json();
            // Redirect to dashboard or perform other actions as needed
            // try this -> router.push('/dashboard');
            // window.location.href = '/dashboard'; // Redirect to dashboard
        } else {
            throw new Error('Failed to sign up');
        }
    })
    .then(data => {
        // Check if login was successful and access token is provided
        if (data) {
            // Save the access token to local storage for future use
            console.log(data.access_token);
            localStorage.setItem('access_token', data.access_token);
        } else {
            throw new Error('Access token not provided');
        }
    })
    .catch(error => {
        console.error('Failed to sign up:', error.message);
    });
  };



  const handleSignin = () => {
    // Handle form submission here (e.g., send login request)
    console.log('Username:', username.value);
    console.log('Password:', password.value);
    const formData = {
    username: username.value,
    password: password.value
    };
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            // Handle successful response from the backend
            console.log('Login successful');
            return response.json();
            // Redirect to dashboard or perform other actions as needed
            // try this -> router.push('/dashboard');
            // window.location.href = '/dashboard'; // Redirect to dashboard
        } else {
            throw new Error('Failed to sign in');
        }
    })
    .then(data => {
        // Check if login was successful and access token is provided
        if (data) {
            // Save the access token to local storage for future use
            console.log(data.access_token);
            localStorage.setItem('access_token', data.access_token);
            window.location.href = '/dashboard'; // Redirect to dashboard
        } else {
            throw new Error('Access token not provided');
        }
    })
    .catch(error => {
        console.error('Failed to sign in:', error.message);
    });
  };
  onMounted(async () => {
 });
</script>

  
  <style>
  /* Add your custom styles here */
  </style>
  