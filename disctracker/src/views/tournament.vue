<template>
    <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/2 h-1/3 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex items-start">
            <div class="flex flex-col items-start">
                <input id="newPlayer" type="text" v-model="name" class="border rounded py-2 px-12 mt-1 ml-1" placeholder="Enter player name" required>
                <div class="flex flex-col sm:flex-row">
                    <button type="button" @click="addPlayer" class="bg-zinc-50 hover:bg-zinc-500 text-black font-bold py-2 px-4 rounded ml-1 mt-1">Add Player</button>
                    <button type="button" @click="startTournament" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-3 rounded ml-1 mt-1">Start Tournament</button>
                </div>
            </div>
            <div id="players" class="ml-20">

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
 const startTournament = () => {
    alert("start");
 };
 const addPlayer = () => {
    var players = document.getElementById("players");
    var newP = document.createElement("p");
    var p = document.getElementById("newPlayer");
    newP.textContent = p.value;
    players.appendChild(newP);

 };


</script>

<style>
/* Add your custom styles here */
</style>
  