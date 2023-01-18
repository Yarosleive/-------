import pygame

pygame.init()
pygame.display.set_caption('Герой двигается')
size = width, height = 600, 95
screen = pygame.display.set_mode(size)
sprite = pygame.sprite.Sprite()
sprite = pygame.image.load('data/car2.png')
screen.fill((255, 255, 255))
running = True
clock = pygame.time.Clock()
sprite_rect = sprite.get_rect()
sprite_rect_x = 0
sprite_rect_y = 0
pygame.transform.scale(sprite, (100, 95))
v = 40
right = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(sprite, (sprite_rect_x, sprite_rect_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if right:
        sprite_rect_x += v * clock.tick() / 1000
    else:
        sprite_rect_x -= v * clock.tick() / 1000
    if sprite_rect_x + 150 >= width and right:
        sprite = pygame.transform.flip(sprite, True, False)
        right = False
    elif sprite_rect_x <= 0 and not right:
        sprite = pygame.transform.flip(sprite, True, False)
        right = True
    pygame.display.flip()
pygame.quit()