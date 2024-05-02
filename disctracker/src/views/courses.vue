<template>
   
   <div class="flex flex-col justify-top items-center h-full w-full">
        <div class="w-1/2 h-1/4 bg-sky-300 bg-opacity-50 rounded-lg mt-20">
            <h2 class="text-white text-3xl font-bold ml-2">Rydskogen DGC</h2>
            <div class="grid grid-cols-9 mt-4 mr-2 ml-2">
                <template v-for="num in 9" :key="`box-${num}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9  mr-2 ml-2">
                <template v-for="(num, index) in rydsParFront" :key="`box-${num}`">
                    <div class="box bg-blue-200 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
      
            <div class="grid grid-cols-9 mt-4  mr-2 ml-2">
                <template v-for="num in 9" :key="`box-${num + 9}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num + 9 }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9 mb-2  mr-2 ml-2">
                <template v-for="(num, index) in rydsParBack" :key="`box-${num }`">
                    <div class="box bg-blue-200 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
            <div>
                <button @click="$emit('myEvent')" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow text-sm ml-2">Start new round</button>
                
            </div>
            
        </div>
        <div class="w-1/2 h-1/4 bg-sky-300 bg-opacity-50 rounded-lg mt-20">
            <h2 class="text-white text-3xl font-bold ml-2">Hammaren DiscGolfPark</h2>
            <div class="grid grid-cols-9 mt-4 mr-2 ml-2">
                <template v-for="num in 9" :key="`box-${num}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9  mr-2 ml-2">
                <template v-for="(num, index) in hammarenParFront" :key="`box-${num}`">
                    <div class="box bg-blue-200 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
      
            <div class="grid grid-cols-9 mt-4  mr-2 ml-2">
                <template v-for="num in 9" :key="`box-${num + 9}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num + 9 }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9 mb-2  mr-2 ml-2">
                <template v-for="(num, index) in hammarenParBack" :key="`box-${num }`">
                    <div class="box bg-blue-200 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
            <div>
                <button  @click="$emit('myEvent')" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow text-sm ml-2">Start new round</button>
            </div>
        </div>
    </div>
</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  // Define reactive variables
  const username = ref('');

  const rydsParFront = [3, 4, 4, 3, 3, 3, 3, 5, 3];
  const rydsParBack = [3, 4, 3, 5, 3, 3, 3, 4, 3];
  const hammarenParFront = [3, 3, 3, 3, 3, 3, 3, 3, 4];
  const hammarenParBack = [3, 4, 3, 4, 3, 3, 3, 3, 3];
  // Define methods

  onMounted(async () => {
  
 });
 const startRound = () => {
    alert("lets roll!");
 };
 
 
</script>

<style>
/* Add your custom styles here */
</style>
  