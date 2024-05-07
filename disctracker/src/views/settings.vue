<template>
   
   <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/6 h-1/4 bg-slate-900 rounded-lg mt-20 mr-10">
            <h2 class="text-white text-md md:text-md lg:text-3xl font-bold ml-3">Change Password</h2>
            <div>
                <input type="text" v-model="name" class="border rounded py-2 ml-2 mt-3 mr-2 w-2/3 h-1/4 text-center" placeholder="Enter old password" required>
                <input type="text" v-model="name" class="border rounded py-2 ml-2 mt-1 mr-2 w-2/3 h-1/4 text-center" placeholder="Enter new password" required>
                <input type="text" v-model="name" class="border rounded py-2 ml-2 mt-1 mr-2 w-2/3 h-1/4 text-center" placeholder="Repeat new password" required>
                <button @click="changePw()" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-1 px-4 border border-gray-400 rounded shadow text-sm ml-2 mt-1">Change Password</button>
            </div>
        </div>
           
    </div>
</template>
  
  
  
  
  <script setup>
  //this file is unused
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
  