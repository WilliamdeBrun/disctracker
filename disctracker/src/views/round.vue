<template>
    <div class="flex flex-wrap relative justify-center items-top w-full mt-44">
        <div class="lg:w-11/12 lg:h-11/12 w-11/12 lg:mx-2 my-2 h-[1200px]">
            <div class="relative bg-slate-900 bg-opacity-90 rounded-lg p-4 h-full">
                <p class="text-white"></p>   
                <div class="flex justify-center absolute inset-x-0 top-0 left-1/3 bg-slate-400  bg-opacity-30 w-2/6 h-1/4 rounded-lg">
                    <p class="text-white self-center ">HOLE {{ Hole }}</p>
                </div>
                <div @click="changePrevHole()" class=" flex justify-center absolute inset-y-0 left-[10%] top-0 bg-slate-400 w-[23%] h-1/4 rounded-lg">
                    <i class="fa fa-arrow-left self-center text-white"></i>
                </div>
                <div @click="changeNextHole()"  class=" flex justify-center absolute inset-y-0 left-[67%] top-0 bg-slate-400 w-[23%] h-1/4 rounded-lg">
                    <i class="fa fa-arrow-right self-center text-white"></i>
                </div>
                <div class="flex justify-center absolute inset-y-0 left-[0%] top-[30%] bg-slate-400 w-[23%] h-[15%] rounded-lg" @click="highlight(1,{players})" :class="{ 'highlighted': active === 1 }">
                    <p class="text-white"> {{ players[0] }}</p>
                </div>
                <div class="flex justify-center absolute inset-y-0 left-[0%] top-[45%] bg-slate-500 w-[23%] h-[15%] rounded-lg" @click="highlight(2,{players})" :class="{ 'highlighted': active === 2 }">
                    <p class="text-white text-center">{{ players[1] }}</p>
                </div>
                <div class="flex justify-center absolute inset-y-0 left-[0%] top-[60%] bg-slate-400 w-[23%] h-[15%] rounded-lg" @click="highlight(3,{players})" :class="{ 'highlighted': active === 3 }">
                    <p class="text-white text-center">{{ players[2] }}</p>
                </div>
                <div class="flex justify-center absolute inset-y-0 left-[0%] top-[75%] bg-slate-500 w-[23%] h-[15%] rounded-lg" @click="highlight(4,{players})" :class="{ 'highlighted': active === 4 }">
                    <p class="text-white text-center">{{ players[3] }}</p>
                </div>
                <div @click="subScore()" class="flex justify-center absolute inset-y-0 left-[33%] top-[45%] bg-slate-500 w-[15%] h-[15%] rounded-lg">
                    <i class="fa fa-minus self-center text-white"></i>
                </div>
                <div class="flex flex-col absolute inset-y-0 left-[48%] top-[45%] bg-slate-400 w-[26%] h-[15%] rounded-lg">
                    <p class="text-white text-center">Score</p>
                     <p class="text-white text-9xl self-center">{{ Score }}</p>
                </div>
                <div @click="addScore()" class="flex justify-center absolute inset-y-0 left-[74%] top-[45%] bg-slate-500 w-[15%] h-[15%] rounded-lg">
                    <i class="fa fa-plus self-center text-white"></i>
                </div>
                <div @click="saveScore(course)" class="flex justify-center absolute inset-y-0 left-[48%] top-[65%] bg-slate-500 w-[26%] h-[15%] rounded-lg">
                    <p class="text-white self-center">Save</p>
                </div>
            </div>
        </div> 
    </div>
</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  const props = defineProps({
    course: String,
    players: {
    type: Array,
    default: () => [],
    },
  });



  // Define reactive variables
  const username = ref('user1');
  const Score = ref(0);
  const Hole = ref(1);
  const active = ref(1);
  const highlight = (item, players) => {
     active.value = item;
     username.value = players[item-1];
  }
  const addScore = () => {
    Score.value += 1;
  };
  const subScore = () => {
    if (Score.value > 0){
        Score.value -= 1;
    }
  };
  const changeNextHole = () => {
    if (Hole.value < 18){
        Hole.value += 1;
    }
  };
  const changePrevHole = () => {
    if (Hole.value > 1){
        Hole.value -= 1;
    }
  };
  const saveScore = (course) => {
    fetch('http://localhost:5000/savescoreonhole', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify({
            course_name: course.value,
            score: Score.value,
            hole_number: Hole.value,
        }),

    })
    .then(response => {
        if (response.ok) {
            // Score saved
        } else {
            // Score not saved
        }
    })
    .catch(error => {
        console.error('Failed to save score:', error);
    });
  };

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


<style scoped>
.highlighted {
  border: 2px solid yellow; /* Example highlight style */
}
</style>
  