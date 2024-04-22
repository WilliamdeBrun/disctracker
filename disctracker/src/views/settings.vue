<template>
   
   <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/6 h-1/4 bg-blue-600 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-3xl font-bold ml-2">Change Password</h2>
            <div>
                <input type="text" v-model="name" class="border rounded py-2 px-11 ml-2 mt-3 mr-2" placeholder="Enter old password" required>
                <input type="text" v-model="name" class="border rounded py-2 px-11 ml-2 mt-1 mr-2" placeholder="Enter new password" required>
                <input type="text" v-model="name" class="border rounded py-2 px-11 ml-2 mt-1 mr-2" placeholder="Repear new password" required>
                <button @click="changePw()" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-1 px-4 border border-gray-400 rounded shadow text-sm ml-2 mt-1">Change Password</button>
            </div>
        </div>
        <div class="w-1/6 h-1/6 bg-blue-600 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-3xl font-bold ml-2">Change Avatar</h2>
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
 const changePw = () => {
    alert("pw changed");
 };
 
</script>

<style>
/* Add your custom styles here */
</style>
  