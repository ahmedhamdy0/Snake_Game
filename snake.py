import pygame  
from pygame.locals import * 
from random import randrange 

pygame.init()

black = (0,0,0)
white = (255 , 255 , 255) 
red = (255,0,0)
green = (0,255,0)
gray = (128,128,128)

display_width = 800
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height) , 0 , 32 )
pygame.display.set_caption('SNAKE')

clock = pygame.time.Clock()
FPS = 30 # frames per second

def snake(block_size , snakeList): # drawing snake  
  for a in snakeList  : 
    pygame.draw.rect(gameDisplay , green ,[a[0],a[1],block_size,block_size])

def apples(): # drawing apples 
  pygame.draw.rect(gameDisplay , red ,  [ x_apples , y_apples   ,block_size+5 , block_size+5])


def initial_state() : 
  global score 
  score = 0
  global change 
  change = 0 
  global x_snake
  x_snake = display_width/2
  global y_snake
  y_snake = display_height/2
  global x_change
  x_change = 0
  global y_change 
  y_change = 0
  global x_apples 
  x_apples = randrange(0,display_width-15)
  global y_apples
  y_apples = randrange(0,display_height-15)
  global snakeList 
  snakeList = [] # to store snake head and body locations 
  global snakeLength
  snakeLength = 1
  global block_size 
  block_size = 15 
  global speed
  speed = 300

initial_state()
# ==================================================================================== 
# draw score statement 
score_font = pygame.font.SysFont("ubuntu",40)
score_font_surface = score_font.render(str(score) , True , gray , None)
score_font_x = display_width - 130 
score_font_y = 100 
# ====================================================================================
your_score = pygame.font.SysFont("ubuntu" , 30)
your_score_surface = your_score.render("Your Score" , True , gray , None)
your_score_x  = display_width - 200
your_score_y = 50
# =====================================================================================
game_over = pygame.font.SysFont("ubuntu" , 60 )
game_over_surface = game_over.render(" Game Over  " , True , red , None )
game_over_x = display_width/2 - 150  
game_over_y = display_height/2 - 50 
# =====================================================================================
try_again = pygame.font.SysFont("ubuntu" , 30 )
try_again_surface = try_again.render("try again ... " , True , white , None) 
try_again_x = display_width/2 - 100 
try_again_y = display_height/2 + 50 
# =====================================================================================
final_score = pygame.font.SysFont("ubuntu" , 160 )
final_score_x = display_width / 2 - 30   
final_score_y = 50 
# =====================================================================================


# =====================================================================================
my_name = pygame.font.SysFont("ubuntu" , 20 )
my_name_surface = my_name.render("Ahmed Hamdy" , True , gray , None)
my_name_x = display_width/2 + 225
my_name_y = display_height/2 + 250
# =====================================================================================
while True :
  time_passed  =  clock.tick(FPS)
  time_passed_seconds = time_passed / 1000.0 
  change = speed * time_passed_seconds 

  for event in pygame.event.get() : 
    if event.type == QUIT : 
      	exit() 
    if event.type == KEYDOWN :  # key is pressed 
# ================== [ ^ ] =============================
      if event.key == K_UP : 
        x_change = 0
        y_change -= change
        if y_change == 0 : 
        	y_change -= change 
        if y_change < -block_size : 
        	y_change += change
# ================== [ v ] =============================     
      elif event.key == K_DOWN : 
        x_change = 0
        y_change += change
        if y_change==0:
        	y_change +=change
        if y_change > block_size :  
        	y_change -= change

# ================== [ > ] =============================
      elif event.key == K_RIGHT : 
        x_change +=change 
        y_change = 0
        if x_change == 0 : 
        	x_change += change
        if x_change > block_size : 
        	x_change -= change

# ================== [ < ] =============================
      elif event.key == K_LEFT : 
        x_change -= change 
        y_change = 0
        if x_change == 0 :
            x_change -= change
        if x_change < -block_size :
            x_change += change
# ======================================================  
	
  x_snake = x_snake + x_change 
  y_snake = y_snake + y_change
  #force the snake to be in the screen borders and not escape from us 
  if x_snake > display_width : 
    x_snake = 0 
  elif x_snake < 0 : 
    x_snake = display_width
  if y_snake > display_height : 
    y_snake = 0 
  elif y_snake <0 : 
    y_snake = display_height
  gameDisplay.fill(black)
  apples()
  snakeHead = []
  snakeHead.append(x_snake)
  snakeHead.append(y_snake)
  snakeList.append(snakeHead)
  if len(snakeList) > snakeLength:
    del snakeList[0]
  for element in snakeList[:-1]:
    if element == snakeHead :
  #  print("Game Over , Try again ... ")
  	  gameDisplay.fill(black) 	  
  	  final_score_surface = final_score.render(str(score) , True , green , None)
  	  gameDisplay.blit(final_score_surface , (final_score_x , final_score_y))
  	  gameDisplay.blit(game_over_surface , (game_over_x , game_over_y))
  	  gameDisplay.blit(try_again_surface , (try_again_x , try_again_y))
  	  pygame.display.update()
  	  pygame.time.delay(1000)
  	  initial_state()

  #    exit()
  snake(block_size,snakeList)
  if x_snake<=x_apples+10 and x_snake >= x_apples-10  and y_snake <= y_apples+10 and y_snake >= y_apples-10 :
    score +=1 
    snakeLength +=1 
    x_apples = randrange(0,display_width)
    y_apples = randrange(0,display_height)
    apples()
    #print("Your Score = {} " .format(score))
  change = time_passed_seconds * speed
 

  score_font_surface = score_font.render(str(score) , True , gray , None)
  gameDisplay.blit(your_score_surface , (your_score_x , your_score_y))
  gameDisplay.blit(score_font_surface , (score_font_x , score_font_y))
  gameDisplay.blit(my_name_surface , (my_name_x , my_name_y))
  pygame.display.update()
  