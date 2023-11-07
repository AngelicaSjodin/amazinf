import pygame
import math

pygame.init()
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

class Player():
    def  __init__(self):
        self.rotation_angle = 0
        self.player = pygame.Surface((20, 20), pygame.SRCALPHA)
        self.player.fill((0, 255, 0))
        self.rotated_player = self.player
        self.pos = (WIDTH//2, HEIGHT//2)
        
    def rotate(self, keys, left, right):
        if keys[right]:
            self.rotation_angle -= 0.5
        if keys[left]:
            self.rotation_angle += 0.5
        self.rotated_player = pygame.transform.rotate(self.player, (self.rotation_angle))

class Bullet:
    def __init__(self):
        self.pos = [player1.pos[0], player1.pos[1]]
        self.direction = math.radians(player1.rotation_angle)
        self.bullet = pygame.Surface((10, 5), pygame.SRCALPHA)
        self.bullet.fill((100, 200, 120))
        self.rotated_bullet = pygame.transform.rotate(self.bullet, player1.rotation_angle)
        self.time = 0

    def shoot(self):
        self.pos[0] += math.cos(self.direction) * self.time
        self.pos[1] -= math.sin(self.direction) * self.time
        self.time += 0.5

player1 = Player()

bullets = []
pos = (250, 250)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet())

    keys = pygame.key.get_pressed()
    player1.rotate(keys, pygame.K_LEFT, pygame.K_RIGHT)       

    for bullet in bullets[:]:
        bullet.shoot()
        if not window.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)

    window.fill(0)
    window.blit(player1.rotated_player, player1.rotated_player.get_rect(center=player1.pos))
    for bullet in bullets:
        window.blit(bullet.rotated_bullet, bullet.rotated_bullet.get_rect(center=bullet.pos))
    pygame.display.flip()