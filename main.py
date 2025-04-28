import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_zone = pygame.Vector2(400, 600)
opponent_zone = pygame.Vector2(800, 200)

def render():
    screen.fill("purple")
    pygame.draw.circle(screen, "white", player_pos, 20)
    
    pygame.draw.circle(screen, "green", player_zone, 100)
    pygame.draw.circle(screen, "green", opponent_zone, 100)
    
    pygame.display.flip()

def update():
    global dt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    elif keys[pygame.K_s]:
        player_pos.y += 300 * dt
    elif keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    elif keys[pygame.K_d]:
        player_pos.x += 300 * dt

    dt = clock.tick(60) / 1000

def processEvents():
    global running
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def main_loop():
    while running:
        processEvents()
        update()
        render()


if __name__ == "__main__":
    main_loop()
    pygame.quit()