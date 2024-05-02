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
        </div>
           
    </div>   

</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'
  import { Bar, Doughnut } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement } from 'chart.js'
  // Define reactive variables
  const username = ref('');
 // Ensure Chart.js plugins are registered
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement);

// Define reactive variables
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
  