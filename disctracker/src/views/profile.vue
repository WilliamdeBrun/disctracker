<template>
    <div class="flex flex-col justify-top items-center h-full w-full">
        
        <div class="w-2/3 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-10 flex flex-col items-center">
            <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden h-1/5">Your averages</h2>
            <div class="flex w-full h-full justify-center">
                <div v-if="avgLoaded" class="h-4/5 w-1/4 mt-2 rounded-lg mr-10 flex items-top justify-center ml-10">
                    <Bar :options="avgOpt" :data="avgParData" />
                </div>
                <div v-if="avgLoaded" class="h-4/5 w-1/4 mt-2 rounded-lg mr-10 flex items-top justify-center">
                    <Bar :options="avgOpt" :data="avgHammarenData" />
                </div>
                <div v-if="avgLoaded" class="h-4/5 w-1/4 mt-2 rounded-lg flex items-top justify-center mr-10">
                    <Bar :options="avgOpt" :data="avgRydData" />
                </div>
            </div>
        </div>
        <div class="flex items-top justify-center w-2/3 h-1/4 mt-10 ">
            <div class="w-1/2 h-full bg-slate-900 bg-opacity-90 rounded-lg mr-10 flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Your previous round</h2>
                <div v-if="previousLoaded" class="h-2/3 w-4/5 mt-2 flex items-center justify-center">
                    <Bar :options="roundOpt" :data="prevData" />
                </div>
            </div>
            <div class="w-1/2 h-full bg-slate-900 bg-opacity-90 rounded-lg flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Your best round</h2>
                <div v-if="bestLoaded" class="h-2/3 w-4/5 mt-2 flex items-center justify-center">
                    <Bar :options="roundOpt" :data="bestData" />
                </div>
            </div>
        </div>
        <div class="flex items-top justify-center w-2/3 h-1/3 mt-10 ">
            
            <div class="w-1/3 h-full bg-slate-900 bg-opacity-90 rounded-lg mr-10 flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Played courses</h2>
                <div v-if="playedLoaded" class="h-3/4 w-4/5 mt-2 flex items-center justify-center">
                    <Doughnut :options="coursesOpt" :data="coursesData" />
                </div>
            </div>
            <div class="w-1/3 h-full bg-slate-900 bg-opacity-90 rounded-lg mr-10 flex flex-col items-center">
            <h2 class="text-white text-md md:text-md lg:text-3xl font-bold ml-3">Change Password</h2>
            <div class="flex flex-col items-center w-2/3">
                <input type="password" v-model="oldPw" class="border rounded py-2 ml-2 mt-5 mr-2 w-2/3 h-1/4 text-center" placeholder="Enter old password" required>
                <input type="password" v-model="newPw" class="border rounded py-2 ml-2 mt-3 mr-2 w-2/3 h-1/4 text-center" placeholder="Enter new password" required>
                <input type="password" v-model="repeatPw" class="border rounded py-2 ml-2 mt-3 mr-2 w-2/3 h-1/4 text-center" placeholder="Repeat new password" required>
                <button @click="changePw" class="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-1 px-4 border border-gray-400 rounded shadow text-sm ml-2 mt-3">Change Password</button>
                <p v-if="passwordChange === 'success'" class="text-green-500 mt-2 ml-2">{{ passwordMessage }}</p>  
                <p v-else-if="passwordChange === 'fail'" class="text-red-500 mt-2 ml-2">{{ passwordMessage }}</p> 
            </div>
        </div>
        </div>
        
           
    </div>   

</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'
  import { Bar, Doughnut } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from 'chart.js'
  import { toRaw } from 'vue';
  // Define reactive variables
  const passwordChange = ref('');
  const oldPw = ref('');
  const newPw = ref('');
  const repeatPw = ref('');
  const passwordMessage = ref('');
  const previousLoaded = ref(false);
  const bestLoaded = ref(false);
  const avgLoaded = ref(false);
  const playedLoaded = ref(false);
  
 // Ensure Chart.js plugins are registered
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);

// Define reactive variables
const changePw = () =>{
  const data = {
    old_pw: oldPw.value,
    new_pw: newPw.value,
    repeat_pw: repeatPw.value
  };
  fetch('http://127.0.0.1:5000/changepw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            passwordChange.value = 'success';
            return response.json();
        }    
         else {
          passwordChange.value = 'fail';
          return response.json().then(error=>{
            throw new Error(error.message);
          });
        }
    })
    .then(data => {
        console.log(data.message);
        passwordMessage.value = data.message;
    })
    .catch(error => {
        console.error('PW changing error:', error.message);
        passwordMessage.value = error.message;
    });

};

const avgParData = ref({
  labels: [''],
  datasets: [
    {
      label: '',
      backgroundColor: '',
      data: []
    }
  ]
});

