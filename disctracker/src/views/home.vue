<template>
    <div class="flex flex-col relative justify-top items-center w-full h-full mt-44">
        <div class="lg:w-8/12 w-11/12 lg:mx-2 mt-2 h-1/6 mb-10">
            <div class="relative bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full flex justify-center items-center">
                <p class="text-white text-md md:text-xl lg:text-3xl font-bold">Welcome back {{ username }}!</p>
                
            </div>
        </div>
        <div class="relative lg:w-8/12 w-11/12 lg:mx-2 mb-2 h-1/3">
            <div class="flex flex-col bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full justify-center items-center hover:bg-slate-800 hover:bg-opacity-90"
                        @click="$emit('myEvent')">
                <p class="text-white text-md md:text-xl lg:text-3xl font-bold">Start new game</p>
            </div>
        </div>
    </div>
</template>
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  // Define reactive variables
  const username = ref('');
  const dynamicHeight = ref('300'); // Initial height value
  // Define methods
  
    onMounted(async () => {
        getUser();
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
    const getUser = () => {
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
            throw new Error('Failed to get user');
        }
    })
    .then(data => {
        console.log(data);
        if(data.username){
            username.value = data.username;
            
        }
    })
    .catch(error => {
        console.error('Error finding user:', error.message);
        
    });
    
    
}; 
</script>

<style>
/* Add your custom styles here */
</style>
  