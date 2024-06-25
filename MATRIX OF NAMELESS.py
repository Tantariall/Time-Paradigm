import decimal
import os
import math
import random
from time import sleep
import ctypes
from msvcrt import getch, kbhit
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_MAXIMIZE = 3
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)
p=0
sp=0
pc=10
ap=0
apc=1
highest_p=0
pm=10
xcoor=0
ycoor=0
sel=0
field=[['.']*20 for i in range(20)]
def sci(x):
  return format(x, '.2e' if x>1000 else '.2f')
def rand(minimum, maximum):
  return random.randint(0,19)
def chance(x):
  if rand(1,100) in range(1,x):
    return True
  else:
    return False
for i in range(50):
  field[rand(0, 19)][rand(0,19)]='*'
field[0][0]='Y'
startscene=1
def give_points():               #POINTS GIVING
  global p, pm, highest_p, ap, apc
  p+=(ap+2)**pm
  if p>highest_p:
    highest_p=p
def shop(): #SHOP FUNCTION
  global p, pc, pm, highest_p, sp
  os.system('cls')
  while True:
    os.system('cls')
    text(4, "Q - exit shop")
    text(1, "Note: You always buy maximum amount of upgrades.")
    if highest_p>9:
      print('\n'*3,' '*26, "1 - Buy Point Boosts")
      print(' '*27, "Cost -", sci(pc), 'points')
      print(' '*27, "Effect: x"+str(sci((ap+2)**pm)), 'points')
      print(' '*27, "You have", sci(pm), 'Point Boosts')
    if highest_p>99:
      print('\n'*2,' '*26, "2 - Buy Amplifiers")
      print(' '*27, "Cost -", sci(apc), 'Point Boosts')
      print(' '*27, "Effect: +"+str(sci(ap)), 'Point Boost power')
      print(' '*27, 'You have', sci(ap), 'Amplifiers')
    if highest_p>299:
      print("\n"*2,' '*26, "3 - Sacrifice | Trade | Exchange")
      print(' '*27, 'Sacrificed -', sci(sp), 'points')
      print(' '*27, 'Effect: x'+str(sci(math.log(sp+1, 15)+1)), 'points')
    while True:
      select()
      if sel!=0:
        if sel==49:
          purchase(1)
        if sel==50 and highest_p>99:
          purchase(2)
        if sel==51 and highest_p>299:
          purchase(3)
        if sel==113:
          os.system('cls')
          play()
        break
def purchase(x):                               #PURCHASE FUNCTION-----------------
  global p, pm, highest_p, pc, apc, ap, sp
  if x==1:
    while p>=pc:
      pm+=1
      p-=pc
      pc*=5
  if x==2:
    while pm>=apc:
      ap+=1
      pm-=apc
      apc+=1
  if x==3:
    sp+=p
    p=0
