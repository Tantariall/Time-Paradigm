function Delay(time){
   return new Promise(resolve => setTimeout(resolve, time));
}
function ResetActions(){
   Actions = {
  FightingNow: 0,
  TravellingNow: 0,
  TrainingNow: 0,
  MeditatingNow: 0,
   }
}
let display = document.getElementById("PowerGained");
let Actions = {
  FightingNow: 0,
  TravellingNow: 0,
  TrainingNow: 0,
  MeditatingNow: 0,
}
let GameData = {
  power: 0,
  powerPerSecond: 1,
  TrainingBoost: 1,
};
function Display(){
  display.innerHTML =`Level ${GameData.power.toFixed(2)}, Fight Efficiency ${GameData.powerPerSecond.toFixed(2)}`;
}
async function Fight() {
  ResetActions()
  Actions.FightingNow=1;
  while (Actions.FightingNow==1){
    GameData.power += (GameData.powerPerSecond/10);
    Display();
    await Delay(100);
  }
}
async function Train(){
  ResetActions()
  Actions.TrainingNow=1;
  while (Actions.TrainingNow==1){
    GameData.powerPerSecond += (GameData.TrainingBoost);
    Display();
    await Delay(100);
  }
}
