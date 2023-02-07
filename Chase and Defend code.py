# Chase-and-Defend

#This is a two-player python game I made, using the Turtle package. The game has a blue and a red square. The red square's goal is to touch the blue square. The blue square's goal is the eliminate the red square by shooting with bullets that go to its cursor (you have zero ammo to start, but you could reload to get a bullet). Blue controls: W : jump, A : left, D : right, S : down, R : reload. Red controls: Arrow keys

import turtle

sc = turtle.Screen()
sc.title('Chase and Defend')
sc.setup(width = 1000, height = 600)

bullet = turtle.Turtle()
bullet.ht()
bullet.penup()
bullet.color('black')
bullet.shape('circle')
bullet.shapesize(stretch_wid=1, stretch_len=1)

player2Health = 10

ammoList = []

def bulletFire(x, y):
  if ammoList[-1] == 0:
    print('no ammo')
  else:
    bullet.st()
    bullet.speed(5)
    bullet.goto(x, y)
    if (bullet.xcor() <= player2.xcor() + 90) and (bullet.xcor() >= player2.xcor() - 90) and (bullet.ycor() <= player2.ycor() + 90) and (bullet.ycor() >= player2.ycor() - 90):
      global player2Health
      player2Health -= 1.1
    bullet.ht()
    ammoList.append(0)

def bulletReload():
  bullet.ht()
  ammoList.append(1)
  bullet.speed(0)
  bullet.goto(player1.xcor(), player1.ycor())

player2HealthBar = turtle.Turtle()

player2HealthBar.penup()
player2HealthBar.speed(0)
player2HealthBar.goto(-350, 250)
player2HealthBar.shape('square')
player2HealthBar.color('green')

player2Bg = turtle.Turtle()

player2Bg.penup()
player2Bg.speed(0)
player2Bg.goto(-350, 250)
player2Bg.shape('square')
player2Bg.shapesize(stretch_wid=1.5, stretch_len=10)
player2Bg.fillcolor('')

# P1
player1 = turtle.Turtle()
player1.penup()
player1.color('blue')
player1.shape('square')
player1.goto(450, -240)
player1.shapesize(stretch_wid=1, stretch_len=1, outline=50)



def up1():
  if player1.ycor() >= -200:
    return False
  else:
    jumpPower = 12.5
    for i in range(85):
      yCor = player1.ycor() + jumpPower
      player1.sety(yCor)
      jumpPower -= 0.3
      if (player1.ycor() + 85 >= player2.ycor()) and (player1.ycor() - 85 <= player2.ycor()) and (player1.xcor() + 85 >= player2.xcor()) and (player1.xcor() - 85 <= player2.xcor()):
        break

      bullet.goto(player1.xcor(), player1.ycor())

    player1.sety(-240)
    


def down1():
  yCor1 = player1.ycor() - 7
  player1.sety(yCor1)
  bullet.goto(player1.xcor(), player1.ycor())
  if player1.ycor() <= -240:
    player1.sety(-239)
  if player1.ycor() >= -235:
    player1.sety(player1.ycor() - 3)
  

def left1():
  xCor1 = player1.xcor() - 8
  player1.setx(xCor1)
  bullet.goto(player1.xcor(), player1.ycor())
  if player1.ycor() <= -240:
    player1.sety(-239)
  if player1.ycor() >= -235:
    player1.sety(player1.ycor() - 3)

def right1():
  xCor1 = player1.xcor() + 8
  player1.setx(xCor1)
  if player1.ycor() <= -240:
    player1.sety(-239)
  bullet.goto(player1.xcor(), player1.ycor())
  if player1.ycor() >= -235:
    player1.sety(player1.ycor() - 3)



    # angle = math.atan2(player1.ycor() - y, player1.xcor() - x)
    # degrees = angle*180/math.pi
    # dx = int(math.cos(angle)*2)
    # dy = int(math.sin(angle)*2)
    
    # while True:
      # bulletFireX = bullet.xcor() + int(dx)
      # bulletFireY = bullet.xcor() + int(dy)
      # if (bullet.xcor() >= 500):
      #   bullet.goto(0, 0)
      #   break
      # if (bullet.ycor() <= -500):
      #   bullet.goto(0, 0)
      #   break  
# P2

player2 = turtle.Turtle()
player2.penup()
player2.color('red')
player2.shape('square')
player2.goto(-450, 0)
player2.shapesize(stretch_wid=2, stretch_len=2, outline=50)

def up2():
  yCor2 = player2.ycor() + 20
  player2.sety(yCor2)

def down2():
  yCor2 = player2.ycor() - 20
  player2.sety(yCor2)

def left2():
  xCor2 = player2.xcor() - 20
  player2.setx(xCor2)

def right2():
  xCor2 = player2.xcor() + 20
  player2.setx(xCor2)


while True:
  sc.update()

  bullet.goto(player1.xcor(), player1.ycor())

  # P1
  sc.onkeypress(up1, 'w')
  sc.onkeypress(left1, 'a')
  sc.onkeypress(right1, 'd')
  sc.onkeypress(down1, 's')
  sc.onkeypress(bulletReload, 'r')
  sc.onscreenclick(bulletFire)
  # P2
  sc.onkeypress(up2, 'Up')
  sc.onkeypress(left2, 'Left')
  sc.onkeypress(right2, 'Right')
  sc.onkeypress(down2, 'Down')
  
  if player1.ycor() <= -240:
      player1.sety(-239)


  if player2.ycor() <= -240:
    player2.sety(-239) 
  
  player2HealthBar.shapesize(stretch_wid=1.5, stretch_len=player2Health)

  if (player1.ycor() + 85 >= player2.ycor()) and (player1.ycor() - 85 <= player2.ycor()) and (player1.xcor() + 85 >= player2.xcor()) and (player1.xcor() - 85 <= player2.xcor()):
    global death
    death = True
    break

  if player2Health <= 0:
    death = False
    break
  sc.listen()

sc.clear()



if death:
  while True:
    turtle.write('Red square wins!', align='Center', font=('Arial', 30, 'normal'))

if not death:
  while True:
    turtle.write('Blue square wins!', align='Center', font=('Arial', 30, 'normal'))
