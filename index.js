let GameData={
  power: 0,
  powerOnClick: 1
}

function Gain(){
  GameData.power += GameData.powerOnClick
  document.getElementById("PowerGained").innerHTML = gameData.power + " Power"
}
