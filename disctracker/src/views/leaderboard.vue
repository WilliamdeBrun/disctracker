<template>
    <div class="flex flex-col justify-top items-center h-full w-full">
      <div class="w-1/2 h-1/3 bg-slate-900 bg-opacity-90 rounded-lg mt-20 flex flex-col jusify-top items-center">
        <h2 class="text-white text-md md:text-xl lg:text-3xl font-bold">Top Players</h2>    
        <div class="flex items-start justify-top">      
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 3</h2> 
              <tbody>
                <tr v-for="(player, index) in topPar3" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 4</h2> 
              <tbody>
                <tr v-for="(player, index) in topPar4" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Par 5</h2> 
              <tbody>
                <tr v-for="(player, index) in topPar5" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">All Pars</h2> 
              <tbody>
                <tr v-for="(player, index) in topPar" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
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
                <tr v-for="(player, index) in topRydF9" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Ryd B9</h2> 
              <tbody>
                <tr v-for="(player, index) in topRydB9" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Ryd 18</h2> 
              <tbody>
                <tr v-for="(player, index) in topRyd18" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren F9</h2> 
              <tbody>
                <tr v-for="(player, index) in topHammarenF9" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top mr-10">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren B9</h2> 
              <tbody>
                <tr v-for="(player, index) in topHammarenB9" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
                </tr>
              </tbody>
            </table>
            <table class="text-white text-md md:text-md lg:text-xl font-bold mt-5 flex flex-col items-center justify-top">
              <h2 class="text-white text-md md:text-md lg:text-xl font-bold mb-3">Hammaren 18</h2> 
              <tbody>
                <tr v-for="(player, index) in topHammaren18" :key="index">
                  <td class="border-r border-white pr-2">{{ Object.keys(player)[0] }}</td>
                  <td :class="avgColor(player[Object.keys(player)[0]]) + ' pl-4'"> {{ addPlus(player[Object.keys(player)[0]]) }} </td>
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
  getScores();
 });

 const topPar = ref([]);
 const topPar3 = ref([]);
 const topPar4 = ref([]);
 const topPar5 = ref([]);
 const topRydF9 = ref([]);

 const topRydB9 = ref([]);

 const topRyd18 = ref([]);

 const topHammarenF9 = ref([]);

 const topHammarenB9 = ref([]);

 const topHammaren18 = ref([]);

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
  const getScores = () => {
    fetch('http://127.0.0.1:5000/getscores', {
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
            throw new error('Failed to get friends');
        }
    })
    .then(data => {
        console.log(data);
        if(data){
            const {best_ham_f9, best_ham_18, best_ham_b9, best_ryd_f9, best_ryd_18, best_ryd_b9, par3, par4, par5, allpar } = data;
            console.log(topPar);
            topHammarenB9.value = best_ham_b9;
            topHammarenF9.value = best_ham_f9;
            topHammaren18.value = best_ham_18;
            topRydF9.value = best_ryd_f9;
            topRydB9.value = best_ryd_b9;
            topRyd18.value = best_ryd_18;
            topPar.value = allpar;
            topPar3.value = par3;
            topPar4.value = par4;
            topPar5.value = par5;
            
            console.log(topPar);
        }
    })
    .catch(error => {
        console.error('Error adding friends:', error.message);
        
    });
};
</script>

<style>
/* Add your custom styles here */
</style>
  