<template>
    <div class="flex justify-center items-top h-full w-full mt-20">
      <div class="flex justify-center items-end w-1/3 h-1/3">
        <!-- Second place div -->
        <div class="h-3/5 w-1/3 bg-blue-600 relative mt-10 rounded-lg flex justify-center">
          <h2 class="text-white text-4xl font-bold">2</h2>
        </div>
        <!-- First place div -->
        <div class="h-3/4 w-1/3 bg-blue-600 relative rounded-lg flex justify-center">
          <h2 class="text-white text-4xl font-bold">1</h2>
        </div>
      
      <!-- Third place div -->
        <div class="h-1/2 bg-blue-600 relative mt-20 w-1/3 rounded-lg flex justify-center">
            <h2 class="text-white text-4xl font-bold">3</h2>
        </div>
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
  