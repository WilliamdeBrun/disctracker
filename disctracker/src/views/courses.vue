<template>
   
   <div class="flex justify-center items-top h-full w-full">
        <div class="w-1/2 h-1/6 bg-blue-900 rounded-lg mt-20">
            <h2 class="text-white text-3xl font-bold">Rydskogen Discgolf</h2>
            <div class="grid grid-cols-9 mt-4">
                <template v-for="num in 9" :key="`box-${num}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9">
                <template v-for="(num, index) in rydsParFront" :key="`box-${num}`">
                    <div class="box bg-white text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
            </div>
      
            <div class="grid grid-cols-9 mt-4">
                <template v-for="num in 9" :key="`box-${num + 9}`">
                    <div class="box bg-green-500 text-black flex justify-center items-center rounded border border-black w-full">{{ num + 9 }}</div>
                </template>
            </div>
            <div class="grid grid-cols-9">
                <template v-for="(num, index) in rydsParBack" :key="`box-${num }`">
                    <div class="box bg-white text-black flex justify-center items-center rounded border border-black w-full">{{ num }}</div>
                </template>
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
  