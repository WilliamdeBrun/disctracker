<template>
    <div class="flex flex-col relative justify-top items-center h-full w-full">
        <div class="w-4/5 h-4/5 bg-opacity-90 rounded-lg">

                <div class="flex justify-center absolute inset-x-0 top-[5%] left-1/3  bg-slate-900 w-2/6 h-1/4 rounded-lg">
                    <p class="text-white self-center ">HOLE {{ Hole }}</p>
                </div>
                <div @click="changePrevHole()" class=" flex justify-center absolute inset-y-0 left-[10%] top-[5%] bg-slate-900 w-[23%] h-1/4 rounded-lg">
                    <i class="fa fa-arrow-left self-center text-white"></i>
                </div>
                <div @click="changeNextHole()"  class=" flex justify-center absolute inset-y-0 left-[67%] top-[5%] bg-slate-900 w-[23%] h-1/4 rounded-lg">
                    <i class="fa fa-arrow-right self-center text-white"></i>
                </div>
                <div class=" absolute inset-x-0 top-[35%] w-[80%] left-[10%]"> 
                    <div v-for="(player,index) in updatePlayer" :key="index" class="flex items-center  mb-1">
                        <div class="flex  bg-slate-900 w-full  h-44 rounded-md"> 
                            <div class="w-full h-full justify-center items-center text-center overflow-hidden">
                                <p class="text-white text-[400%] mt-3">{{ player }}</p>
                            </div>
                            <div class="w-full h-full flex justify-end mr-3 items-center text-center"> 
                                <div class="rounded-md bg-slate-600  w-[160px] h-[90%]" @click="subScore(index)">-</div>
                                <div class="text-white w-[140px] h-[70%] text-[120px] -mt-20">{{ Score[index][0] }}</div>
                                <div class="rounded-md bg-slate-600  w-[160px] h-[90%]" @click="addScore(index)">+</div>
                            </div>
                        </div> 
                    </div>
                </div>
        </div>
    </div>
