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
async function Act(x){
   switch (x){
      case 1:
         //Travel;
      case 2:
         Fight();
      case 3:
         Train();
      case 4:
         //Meditate;
   }
   display()
   delay(10)
function Display(){
  display.innerHTML =`Your Power is ${GameData.power.toFixed(2)}, Fight Efficiency ${GameData.powerPerSecond.toFixed(2)}`;
}
function Fight() {
   GameData.power += (GameData.powerPerSecond/100);
}
function Train(){
   GameData.powerPerSecond += (GameData.TrainingBoost/1000);
}
