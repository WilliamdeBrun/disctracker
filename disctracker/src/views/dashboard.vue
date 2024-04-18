<template>
   
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<div class="bg-blue-500 flex h-screen">
  <div class="sidebar bg-blue-900 w-40">
    <div class="p-2">
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 flex items-center" @click="updateDashboard('Home')">
        <i class="fa fa-home text-white mr-2"></i>
        <p class="text-white">Home</p>
      </div>
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Profile')">
        <i class="fa fa-user text-white mr-2"></i>
        <p class="text-white">Profile</p>
      </div>
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Leaderboard')">
        <i class="fa fa-line-chart text-white mr-2"></i>
        <p class="text-white">Leaderboard</p>
      </div> 
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Tournament')">
        <i class="fa fa-trophy text-white mr-2"></i>
        <p class="text-white">Tournament</p>
      </div> 
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Courses')">
        <i class="fa fa-flag text-white mr-2"></i>
        <p class="text-white">Courses</p>
      </div>
      <div class="hover:bg-blue-800 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Settings')">
        <i class="fa fa-cog text-white mr-2"></i>
        <p class="text-white">Settings</p>
      </div>
    </div>
  </div> 
  <div class="flex-1 flex flex-col justify-top items-center">
    <h1 class="text-5xl text-white font-bold">{{ dbHeader }}</h1>
    <div class="flex justify-center items-start w-full h-full">
      <home v-if="dbHeader === 'Home'"/>
      <profile v-else-if="dbHeader === 'Profile'"/>
      <leaderboard v-else-if="dbHeader === 'Leaderboard'"/>
      <tournament v-else-if="dbHeader === 'Tournament'"/>
      <courses v-else-if="dbHeader === 'Courses'" />
      <settings v-else-if="dbHeader === 'Settings'"/>
    </div>
  </div>


  
</div>

</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'
  import home from './home.vue'
  import courses from './courses.vue'
  import leaderboard from './leaderboard.vue'
  import profile from './profile.vue'
  import settings from './settings.vue'
  import tournament from './tournament.vue'


  // Define reactive variables
  const username = ref('');

  // Define methods
  const toggleMode = () => {

  };

  const handleSignin = () => {
  
  };

  const handleSignup = () => {
    
  };
  onMounted(async () => {
  
 });
 const dbHeader = ref('Home');
 const updateDashboard = (text) => {
    dbHeader.value = text; 
  
 }
</script>

<style>
/* Add your custom styles here */
</style>
  