<template>
    <div class="flex flex-col justify-top items-center h-full w-full">
        
        <div class="w-2/3 h-1/4 bg-slate-900 bg-opacity-90 rounded-lg mt-10 flex flex-col items-center">
            <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden h-1/5">Your averages</h2>
            <div class="flex w-full h-full justify-center">
                <div class="h-4/5 w-1/4 mt-2 rounded-lg mr-10 flex items-top justify-center ml-10">
                    <Bar :options="avgParOptions" :data="avgParData" />
                </div>
                <div class="h-4/5 w-1/4 mt-2 rounded-lg mr-10 flex items-top justify-center">
                    <Bar :options="avgHammarenOptions" :data="avgHammarenData" />
                </div>
                <div class="h-4/5 w-1/4 mt-2 rounded-lg flex items-top justify-center mr-10">
                    <Bar :options="avgRydOptions" :data="avgRydData" />
                </div>
            </div>
        </div>
        <div class="flex items-top justify-center w-2/3 h-1/4 mt-10 ">
            <div class="w-1/2 h-full bg-slate-900 bg-opacity-90 rounded-lg mr-10 flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Your previous round</h2>
                <div class="h-2/3 w-4/ mt-2 flex items-center justify-center">
                    <Bar :options="prevOpt" :data="prevData" />
                </div>
            </div>
            <div class="w-1/2 h-full bg-slate-900 bg-opacity-90 rounded-lg flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Your best round</h2>
                <div class="h-2/3 w-4/5 mt-2 flex items-center justify-center">
                    <Bar :options="bestOpt" :data="bestData" />
                </div>
            </div>
        </div>
        <div class="flex items-top justify-center w-2/3 h-1/3 mt-10 ">
            
            <div class="w-1/3 h-full bg-slate-900 bg-opacity-90 rounded-lg mr-10 flex flex-col items-center">
                <h2 class="text-white text-xs md:text-xl lg:text-3xl font-bold overflow-hidden">Played courses</h2>
                <div class="h-3/4 w-4/5 mt-2 flex items-center justify-center">
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
  // Define reactive variables
  const passwordChange = ref('');
  const oldPw = ref('');
  const newPw = ref('');
  const repeatPw = ref('');
  const passwordMessage = ref('');
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
  labels: ['Par 3', 'Par 4', 'Par 5'],
  datasets: [
    {
      label: 'Your averages on pars',
      backgroundColor: 'green',
      data: [3.3, 3.7, 5.9]
    }
  ]
});

const avgHammarenOptions = ref({
  responsive: true,
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
  labels: ['Par 3', 'Par 4', 'Par 5'],
  datasets: [
    {
      label: 'Your averages on Hammaren DiscGolfPark',
      backgroundColor: 'green',
      data: [3.3, 3.7, 5.9]
    }
  ]
});

const avgRydOptions = ref({
    responsive: true,
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

const avgRydData = ref({
  labels: ['Par 3', 'Par 4', 'Par 5'],
  datasets: [
    {
      label: 'Your averages on Rydskogen DGC',
      backgroundColor: 'green',
      data: [3.3, 3.7, 5.9]
    }
  ]
});

const avgParOptions = ref({
    responsive: true,
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

const prevData = ref({
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
  datasets: [
    {
      label: 'Your score on each hole',
      backgroundColor: 'green',
      data: [3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    }
  ]
});

const prevOpt = ref({
  responsive: true,
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
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
  datasets: [
    {
      label: 'Your score on each hole',
      backgroundColor: 'green',
      data: [3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    }
  ]
});

const bestOpt = ref({
  responsive: true,
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

const coursesData = ref({
  labels: ['Rydskogen F9', 'Rydskogen B9', 'Rydskogen 18', 'Hammaren F9', 'Hammaren B9', 'Hammaren 18'],
  datasets: [
    {
    data: [300, 50, 100, 40, 20, 65],
    backgroundColor: ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
  }
]
});

const coursesOpt = ref({
  responsive: true,
  plugins: {
    legend: {
      display: true,
      labels: {
        color: 'white' 
      }
    }
  }

});
 
    

  onMounted(async () => {
  
 });
 
</script>

<style>
/* Add your custom styles here */
</style>
  