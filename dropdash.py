import pygame 
import time
import random
pygame.font.init()

width , height = 1000,800


WIN =  pygame.display.set_mode((width,height))
pygame.display.set_caption("dropdash")
BG = pygame.transform.scale(pygame.image.load("assets/img/bg-1.jpg"),(width,height))
Player_W = 40
Player_H = 60
Player_VEL = 5 
font = pygame.font.SysFont("comicsans",30)
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0




STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VAL = 3
def draw(player,elapsed_time,stars):
    WIN.blit(BG,(0,0))
    time_text = font.render(f"Time: {round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))
    pygame.draw.rect(WIN,"red",player)
    for star in stars:
        pygame.draw.rect(WIN,"white",star)
    pygame.display.update()






def main():
    stars_count = 0
    stars_increament = 2000
    stars = []
    hit = False


    run = True
    player = pygame.Rect(200,height - Player_H, Player_W, Player_H)
    while run:
        stars_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        if stars_count > stars_increament:
            for _ in range(3):
                star_x = random.randint(0,width - STAR_WIDTH)
                star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH,STAR_HEIGHT)
                stars.append(star)
            stars_increament = max(200,stars_increament - 50)
            stars_count = 0    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - Player_VEL >= 0:
            player.x -= Player_VEL
        if keys[pygame.K_RIGHT] and player.x + Player_VEL + Player_W <= width:
            player.x += Player_VEL       
        
        for star in stars[:]:
            star.y += STAR_VAL 
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit :
            lost_text = font.render("You Lost",1,"white")
            WIN.blit(lost_text,(width/2 - lost_text.get_width()/2,height/2 - lost_text.get_width()/2))    
            pygame.display.update()
            pygame.time.delay(4000)
            break
        draw(player,elapsed_time,stars)    
    pygame.quit()


if __name__ == "__main__":
    main()