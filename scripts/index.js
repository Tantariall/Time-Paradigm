const buttons = document.querySelectorAll('.styled');
buttons.forEach(button => {
  button.addEventListener('click', () => {
    buttons.forEach(button => button.classList.remove('active'));
    button.classList.add('active');
    });
});
function Delay(time){
   return new Promise(resolve => setTimeout(resolve, time));
};
let display = {
   PowerDisplay: document.getElementById("Power"),
   DistanceDisplay: document.getElementById("Distance"),
   GoldDisplay: document.getElementById("Gold")
}
let Actions = "Nothing"
let Player = {
   Power: 0,
   Gold: 0,
   Distance: 0,
};
function Display(){
  display.PowerDisplay.innerHTML = Player.Power.toFixed(2);
  display.DistanceDisplay.innerHTML = Player.Distance.toFixed(2);
  display.GoldDisplay.innerHTML = Player.Gold.toFixed(0);
};
async function Act(x){
   if (x==1){
      Actions = "Travel"
   } else if (x==2){
      Actions = "Fight"
   } else if (x==3){
      Actions = "Train"
   } else if (x==0){
      Actions = "Nothing"
   }
}
async function Eternal_Act(){
   while (1>0){
   if (Actions=='Travel'){
      Travel();
   }
   else if (Actions=='Fight'){
      Fight();
   }
   else if (Actions=='Train'){
      Train();
   }
   else if (Actions=="Nothing"){
      //NOTHING;
   }
   Display()
   await Delay(10)
   }
}
function Fight(){
   Player.Gold += 0.1;
};
function Train(){
   Player.Power += 0.0005
};
function Travel(){
   Player.Distance += 0.001
};
Eternal_Act()
