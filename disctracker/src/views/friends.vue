<template>
   
    <div class="flex flex-col justify-top items-center h-full w-full">
         <div class="w-1/2 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col items-center">
             <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold ml-2">Find new friend</h2>
             <div>
                <input v-model="playername" type="text" class="mt-5 ml-2 p-2 border border-gray-300 rounded-lg" placeholder="Search for a player">
                <button @click.prevent="addFriend" class="ml-2 p-2 bg-blue-500 text-white rounded-lg">
                    Add Friend
                    <span v-if="friendStatus === 'success'" class="text-green-500 ml-2">&#10004;</span>
                    <span v-else-if="friendStatus === 'error'" class="text-red-500 ml-2">&#10008;</span>
                </button>
             </div>
             
             
         </div>
     </div>
 </template>
   
   
   
   
   <script setup>
   import { ref, onMounted} from 'vue'
   const playername = ref('');
   const friendStatus = ref('');
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
            return response.json();
        } else if (response.status === 409) {
            throw new Error('User not found or already added as friend');
        } else {
            throw new Error('Failed to add friend');
        }
    })
    .then(data => {
        console.log(data.message); // Log the response message from the server
    })
    .catch(error => {
        console.error('Error adding friend:', error.message);
        friendStatus.value = 'error';
    });
};
 
   onMounted(async () => {
   
  });
  
  
 </script>
 
 <style>
 /* Add your custom styles here */
 </style>
   