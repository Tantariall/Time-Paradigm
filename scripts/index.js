function Delay(time){
   return new Promise(resolve => setTimeout(resolve, time));
};
function ResetActions(){
   Actions = {
  FightingNow: 0,
  TravellingNow: 0,
  TrainingNow: 0,
  MeditatingNow: 0,
   }
};
let display = document.getElementById("Stats");
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
  display.innerHTML =`Your Power is ${Player.Power.toFixed(2)}, Gold ${Player.Gold.toFixed(2)}, Distance ${Player.Distance.toFixed(2)}`;
};
function Act(x){
   ResetActions()
   Delay (2000)
   if (x==1){
      Actions.TravellingNow=1;
      Do().Travel();
   }
   else if (x==2){
      Actions.FightingNow=1;
      Do().Fight();
   }
   else if (x==3){
      Actions.TrainingNow=1;
      Do().Train();
   }
   else{
      //Do Nothing
   }
};
async function Fight(){
   while (Actions.FightingNow==1){
      Player.Gold += 0.01+(Math.log10(Player.Distance+1));
      Player.Power += 0.01+(Math.log2(Player.Distance+1))/10;
      Display();
      await Delay(10);
   }
}
async function Train(){
   while (Actions.TrainingNow==1){
      Player.Power += 1;
      Display();
      await Delay(10);
   }
}
async function Travel(){
   while (Actions.TravellingNow==1){
      Player.Distance += ((Player.Power**1.05)-Player.Distance)/500;
      Display();
      await Delay(10);
   }
}
