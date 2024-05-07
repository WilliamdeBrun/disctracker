<template>
   
    <div class="flex flex-col justify-top items-center h-full w-full">
         <div class="w-1/2 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col items-center">
             <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold ml-2">Find new friend</h2>
             <div>
                <input v-model="playername" type="text" class="mt-5 ml-2 p-2 border border-gray-300 rounded-lg" placeholder="Search for a player">
                <button @click.prevent="addFriend" class="ml-2 p-2 bg-blue-500 text-white rounded-lg">
                    Add Friend
                </button>
                <p v-if="friendStatus === 'success'" class="text-green-500 mt-2 ml-2">Friend added successfully!</p>
                <p v-else-if="friendStatus === 'nouser'" class="text-red-500 mt-2 ml-2">Invalid playername. Please try again</p>
                <p v-else-if="friendStatus === 'friends'" class="text-blue-500 mt-2 ml-2">You are already friends</p>
             </div>
             
             
         </div>
         <div :style="{ height: friends.length * 40 + 'px' }" class="w-1/4 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col items-center">
            <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold ml-2">Your friends</h2>
            <ul>
                <li v-for="(friend, index) in friends" :key="index" class="text-white text-md md:text-md lg:text-xl font-bold">{{ friend }}</li>
            </ul>
         </div>
     </div>
 </template>
   
   
   
   
   <script setup>
   import { ref, onMounted} from 'vue'
   const playername = ref('');
   const friendStatus = ref('');
   const friends = ref([]);
   const addFriend = () => {
    const data = {
        playername: playername.value

    };

    fetch('http://127.0.0.1:5000/addfriend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            // Handle successful response from the backend
            console.log('Friend added successfully');
            friendStatus.value = 'success';
            getFriends();
            return response.json();
        } else if (response.status === 409) {
            return response.json().then(json => {
                console.log(json);
                friendStatus.value = json.message === 'nouser' ? 'nouser' : 'friends';
            throw new Error('User not found or already added as friend');
            });
            
        } else {
            throw new Error('Failed to add friend');
        }
    })
    .then(data => {
        console.log(data.message); // Log the response message from the server
    })
    .catch(error => {
        console.error('Error adding friend:', error.message);
        
    });
};
const getFriends = () => {
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
};
 
   onMounted(async () => {
    getFriends();
  });
  
  
 </script>
 
 <style>
 /* Add your custom styles here */
 </style>
   