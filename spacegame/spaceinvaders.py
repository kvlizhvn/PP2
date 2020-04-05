import pygame
import random,time
pygame.init()


screen = pygame.display.set_mode((800, 600))


enemyImage = pygame.image.load("enemy.png")
enemy_x = [random.randint(0, 736)]
enemy_y = [random.randint(20, 50)]


bulletImage = pygame.image.load("bullet.png")
bullet_x = [200]
bullet_y = [436]


backgroundImage = pygame.image.load("background.jpg")
playerImage = pygame.image.load("player.png")
player_x = 200
player_y = 536


enemy_dx = [5]    
enemy_dy = 30


def score_text():
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render("Score: "+str(score), 1, (180, 180, 0))
    screen.blit(text1, (650, 10))

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullet(x, y):
    screen.blit(bulletImage, (x, y))

f=[False]
i=0
g=1
score=0


#GAME LOOP
done = False
while not done:
    f1 = pygame.font.Font(None, 36)


    
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT : 
            done = True
        if  pressed[pygame.K_f]:
            bullet_x[i]= player_x
            bullet_x.append(player_x)
            bullet_y[i]=536
            bullet_y.append(536)
            f[i]=True           
            f.append(False)
            i+=1
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: player_x -= 5
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: player_x += 5
    
    
        if pressed[pygame.K_ESCAPE]:
            done = True
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: player_x -= 5
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: player_x += 5

    
    for k in range (0,g):
        enemy_x[k] += enemy_dx[k]
        enemy_dx.append(3)
        if enemy_x[k] < 0 or enemy_x[k] > 736:
            enemy_dx[k] = -enemy_dx[k]
            enemy_y[k] += enemy_dy
        if player_x < 0:
            player_x += 5
        if player_x >736:
            player_x -= 5

        if enemy_y[k]>550:
            enemy_y[k]=False
            

    screen.blit(backgroundImage, (0, 0)) 
    player(player_x, player_y)
    for k in range (0,g):
        if enemy_y[k]:
            enemy(enemy_x[k], enemy_y[k])    
    score_text()
    for j in range (0,i):
        if f[j]:
            if bullet_y[j]<0:
                f[j]=False
            bullet_y[j] -= 10
            for k in range(0,g):
                if (enemy_x[k] + 50 >= bullet_x[j]>=enemy_x[k]-50) and (enemy_y[k] + 50 >= bullet_y[j]>=enemy_y[k]):
                    if score<5:
                        enemy_y[k] = False
                        enemy_y.append(random.randint(0, 100))
                        enemy_x.append(random.randint(0, 736))
                        g+=1
                    else: 
                        numm=score//50
                        enemy_y[k]=False
                        for y in range (0,numm):
                            enemy_y.append(random.randint(0, 100))
                            enemy_x.append(random.randint(0, 736))
                            g+=1
                    score+=1
                    f[j]=False

                bullet(bullet_x[j]+8, bullet_y[j])
                bullet(bullet_x[j]+52, bullet_y[j])

    for k in range(0,g):
        if (player_x + 50 >=enemy_x[k]>=player_x-50)and(enemy_y[k]>=486):
          pygame.quit()

    pygame.display.flip()