const avgOpt = ref({
  responsive: true,
  maintainAspectRatio: false, 
  aspectRatio: 2,
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        color: 'white' 
      },
      ticks: {
        color: 'white'
      }
    },
    x: {
      grid: {
        color: 'white' 
      },
      ticks: {
        color: 'white'
      }
    }
  },
  plugins: {
    legend: {
      display: true,
      labels: {
        color: 'white' 
      }
    }
  }
});
const avgHammarenData = ref({
  labels: [''],
  datasets: [
    {
      label: '',
      backgroundColor: '',
      data: []
    }
  ]
});



const avgRydData = ref({
  labels: [''],
  datasets: [
    {
      label: '',
      backgroundColor: '',
      data: []
    }
  ]
});



const prevData = ref({
  labels: [],
  datasets: [
    {
      label: '',
      backgroundColor: '',
      data: []
    }
  ]
});

const roundOpt = ref({
  responsive: true,
  maintainAspectRatio: false, 
  aspectRatio: 2,
  scales: {
    y: {
      beginAtZero: true,
      grid: {
        display: false 
      },
      ticks: {
        
        color: 'white'
      }
    }, 
    x: {
      ticks: {
        font: {
          size: 8
        },
        color: 'white'
      },
      grid: {
        display: false 
      }
    }
  },
  plugins: {
    legend: {
      display: false
    }
  }
});

const bestData = ref({
  labels: [],
  datasets: [
    {
      label: '',
      backgroundColor: '',
      data: []
    }
  ]
});

const coursesData = ref({
  labels: [],
  datasets: [
    {
    data: [],
    backgroundColor: []
  }
]
});

const coursesOpt = ref({
  responsive: true,
  maintainAspectRatio: false, // prevent chartsize from being rendered poorly
  aspectRatio: 2,
  plugins: {
    legend: {
      display: true,
      labels: {
        color: 'white' 
      }
    }
  }

});

const getAvgs = () => {
    fetch('http://127.0.0.1:5000/youravg', {
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
            throw new Error('Failed to get averages');
        }
    })
    .then(data => {
        console.log(data);
        if(data){
            const avgRyd = data.ryd;
            const avgHammaren = data.hammaren;
            const avgAll = data.all;
            avgRydData.value = {
                labels: Object.keys(avgRyd),
                datasets: [
                    {
                        label: 'Your averages on Rydskogen DGC',
                        backgroundColor: 'green',
                        data: Object.values(avgRyd)
                    }
                ]
            };
            avgHammarenData.value = {
                labels: Object.keys(avgHammaren),
                datasets: [
                    {
                        label: 'Your averages on Hammaren DiscGolfPark',
                        backgroundColor: 'green',
                        data: Object.values(avgHammaren)
                    }
                ]
            };
            avgParData.value = {
                labels: Object.keys(avgAll),
                datasets: [
                    {
                        label: 'Your averages on pars',
                        backgroundColor: 'green',
                        data: Object.values(avgAll)
                    }
                ]
            };
        }
    })
    .catch(error => {
        console.error('Error averages:', error.message);
        
    });
    
    
};

const bestRound = () => {
    fetch('http://127.0.0.1:5000/bestround', {
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
            throw new Error('Failed to get best round');
        }
    })
    .then(data => {
        console.log(data);
        if(data.best_round){
            const bestRound = data.best_round;
            bestData.value = {
                labels: Object.keys(bestRound),
                datasets: [
                    {
                        label: 'Your score on each hole',
                        backgroundColor: 'green',
                        data: Object.values(bestRound)
                    }
                ]
            };
            
        }
    })
    .catch(error => {
        console.error('Error finding round:', error.message);
        
    });
    
    
};
const prevRound = () => {
    fetch('http://127.0.0.1:5000/previousround', {
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
            throw new Error('Failed to get latest round');
        }
    })
    .then(data => {
        if(data){
            const prevRound = data.latest_round;
            prevData.value = {
                labels: Object.keys(prevRound),
                datasets: [
                    {
                        label: 'Your score on each hole',
                        backgroundColor: 'green',
                        data: Object.values(prevRound)
                    }
                ]
            };
        }
    })
    .catch(error => {
        console.error('Error finding round:', error.message);
        
    });
    
    
};

const mostPlayed = () => {
    fetch('http://127.0.0.1:5000/mostplayed', {
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
            throw new Error('Failed to get played round');
        }
    })
    .then(data => {
        console.log(data);
        if(data.rounds){
            const played = data.rounds;
            coursesData.value = {
                labels: Object.keys(played),
                datasets: [
                    {
                        label: 'Number of times played',
                        data: Object.values(played),
                        backgroundColor: ['red', 'blue']
                    }
                ]
            };
            
        }
    })
    .catch(error => {
        console.error('Error finding rounds:', error.message);
        
    });
    
    
};
    

  onMounted(async () => {
    await getData();
    
 });
 const getData = async () =>{
  try{
    await prevRound();
    previousLoaded.value = true;
    await bestRound();
    bestLoaded.value = true;
    await getAvgs();
    avgLoaded.value = true;
    await mostPlayed();
    playedLoaded.value = true;
  }catch(error){
    console.log('Error getting data:', error.message)
  };
 };
 
</script>

<style>
/* Add your custom styles here */
</style>
  