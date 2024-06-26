let GameData={
  power: 0,
  powerOnClick: 1
}

function MineGold(){
  GameData.power += GameData.powerOnClick
  document.getElementById("goldMined").innerHTML = gameData.power + " Gold Mined"
}