</template>
  
  
  
  
  <script setup>
  import { ref, onMounted} from 'vue'

  const props = defineProps({
    course: String,
    typeOfRound: {
        type: String,
        default: 'Full18'
    },
    players: {
    type: Array,
    default: () => [],
    },
  });



  // Our reactive variables
  const updatePlayer = ref([]);
  const username = ref('');
  const Score = ref([]);
  const ScoreCopy = ref([]);
  const localTotScore = ref([]);
  const savescoreOnHole = ref(18);
  const rydholePar = ref([]);
  const hamholePar = ref([]);
  const HolePar = ref([]);
  const Hole = ref(1);

  //A function that adds a score to a player
  const addScore = (index) => {

    localTotScore.value[Hole.value-1][1][index][0] += 1;
    Score.value[index][0] = localTotScore.value[Hole.value-1][1][index][0];
  
  };
  //A function that subtracts a score from a player
  const subScore = (index) => {
    if (localTotScore.value[Hole.value-1][1][index][0] > 0){
        localTotScore.value[Hole.value-1][1][index][0] -= 1;
        Score.value[index][0] = localTotScore.value[Hole.value-1][1][index][0];
    }
  };
  //A function that changes the hole to the next hole, and saves the score if the hole is the same as the hole to save the score on.
  // (default is 18, so it saves the score on the last hole)
  const changeNextHole = () => {
    if(Hole.value === savescoreOnHole.value){
        saveScore();
    }
    if (Hole.value < 18){
        savescorelocal();
        Hole.value += 1;
    }
  };
  //A function that changes the hole to the previous hole
  const changePrevHole = () => {
    if (Hole.value > 1){
        Hole.value -= 1;
        for(let i = 0; i < Score.value.length; i++){
            Score.value[i][0] = localTotScore.value[Hole.value-1][1][i][0];
        }
       
    }
  };

  //A function that saves the score on the local variable
  const savescorelocal = () => {
    ScoreCopy.value = Score.value;
    Score.value = [];
    for (let i = 0; i < ScoreCopy.value.length; i++) {
        Score.value.push([0,ScoreCopy.value[i][1]]);
    }
    for(let i = 0; i < Score.value.length; i++){
        
        Score.value[i][0] = localTotScore.value[Hole.value][1][i][0];
    } 
  };

  //A function that gets the holepars for the current course that is being played 
  const getHolePar = async () => {
    await fetch('http://localhost:5000/coursepars', {
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
            throw new Error('Failed to get holepars');
        }
    })
    .then(data => {
        if(data){
            rydholePar.value.push(data.rydf9);
            rydholePar.value.push(data.rydb9);
            hamholePar.value.push(data.hamf9);
            hamholePar.value.push(data.hamb9);
            console.log("rydholePar: ",rydholePar.value);
            console.log("hamholePar: ",hamholePar.value);
        }
    })
    .catch(error => {
        console.error('Error getting holepars:', error.message);
    });
    };

  // A function that saves the score to the SQL database.  
  const saveScore = () => {
    fetch('http://localhost:5000/savescoreonhole', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        },
        body: JSON.stringify({
            course_name: props.course,
            score: localTotScore.value
        }),
    })
    .then(response => {
        if (response.ok) {

        } else {

        }
    })
    .catch(error => {
        console.error('Failed to save score:', error);
    });
  };

  // A function that is being called when the component is mounted.
  onMounted(async () => {

    // To start with, the holepars for the current course is fetched.
    await getHolePar(); 
    
    // check which course is being played and set the holepars accordingly
    if(props.course === 'Rydskogens DGC'){
        HolePar.value = rydholePar.value;
    }else{
        HolePar.value = hamholePar.value;
    }

    // Set up the players and their scores, starting with 0 for each player.
    props.players.forEach((player, index) => {
    if(player !== ''){
        updatePlayer.value.push(player); 
        Score.value.push([0,player]);   
    }   
    });

    // Set up the localTotScore variable with the scores for each player on each hole.
    for(let i = 0; i < 18; i++){
            ScoreCopy.value = Score.value;
            Score.value = [];
            for (let j = 0; j < ScoreCopy.value.length; j++) {
                Score.value.push([0,ScoreCopy.value[j][1]]);
            }
            localTotScore.value.push([i,Score.value.slice()]);
    }
    if(props.typeOfRound === 'F9'){
        Hole.value = 1;
        savescoreOnHole.value = 9;
        for(let i = 0; i < 9; i++){
            for(let j = 0; j < Score.value.length; j++){
                localTotScore.value[i][1][j][0] = HolePar.value[0][i];
                localTotScore.value[17][1][j][0] = 0;
            }
        }
    }else if(props.typeOfRound === 'B9'){
        savescoreOnHole.value = 18;
        Hole.value = 10;
        for(let i = 9; i < 18; i++){
            for(let j = 0; j < Score.value.length; j++){
                localTotScore.value[i][1][j][0] = HolePar.value[1][i-9];
            }
        }
    }else{
        savescoreOnHole.value = 18;
        Hole.value = 1;
        for(let i = 0; i < 9; i++){
            for(let j = 0; j < Score.value.length; j++){
                localTotScore.value[i][1][j][0] = HolePar.value[0][i];
            }
        }
        for(let i = 9; i < 18; i++){
            for(let j = 0; j < Score.value.length; j++){
                localTotScore.value[i][1][j][0] = HolePar.value[1][i-9];
            }
        }
    }
    
    // This is for the first hole, to set the scores for each player.
    for(let i = 0; i < Score.value.length; i++){
        Score.value[i][0] = localTotScore.value[Hole.value-1][1][i][0];
        if(props.typeOfRound === 'F9'){
            localTotScore.value[17][1][i][0] = 0;
        }
    }
 });
</script>


<style scoped>
.highlighted {
  border: 2px solid yellow;
}
</style>
  