<template>
   
   <div class="flex flex-col justify-top items-center h-full w-full">
        <div class="w-1/2 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-20">
            <div class="flex items-start justify-between">
                <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold ml-2">Rydskogen DGC</h2>
                <h2 v-if="dists.ryd !== null" class="mr-2 text-white text-md md:text-xl lg:text-3xl font-bold ml-2">
                    Distance to course: {{ dists.ryd }} km
                </h2>
            </div>
            <div class="grid grid-cols-9 mt-2 mr-2 ml-2">
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
                <button @click="$emit('startEvent', 'Rydskogens DGC')" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow text-xs md:text-xs lg:text-sm ml-2">Start Round</button>
                
                
            </div>
            
        </div>
        <div class="w-1/2 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-20">
            <div class="flex items-start justify-between">
                <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold ml-2">Hammaren DiscGolfPark</h2>
                <h2 v-if="dists.ham !== null" class="mr-2 text-white text-md md:text-xl lg:text-3xl font-bold ml-2">
                Distance to course: {{ dists.ham }} km
                </h2>
            </div>
            <div class="grid grid-cols-9 mt-2 mr-2 ml-2">
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
                <button @click="$emit('startEvent', 'Hammarens DiscGolfPark')" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow text-xs md:text-xs lg:text-sm ml-2">Start Round</button>
                
                
            </div>
        </div>
    </div>
</template>
  
  
  
  
  <script setup>
  import { ref, onMounted, computed, watch} from 'vue'
  import { useGeolocation } from '@vueuse/core'

  // Define reactive variables

  const rydsParFront = ref([]);
  const rydsParBack = ref([]);
  const hammarenParFront = ref([]);
  const hammarenParBack = ref([]);
  const rydLat = 58.4135263264688;
  const rydLong = 15.584701134102012;
  const hamLat = 59.268886408012854;
  const hamLong = 17.218092838401137;
  const dists = ref({ryd: null, ham: null});
  const {coords} = useGeolocation();
  // Define methods
  const getDistance = (lat, long, userLat, userLong) => {
    //function to calculate the birds path between user and course using Haversine formula, "fågelvägen"
    const R = 6371; //the radius of the earth(km)
    const dLat = degToRad(userLat-lat);
    const dLong = degToRad(userLong-long);
    const a1 = Math.sin(dLat/2) ** 2;
    const a2 = Math.cos(degToRad(lat)) * Math.cos(degToRad(userLat));
    const a3 = Math.sin(dLong/2) ** 2;
    const a = a1 + a2 * a3;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    const dist = R * c;
    return dist.toFixed(1);
  };
  const degToRad = (val) => {
    return val * Math.PI / 180;
  };
  const getCourseDist = computed(() => {
    if(coords.value.latitude && coords.value.longitude){
        const userLat = coords.value.latitude;
        const userLong = coords.value.longitude;
        dists.value.ryd = getDistance(rydLat, rydLong, userLat, userLong);
        dists.value.ham = getDistance(hamLat, hamLong, userLat, userLong);
    }
    return dists.value;
  });
  const getCoursePars = () => {
    fetch('http://127.0.0.1:5000/coursepars', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }else{
            throw new Error('Failed to get courses');
        }
    })
    .then(data => {
        if(data){
            rydsParFront.value = data.rydf9;
            rydsParBack.value = data.rydb9;
            hammarenParBack.value = data.hamb9;
            hammarenParFront.value = data.hamf9;

            
        }
    })
    .catch(error => {
        console.error('Error finding coursepars:', error.message);
        
    });
};

onMounted(async () => {
  getCoursePars();
 });
watch(coords, () => {
    getCourseDist.value;
});
 
</script>

<style>
/* Add your custom styles here */
</style>
  