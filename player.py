import pygame

class macchina:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('imageprog/carplayer2.npg')
        self.image = pygame.transform.scale(self.image, size)
        self.vel = [0,0]
        
        self.moving_right = False
        self.moving_left = False

        self.vel_orizz = 5
        self.falling = False
        self.forza_jump = 10

    def move_right(self):
        self.moving_right = True
    
    def stop_moving_right(self):
        self.moving_right = False

    def move_left(self):
        self.moving_left = True
    
    def stop_moving_left(self):
        self.moving_left = False
