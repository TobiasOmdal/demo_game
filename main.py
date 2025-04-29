import pygame

pygame.init()
pygame.font.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_zone = pygame.Vector2(400, 600)
opponent_zone = pygame.Vector2(800, 200)
menu_width, menu_height = (180, 80)

menu = [pygame.Rect(800, 500, menu_width, menu_height), 
        pygame.Rect(1000, 500, menu_width, menu_height), 
        pygame.Rect(800, 600, menu_width, menu_height), 
        pygame.Rect(1000, 600, menu_width, menu_height)] 

battle_ground_player = pygame.Rect(200, 400, 400, 200)
battle_ground_opponent = pygame.Rect(800, 200, 400, 160)

def render():
    screen.fill("purple")
    pygame.draw.circle(screen, "white", player_pos, 20)
    
    pygame.draw.ellipse(screen, "green", battle_ground_player, 0)
    pygame.draw.ellipse(screen, "green", battle_ground_opponent, 0)

    pygame.draw.rect(screen, "grey", menu[0])
    pygame.draw.rect(screen, "grey", menu[1])
    pygame.draw.rect(screen, "grey", menu[2])
    pygame.draw.rect(screen, "grey", menu[3])

    font = pygame.font.Font('freesansbold.ttf', 32)
    menu1 = font.render("Fight", True, (255, 255, 255), 'grey')
    menu2 = font.render("Team", True, (255, 255, 255), 'grey')
    menu3 = font.render("Settings", True, (255, 255, 255), 'grey')
    menu4 = font.render("Flee", True, (255, 255, 255), 'grey')

    menu1_rect = menu1.get_rect()
    menu2_rect = menu2.get_rect()
    menu3_rect = menu3.get_rect()
    menu4_rect = menu4.get_rect()

    menu1_rect.center = (800 + menu_width // 2, 500 + menu_height // 2)
    menu2_rect.center = (1000 + menu_width // 2, 500 + menu_height // 2)
    menu3_rect.center = (800 + menu_width // 2, 600 + menu_height // 2)
    menu4_rect.center = (1000 + menu_width // 2, 600 + menu_height // 2)

    screen.blit(menu1, menu1_rect)
    screen.blit(menu2, menu2_rect)
    screen.blit(menu3, menu3_rect)
    screen.blit(menu4, menu4_rect)


    pygame.display.flip()

def update():
    global dt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    dt = clock.tick(60) / 1000

def attack():
    print("ATTACK")

def processEvents():
    global running
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > 800 and x < 800 + menu_width and y > 500 and y < 500 + menu_height:
                    attack()
                elif x > 1000 and x < 1000 + menu_width and y > 500 and y < 500 + menu_height:
                    print("Team")
                elif x > 800 and x < 800 + menu_width and y > 600 and y < 600 + menu_height:
                    print("Settings")
                elif x > 1000 and x < 1000 + menu_width and y > 600 and y < 600 + menu_height:
                    print("Flee")

def main_loop():
    while running:
        processEvents()
        update()
        render()


if __name__ == "__main__":
    main_loop()
    pygame.font.quit()
    pygame.quit()