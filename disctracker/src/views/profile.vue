<template>
    <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/6 h-1/6 bg-blue-600 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-3xl font-bold">Your previous round</h2>
        </div>
        <div class="w-1/6 h-1/6 bg-blue-600 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-3xl font-bold">Your best round</h2>
        </div>
        <div class="w-1/6 h-1/3 bg-blue-600 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-3xl font-bold">Your averages</h2>
        </div>
           
    </div>   

</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  // Define reactive variables
  const username = ref('');

  // Define methods
 
    

  onMounted(async () => {
  
 });
 
</script>

<style>
/* Add your custom styles here */
</style>
  