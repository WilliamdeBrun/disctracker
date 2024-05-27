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



  // Define reactive variables
  const updatePlayer = ref([]);
  const username = ref('');
  const notTempPlayerList = ref([]);
  const Score = ref([]);
  const ScoreCopy = ref([]);
  const localTotScore = ref([]);
  const savescoreOnHole = ref(18);
  const rydholePar = ref([]);
  const hamholePar = ref([]);
  const HolePar = ref([]);
  const Hole = ref(1);
  const active = ref(1);
  const highlight = (item, players) => {
     active.value = item;
     username.value = players[item-1];
  }
  const addScore = (index) => {
    console.log(Hole.value);
    localTotScore.value[Hole.value-1][1][index][0] += 1;
    Score.value[index][0] = localTotScore.value[Hole.value-1][1][index][0];
    console.log("addScore: ",Score.value);
  };
  const subScore = (index) => {
    if (localTotScore.value[Hole.value-1][1][index][0] > 0){
        localTotScore.value[Hole.value-1][1][index][0] -= 1;
        Score.value[index][0] = localTotScore.value[Hole.value-1][1][index][0];
    }
  };
  const changeNextHole = () => {
    if(Hole.value === savescoreOnHole.value){
        saveScore();
    }
    if (Hole.value < 18){
        savescorelocal();
        Hole.value += 1;
    }
  };
  const changePrevHole = () => {
    if (Hole.value > 1){
        Hole.value -= 1;
        for(let i = 0; i < Score.value.length; i++){
            Score.value[i][0] = localTotScore.value[Hole.value-1][1][i][0];
        }
        //Score.value[0] = localTotScore.value[0][s];
        //savescorelocal(); 
    }
  };


  const savescorelocal = () => {
    console.log("first ", localTotScore.value[0], "Score: ", Score.value);
    //localTotScore.value.push([Hole.value,Score.value,username.value]);
    console.log("second ", localTotScore.value);
    ScoreCopy.value = Score.value;
    Score.value = [];
    for (let i = 0; i < ScoreCopy.value.length; i++) {
        Score.value.push([0,ScoreCopy.value[i][1]]);
    }
    for(let i = 0; i < Score.value.length; i++){
        //console.log("localTotScore: ",localTotScore.value[Hole.value][1][i][0]);
        //localTotScore.value.push([Hole.value,Score.value.slice(),username.value]);
        Score.value[i][0] = localTotScore.value[Hole.value][1][i][0];
    }  
    console.log("end localTotscore ",localTotScore.value);
    //localStorage.setItem('score', JSON.stringify(Score.value));
  };


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

  // Define methods
  
  onMounted(async () => {
    await getHolePar(); 
    
    if(props.course === 'Rydskogens DGC'){
        HolePar.value = rydholePar.value;
    }else{
        HolePar.value = hamholePar.value;
    }

    console.log(props.typeOfRound);
    props.players.forEach((player, index) => {
    if(player !== ''){
        updatePlayer.value.push(player); 
        Score.value.push([0,player]);   
    }   
    });
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
        console.log("HolePar: ",HolePar.value[0][0]);
        console.log(localTotScore.value[0][1][0][0]);
        for(let i = 0; i < 9; i++){
            for(let j = 0; j < Score.value.length; j++){
                console.log(i,j);
                localTotScore.value[i][1][j][0] = HolePar.value[0][i];
            }
        }
        for(let i = 9; i < 18; i++){
            for(let j = 0; j < Score.value.length; j++){
                console.log(HolePar.value);
                localTotScore.value[i][1][j][0] = HolePar.value[1][i-9];
            }
        }
    }
            
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
  