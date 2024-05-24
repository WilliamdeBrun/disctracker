<template>
   
    <div class="flex flex-col justify-top items-center h-full w-full">
         <div class="w-1/2 h-1/2 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
            <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Start new round at {{ course }} </h2>
            <form class="mt-4" @submit.prevent="startRound">
                <div class="mb-2 mt-2">
                    <select id="typeOfRound" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="selectedOption" @change="changePath()">
                        <option value="F9">Front 9</option>
                        <option value="B9">Back 9</option>
                        <option value="Full18">Full 18</option>
                    </select>
                </div>
                <div v-for="index in numOfFriends" :key="index" class="mb-2">
                    <input type="text" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="players[index - 1]" :placeholder="'Player ' + index + ' name'" @input="selectSuggestion(players[index-1])" @click="swithIndex(index-1)">
                    <ul class=" bg-slate-500 rounded-b-lg bg-opacity-30">
                        <li v-if="(numOfFriends === newindex ? index === numOfFriends+1 : index === newindex+1)" v-for="(friend, index1) in filteredFriends" :key="index1" @click="selected(friend), selectSuggestion(players[index-1])" class="text-white text-md md:text-md lg:text-xl font-bold text-center">{{ friend }}</li>
                    </ul>
                </div>
                <button @click="addNumofPlayers()" type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Add player
                </button>
                <button @click="$emit('playEvent', players), $emit('send', typeOfRound)" type="submit" class=" ml-6 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Start round
            </button>
            </form>   
           
         </div>
         
     </div>
 </template>
 
   <script setup>
   import { ref, onMounted} from 'vue'

   // Define reactive variables
   const selectedOption = ref('Full18');
   const numOfFriends = ref(0); 
   const newindex = ref(0);
   const players = ref([]);
   const typeOfRound = ref('');
   const friends = ref([]);
   const filteredFriends = ref([]);
   const props = defineProps({
    course: String,
   });
   const changePath = () => {
    typeOfRound.value = selectedOption.value;
    console.log(typeOfRound.value);
   }
   const addNumofPlayers = () => {
    if (numOfFriends.value < 4){
        numOfFriends.value = numOfFriends.value+1;
    }
   }

   const swithIndex = (index) => {
    newindex.value = index;
   }

   const selected = (friend) => {
    
    if (newindex.value != numOfFriends.value){
        players.value.splice(newindex.value, 1, friend);
    }
    else{
        players.value.splice(numOfFriends.value-1, 1,friend);
    }
       
   }

   const selectSuggestion = (suggestion) => {
    
    const filtered = friends.value.filter(friend => {
        return friend.toLowerCase().includes(suggestion.toLowerCase());
    });
  
    filteredFriends.value = filtered;
    if(filteredFriends.value.length === 1){
        filteredFriends.value = [];
    } 

   };
  
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

    fetch('http://127.0.0.1:5000/getuser', {
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
            throw new error('Failed to get user');
        }
    })
    .then(data => {
        if(data){
            const {uid, username, realname, email} = data;
            players.value.push(username);
            numOfFriends.value = numOfFriends.value + 1;
        }
    })
    .catch(error => {
        console.error('Error adding user:', error.message);
        
    });

  });
  
  
  
 </script>
 
 <style>
 /* Add your custom styles here */
 </style>
   