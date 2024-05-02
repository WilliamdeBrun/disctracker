<template>
   
    <div class="flex flex-col justify-top items-center h-full w-full">
         <div class="w-1/2 h-1/2 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
            <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Start new round at {{ course }} </h2>
            <form class="mt-4" @submit.prevent="startRound">
                <div class="mb-2 mt-2">
                    <select id="coursePath" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="coursePath">
                        <option value="" disabled selected>Select Path</option>
                        <option value="F9">Front 9</option>
                        <option value="B9">Back 9</option>
                        <option value="Full18">Full 18</option>
                    </select>
                </div>
                <div v-for="index in 4" :key="index" class="mb-2">
                    <input type="text" class="border border-gray-300 rounded px-4 py-2 w-64" v-model="players[index - 1]" :placeholder="'Player ' + index + ' name'">
                </div>
                <button @click="$emit('playEvent')" type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Start Round
                </button>
            </form>   
             
         </div>
            
     </div>
 </template>
   
   
   
   
   <script setup>
   import { ref, onMounted} from 'vue'
   
   // Define reactive variables
   const props = defineProps({
    course: String,
   });
   const players = ref(['', '', '', '']);
   const coursePath = ref('');
  
  onMounted(async () => {
  });
  
  
  
 </script>
 
 <style>
 /* Add your custom styles here */
 </style>
   