<template>
   
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<div :class="{ 'dark': isDarkmode }">
  <div :class="{ 'dark-mode': isDarkmode }" class="w-full flex h-screen relative">
  <div class="bg-my bg-cover bg-center blur-lg w-full h-screen absolute"></div>
  <div :class="{ 'translate-x-0': sidebarOn, '-translate-x-full': !sidebarOn }" class="sidebar w-60 h-screen bg-slate-900 absolute transition-transform z-10">
    <div class="mb-2 mt-2">
      <img src="../assets/logo.png" alt="Disctracker" class="mb-8"> 
    </div>
    <div class="p-2">
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 flex items-center" @click="updateDashboard('Home')">
        <i class="fa fa-home text-white mr-2"></i>
        <p class="text-white">Home</p>
      </div>
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Profile')">
        <i class="fa fa-user text-white mr-2"></i>
        <p class="text-white">Profile</p>
      </div>
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Leaderboard')">
        <i class="fa fa-line-chart text-white mr-2"></i>
        <p class="text-white">Leaderboard</p>
      </div> 
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Courses')">
        <i class="fa fa-flag text-white mr-2"></i>
        <p class="text-white">Courses</p>
      </div>
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="updateDashboard('Friends')">
        <i class="fa fa-users text-white mr-2"></i>
        <p class="text-white">Friends</p>
      </div>
      <div class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center" @click="signOut()">
        <i class="fa fa-sign-out text-white mr-2"></i>
        <p class="text-white">Sign out</p>
      </div>
      <div @click="toggleDarkMode" class="hover:bg-sky-400 cursor-pointer rounded-lg p-2 mt-2 flex items-center">
        <!-- Sun icon for light mode, Moon icon for dark mode -->
        <i v-if="isDarkmode" class="fa fa-sun-o mr-2 text-white"></i>
        <i v-else class="fa fa-moon-o mr-2 text-white"></i>
        <p v-if="!isDarkmode" class=" text-white">Dark Mode</p>
        <p v-else class="mr-2 text-white">Light Mode</p>
      </div>
    </div>
  </div> 
  <button @click="toggleSb" class="absolute top-0 left-0 mt-4 ml-4 text-white z-20 hover:bg-sky-400 cursor-pointer rounded-lg p-2 flex items-center justify-center">
    <i class="fa fa-bars text-white "></i>
  </button>
  <div class="flex-1 flex flex-col justify-top items-center relative">
    <h1 class="text-5xl text-white font-bold">{{ dbHeader }}</h1>
    <div class="flex justify-center items-start w-full h-full">
      <home @myEvent="updateDashboard('Courses')" v-if="dbHeader === 'Home'"/>
      <round v-if="dbHeader === 'Round'" :players="players" :typeOfRound="typeOfRound" :course="course"/>
      <profile v-else-if="dbHeader === 'Profile'"/>
      <leaderboard v-else-if="dbHeader === 'Leaderboard'"/>
      <courses @startEvent="updateDashboard('Startround', $event)"  v-else-if="dbHeader === 'Courses'" />
      <startround @playEvent="updateDashboard('Round', '', $event)" @send="setTypeOfRound($event)":course="course" v-else-if="dbHeader === 'Startround'"/>
      <friends v-else-if="dbHeader === 'Friends'"/>
    </div>
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
  import startround from './startround.vue'
  import round from './round.vue'
  import friends from './friends.vue'

  const sidebarOn = ref('false');

  
  // Define reactive variables
  const typeOfRound = ref('');
  const username = ref('');
  const isDarkmode = ref(localStorage.getItem('darkModeState') === 'true');
  const setTypeOfRound = (type) => {
    console.log("dashboard",type);
    typeOfRound.value = type;
    console.log("dashboard",typeOfRound.value);
  };
  // Define methods
  onMounted(async () => {
    console.log(typeOfRound.value);
    fetch('http://localhost:5000/dashboard', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
    }
    })
    .then(response => {
        if (response.ok) {
          // Token is valid, allow access to the dashboard
          // Render the dashboard component or navigate to the dashboard route
        } else {
          // Token is invalid or missing, redirect to the login page
          window.location.href = '/';
        }
    })
    .catch(error => {
        console.error('Failed to check token:', error);
    });
  });
  const dbHeader = ref('Home');
  const course = ref('');
  const players = ref(['', '', '', '']);

  const updateDashboard = (text, courseName, player, typeOfRound) => {
    console.log("here",typeOfRound);
    dbHeader.value = text;
    if (courseName != ''){
      course.value = courseName;
    } 
    players.value = player;
    toggleSb1(); 
  };
  const toggleSb = () => {
    console.log(sidebarOn.value);
    sidebarOn.value = !sidebarOn.value;
  };
  const toggleSb1 = () => {
    if(sidebarOn.value){
      console.log(sidebarOn.value);
      sidebarOn.value = !sidebarOn.value;
    }
  };  

  const signOut = () => {
    localStorage.removeItem('access_token');
    location.reload();
  };
  const toggleDarkMode = () => {
    isDarkmode.value = !isDarkmode.value;
    localStorage.setItem('darkModeState', isDarkmode.value);
    toggleSb();
  };

</script>

<style>
/* Add your custom styles here */
.dark-mode{
  filter: brightness(0.5);
}
</style>
  