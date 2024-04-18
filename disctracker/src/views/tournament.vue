<template>
    <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/6 h-1/6 bg-blue-900 rounded-lg mt-20">
            <form @submit.prevent="draft">
                <input type="text" v-model="name" class="border rounded px-4 py-2" placeholder="Enter player name" required>
                <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Add Player</button>
                <button type="button" @click="startTournament" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">Start Tournament</button>
            </form>
            
        </div>

           
    </div>
</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  // Define reactive variables
  const username = ref('');
    
  // Define methods
  const toggleMode = () => {

  };

  const handleSignin = () => {
  
  };

  const handleSignup = () => {
    
  };
  onMounted(async () => {
  
 });


</script>

<style>
/* Add your custom styles here */
</style>
  