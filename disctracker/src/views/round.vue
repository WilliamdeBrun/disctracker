<template>
   <!-- 
   <div class="flex flex-col relative justify-center items-top w-full mt-44">
        <div class="lg:w-11/12 lg:h-11/12 w-11/12 lg:mx-2 my-2 h-[1200px] flex flex-col ">
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


                <div v-for="index in players" :key="index" class="flex justify-center absolute inset-y-0 left-[0%] top-[30%] bg-slate-400 w-[23%] h-[15%] rounded-lg highlighted" @click="highlight(2,{players})" :class="{ 'highlighted': active === 2 }">
                    <p class="text-white text-center">{{ players[index-1] }}</p>
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
   -->
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
  const holePar = ref([]);

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
  const toggleMode = () => {

  };

  const handleSignin = () => {
  
  };

  const handleSignup = () => {
    
  };
  onMounted(async () => {
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
    }else if(props.typeOfRound === 'B9'){
        savescoreOnHole.value = 18;
        Hole.value = 10;
    }else{
        savescoreOnHole.value = 18;
        Hole.value = 1;
    }        
   
    


    fetch('http://localhost:5000/getusers', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`
    },
    body: JSON.stringify({
        list_of_users: updatePlayer.value 
    })
    })
    .then(response => {
        if (response.ok){
            return response.json();
        }else{
            throw new error('Failed to get user');
        }
    })
    .then(data => {
        if(data){
           
        console.log("notTempPlayerList: ",notTempPlayerList.value);
        }
    })
    .catch(error => {
        console.error('Failed to check token:', error);
    });
 });
</script>


<style scoped>
.highlighted {
  border: 2px solid yellow;
}
</style>
  