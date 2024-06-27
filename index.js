function Delay(time){
   return new Promise(resolve => setTimeout(resolve, time));
}
let display = document.getElementById("PowerGained");
let Actions = {
  FightingNow: 0,
  TravellingNow: 0,
  TrainingNow: 0,
  MeditatingNow: 0
}
let GameData = {
  power: 0,
  powerPerSecond: 1,
  TrainingBoost: 1
};
function Display(){
  display.innerHTML =`Level ${GameData.power.toFixed(2)}, Fight Efficiency ${GameData.powerPerSecond.toFixed(2)}`;
}
async function Fight() {
  Actions.FightingNow=1;
  Actions.TrainingNow=0;
  while (Actions.FightingNow==1){
    GameData.power += (GameData.powerPerSecond/10);
    Display();
    await Delay(100);
  }
}
async function Train(){
  Actions.TrainingNow=1;
  Actions.FightingNow=0;
  while (TrainingNow==1){
    GameData.powerPerSecond += (GameData.TrainingBoost);
    Display();
    await Delay(100);
  }
}
