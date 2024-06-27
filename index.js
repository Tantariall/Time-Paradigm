let display = document.getElementById("PowerGained");
let GameData = {
  power: 0,
  powerOnClick: 1,
};
function Display(){
  display.innerHTML =`LV ${GameData.power}`;
}
function Gain() {
  GameData.power += GameData.powerOnClick;
  Display()
}
function Reset(){
  GameData.power = 0;
  Display()
}
