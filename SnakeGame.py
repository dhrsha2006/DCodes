import pygame
import random
pygame.init()
h=600
w=600
gamewin=pygame.display.set_mode((h,w))
pygame.display.set_caption("Snakes")
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,0)
quit_game=False
game_over=False
score=0
snake_x=30
s=0
snake_y=30
food_x=random.randint(50,h-50)
food_y=random.randint(50,w-50)
velocity_x=2
velocity_y=3
snake_size1=10
snake_size2=20
clock=pygame.time.Clock()
snake_eatx=10
snake_eaty=10
fps=30
font=pygame.font.SysFont(None,55)
while quit_game==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
             velocity_x=5
             velocity_y=0
             s=snake_size1
             snake_size1=snake_size2
             snake_size2=s
             # if velocity_x < 0:
             #     s = snake_size2
             #     snake_size2 = snake_size1
             #     snake_size1 = s
            if event.key==pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
                s = snake_size1
                snake_size1 = snake_size2
                snake_size2 = s
                # if velocity_x > 0:
                #     s = snake_size2
                #     snake_size2 = snake_size1
                #     snake_size1 = s
            if event.key==pygame.K_UP:
                velocity_x = 0
                velocity_y = -5
                s = snake_size2
                snake_size2 = snake_size1
                snake_size1 = s
                # if velocity_y<0:
                #  s = snake_size2
                #  snake_size2 = snake_size1
                #  snake_size1 = s
            if event.key==pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 5
                s = snake_size2
                snake_size2 = snake_size1
                snake_size1 = s
                # if velocity_y>0:
                #  s = snake_size2
                #  snake_size2 = snake_size1
                #  snake_size1 = s
    if abs(snake_x-food_x)<snake_eatx and abs(snake_y-food_y)<snake_eaty:
            score+=1
            snake_size2+=2
            snake_eatx+=1
            snake_eaty+=1
            food_x = random.randint(10, h-10)
            food_y = random.randint(10, w-10)
            print("Score:",score)
    gamewin.fill(black)
    screen_text = font.render("Score:"+str(score), True, white)
    gamewin.blit(screen_text, [10, 10])
    snake_x+=velocity_x
    snake_y+=velocity_y
    snake=pygame.draw.rect(gamewin,red,[snake_x,snake_y,snake_size1,snake_size2])
    food=pygame.draw.circle(gamewin,yellow,[food_x,food_y],7,7)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
