<template>
    <div class="flex flex-wrap relative justify-center items-top w-full">
        <div class="lg:w-8/12 w-11/12 lg:mx-2 my-2 h-96">
            <div class="relative bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full">
                <p class="text-white">Welcome back {{ username }}</p>
                <div class="w-1/2 h-80 absolute right-5 bg-slate-700 rounded-lg">
                    <div :style="{ height: `${dynamicHeight-60}px` }" class="flex flex-col rounded-lg absolute bottom-2 right-[11%] bg-slate-500 justify-center w-[13%] ">
                        <p class="text-white self-center">129</p>
                     </div>
                    <div :style="{ height: `${dynamicHeight-30}px`}" class="flex flex-col rounded-lg absolute bottom-2 right-[29%] bg-slate-500 justify-center w-[13%]">
                        <p class="text-white self-center">100</p>
                    </div>
                    <div :style="{ height: `${dynamicHeight}px`}" class="flex flex-col rounded-lg absolute bottom-2 right-[47%] bg-slate-500 justify-center w-[13%]">
                        <p class="text-white self-center">82</p>
                    </div>
                    <div :style="{ height: `${dynamicHeight-60}px` }" class="flex flex-col rounded-lg absolute bottom-2 right-[65%] bg-slate-500 justify-center w-[13%]">
                        <p class="text-white self-center">71</p>
                     </div>
                    <div :style="{ height: `${dynamicHeight-30}px`}" class="flex flex-col rounded-lg absolute bottom-2 right-[82%] bg-slate-500 justify-center w-[13%]">
                        <p class="text-white self-center">24</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="relative justify-center lg:w-8/12 w-11/12 lg:mx-2 my-2 h-60">
            <div class="flex flex-col bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full justify-center items-center hover:bg-slate-800 hover:bg-opacity-90"
                        @click="$emit('myEvent')">
                <p class="text-white">Start new game</p>
            </div>
        </div>
        <div class="relative justify-center lg:w-8/12 w-11/12 lg:mx-2 my-2 h-60">
            <div class="flex flex-col bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full justify-center items-center hover:bg-slate-800 hover:bg-opacity-90"
                        @click="$emit('myEvent')">
                <p class="text-white text-center">Start new tournament</p>
            </div>
        </div>
       
    </div>
    
</template>
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  // Define reactive variables
  const username = ref('user1');
  const dynamicHeight = ref('300'); // Initial height value
  // Define methods
  
    onMounted(async () => {
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
 
</script>

<style>
/* Add your custom styles here */
</style>
  