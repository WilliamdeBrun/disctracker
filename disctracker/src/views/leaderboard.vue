<template>
    <div class="flex flex-col justify-top items-center h-full w-full">
      <div class="w-1/2 h-1/3 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
        <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Top Players</h2>    
        <div class="flex items-start justify-top">      
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 3</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topPlayers, 'avg3')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.avg3) + ' pl-4'"> {{ addPlus(player.avg3) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 4</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topPlayers, 'avg4')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.avg4) + ' pl-4'"> {{ addPlus(player.avg4) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 5</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topPlayers, 'avg5')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.avg5) + ' pl-4'"> {{ addPlus(player.avg5) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">All Pars</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topPlayers, 'avg')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.avg) + ' pl-4'"> {{ addPlus(player.avg) }} </td>
                </tr>
              </tbody>
            </table>
        </div> 
            
            
      </div>
      <div class="w-2/3 h-1/3 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
            <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Top Rounds</h2> 
            <div class="flex items-start justify-top">      
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Ryd F9</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topRydF9, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Ryd B9</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topRydB9, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Ryd 18</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topRyd18, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren F9</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topHammarenF9, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren B9</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topHammarenB9, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren 18</h2> 
              <tbody>
                <tr v-for="(player, index) in sortTables(topHammaren18, 'score')" :key="index">
                  <td class="border-r border-white pr-2">{{ player.name }}</td>
                  <td :class="avgColor(player.score) + ' pl-4'"> {{ addPlus(player.score) }} </td>
                </tr>
              </tbody>
            </table>
        </div>       
      </div>
    </div>
  </template>
  
  
  


  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  onMounted(async () => {
  
 });

 const topPlayers = ref([
  { name: 'Pedro', avg3: -0.21, avg4: -0.35, avg5: 0.11, avg: -0.22},
  { name: 'Alfonso', avg3: -0.13, avg4: -0.05, avg5: -0.11, avg: -0.22},
  { name: 'Pablo', avg3: 0.00, avg4: 0.35, avg5: 0.00, avg: 0.22},
  { name: 'Juan', avg3: 0.12, avg4: 0.34, avg5: 0.14, avg: 0.00},
  { name: 'Carlos', avg3: 0.27, avg4: 0.35, avg5: 0.22, avg: -0.22}
 ]);
 const topRydF9 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: 1},
  { name: 'Carlos', score: 4}
 ]);

 const topRydB9 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: 1},
  { name: 'Carlos', score: 4}
 ]);

 const topRyd18 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: 1},
  { name: 'Carlos', score: 4}
 ]);

 const topHammarenF9 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: 1},
  { name: 'Carlos', score: 4}
 ]);

 const topHammarenB9 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: 1},
  { name: 'Carlos', score: 4}
 ]);

 const topHammaren18 = ref([
  { name: 'Pedro', score: -2},
  { name: 'Alfonso', score: -1},
  { name: 'Pablo', score: 0},
  { name: 'Juan', score: -11},
  { name: 'Carlos', score: 4}
 ]);

 const avgColor = (avg) => {
  if (avg < 0){
    return 'text-green-400';
  } else if (avg > 0){
    return 'text-red-400'
  } else{
    return 'text-white';
  }
 };

 const addPlus = (avg) => {
  if (avg >= 0){
    return '+' + avg;
  } else{
    return avg;
  }
 };

 const sortTables = (table, key) => {
  return table.slice().sort((a,b) => {
    return a[key] - b[key];
  });

  };
</script>

<style>
/* Add your custom styles here */
</style>
  