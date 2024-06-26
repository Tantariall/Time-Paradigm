let display = document.getElementById("PowerGained");
let GameData = {
  power: 0,
  powerOnClick: 1,
};

function Gain() {
  GameData.power += GameData.powerOnClick;
  display.innerHTML =`You have ${GameData.power} Power`;
}
