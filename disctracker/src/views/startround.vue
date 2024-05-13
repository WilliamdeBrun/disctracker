<template>
   
    <div class="flex flex-col justify-top items-center h-full w-full">
         <div class="w-1/2 h-1/2 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
            <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Start new round at {{ course }} </h2>
            <form class="mt-4" @submit.prevent="startRound">
                <div class="mb-2 mt-2">
                    <select id="coursePath" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="coursePath">
                        <option numOfFriends="" disabled selected>Select Path</option>
                        <option numOfFriends="F9">Front 9</option>
                        <option numOfFriends="B9">Back 9</option>
                        <option numOfFriends="Full18">Full 18</option>
                    </select>
                </div>
                <div v-for="index in numOfFriends" :key="index" class="mb-2">
                    <input type="text" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="players[index - 1]" :placeholder="'Player ' + index + ' name'">
                    <ul>
                        <li v-for="(friend, index) in friends" :key="index" class="text-white text-md md:text-md lg:text-xl font-bold">{{ friend }}</li>
                    </ul>
                </div>
                <button @click="addNumofPlayers()" type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Add friend
                </button>
                
            </form>   
            <button @click="$emit('playEvent', players)" type="submit" class=" mt-5 bg-green-300 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Start round
            </button>
         </div>
     </div>
 </template>
   
   
   
   
   <script setup>
   import { ref, onMounted} from 'vue'
   
   // Define reactive variables
   const numOfFriends = ref(0); 
   const addNumofPlayers = () => {
    if (numOfFriends.value < 4){
        numOfFriends.value = numOfFriends.value+1;
    }
    
   }
   const players = ref(['', '', '', '']);
   const coursePath = ref('');
   const friends = ref([]);
   const props = defineProps({
    course: String,
   });

  
  onMounted(async () => {
    fetch('http://127.0.0.1:5000/getfriends', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }else{
            throw new error('Failed to get friends');
        }
    })
    .then(data => {
        if(data.friends){
            friends.value = data.friends;
        }
    })
    .catch(error => {
        console.error('Error adding friends:', error.message);
        
    });

  });
  
  
  
 </script>
 
 <style>
 /* Add your custom styles here */
 </style>
   