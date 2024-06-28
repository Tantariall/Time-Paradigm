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
let Player = {
   Power: 0,
   Gold: 0,
   Distance: 0,
};
function Display(){
  display.innerHTML =`Your Power is ${GameData.power.toFixed(2)}, Fight Efficiency ${GameData.powerPerSecond.toFixed(2)}`;
}
function Act(x){
   ResetActions()
   if (x==1){
      Actions.TravellingNow=1;
      //Travel();
   }
   else if (x==2){
      Actions.FightingNow=1;
      Fight();
   }
   else if (x==3){
      Actions.TrainingNow=1;
      Train();
   }
   else{
      //Do Nothing
   }
async function Fight(){
   while (Actions.FightingNow==1){
      Player.Gold += 0.01+(math.log10(Player.Distance));
      Player.Power += 0.01+(math.log2(Player.Distance));
      Display();
      await Delay(10);