def move():
  global xcoor, ycoor
  select()
  if sel!=0:
    if (sel==80 or sel==115) and ycoor<19: #DOWN---
      field[ycoor][xcoor]='.'
      ycoor+=1
      if field[ycoor][xcoor]=='*':
        give_points()                                     #GIVE POINTS--------
      field[ycoor][xcoor]='Y'
    if (sel==72 or sel==119) and ycoor>0: #UP---
      field[ycoor][xcoor]='.'
      ycoor-=1
      if field[ycoor][xcoor]=='*':
        give_points()                                     #GIVE POINTS------
      field[ycoor][xcoor]='Y'
    if (sel==77 or sel==100) and xcoor<19: #RIGHT---
      field[ycoor][xcoor]='.'
      xcoor+=1
      if field[ycoor][xcoor]=='*':
        give_points()                                     #GIVE POINTS----
      field[ycoor][xcoor]='Y'
    if (sel==75 or sel==97) and xcoor>0: #LEFT---
      field[ycoor][xcoor]='.'
      xcoor-=1
      if field[ycoor][xcoor]=='*':
        give_points()                                         #GIVE POINTS------
      field[ycoor][xcoor]='Y'
    if sel==113 and highest_p>9:                  #GO TO SHOP-----------------
      shop()
    if sel==27:
      main_menu()
    if chance(highest_p//5):
      field[rand(0,19)][rand(0,19)]='*'
    update()
def update():
  os.system('cls')
  if highest_p<5:
    text(0, "Next goal: 5 Points")
  elif highest_p<10:
    text(0, "Next goal: 10 Points")
  elif highest_p<100:
    text(0, "Next goal: 100 Points")
  elif highest_p<300:
    text(0, "N_xt Goal: 3O0 poIn|t s")
  elif highest_p<10000:
    text(0, "Next goal: 10000 points") #LAST GOAL
  if highest_p>9:
    text(2, "Q - Shop")
  else:
    print('\n'*2)
  for i in range(20):
    print(' '*20, *field[i])
  print('\n',' '*20, "You have", sci(p), 'points','(', sci((ap+2)**pm),'per single point)')
  if highest_p>4:
    print('\n', ' '*20, "There is a", str(min(highest_p//5, 100))+'% chance of * appearing')
def play():
  global field, p, highest_p, pc
  os.system('cls')
  update()
  while True:
    move()
def main_menu():
  choice=1
  secret=0
  os.system('cls')
  while True:
    print('Version 0.1')
    text(5, 'MATRIX OF NAMELESS')
    text(2, '1 - PLAY')
    text(1, '2 - WATCH INTRO')
    text(1, '3 - HOW TO PLAY')
    text(1, '4 - LEAVE')
    text(1, str(choice))
    if secret==1:
      text(1, '5 - Secret found!')
    if choice==3:
      guide()
    while True:
      select()
      if sel!=0:
        if sel==80 and choice<5:
          choice+=1
        if sel==72 and choice>1:
          choice-=1
        if sel==13:
          if choice==1:
            play()
            break
          elif choice==2:
            os.system('cls')
            intro()
          elif choice==3:
            pass
          elif choice==4:
            os.system('cls')
            text(10, "Are you leaving? Bye then. I will wait for you.")
            cont()
            quit()
          else:
            secret=1
        os.system('cls')
        break
def text(ss, letter): #TEXT
  print('\n'*ss, ' '*(35-len(letter)//2), letter)
def cont():
  global sel
  sel=0
  while True:
    select()
    if sel==13:
      break
  os.system('cls')
def guide(): #GUIDE
  text(5, "WASD or Arrows to move.")
  text(1, "Your main goal is to get to Endgame.")
  text(1, "Your current goal will be on the top of the screen.")
  text(1, "Good luck and have fun!")
def intro(): #INTRO
  text(5, '???')
  text(0, '___________________')
  text(2, 'Huh? Another one?')
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, '???')
  text(0, '___________________')
  text(2, '...Wake up.')
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, '???')
  text(0, '___________________')
  text(2, 'Haha... Welcome to my ABODE.')
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, 'Nameless Distraught')
  text(0, '___________________')
  text(2, "We are in Matrix. My name? *giggle* Foolish labels... I DO NOT have a NAME.")
  text(0, "Why would you visit such a place? There's so boooring!")
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, 'Y%&^o())U!?@')
  text(0, '_-____/_____\___|__')
  text(2, "Danger.")
  text(0, "Destroy Mad|Psycho|Crazy.")
  text(0, "Leave.")
  text(1, '__-____|/_______-__')
  text(2, '-Enter-')
  cont()
  text(5, 'Nameless Distraught')
  text(0, '___________________')
  text(2, "")
  text(0, "Huh? Did you hear that?")
  text(0, "(My mind... resist...)")
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, 'Nameless Distraught')
  text(0, '___________________')
  text(2, "Maybe I'm hallucinating, HAHAHAHA. Wanna play a, *giggle* game?")
  text(1, '___________________')
  text(2, '-Enter-')
  cont()
  text(5, 'Y%&^o())U!?@')
  text(3, ".Find.Me.I.Help.")
  text(1, '-__  ___<>_*_ _-//')
  text(2, '-En-e--')
  cont()
  text(10, "Your task in this dance will be...")
  cont()
  text(10, "To collect POINTS.")
  cont()
  main_menu()
def select(): #KEYBOARD INPUT
  global sel
  if kbhit():
    sel=ord(getch())
    if sel==224:
      sel=ord(getch())
  else:
    sel=0
def ask(selection):
  os.system('cls')
  print('\n'*5, ' '*25, 'Skip Introduction?')
  print('\n'*3, ' '*27, 'Yes',' '*5, 'No')
  print(' '*selection, '^')
ask(38)
while True:
  select()
  if sel==77:
    ask(38)
    startscene=1
  elif sel==75:
    ask(29)
    startscene=0
  elif sel==13:
    break
os.system('cls')
if startscene==1:
  intro()
else:
  main_menu()
