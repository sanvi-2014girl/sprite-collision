import pygame
import random
#Constants for easier adjustments
SCREEN_WIDTH,SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
#INITIALIZE PYGAME
pygame.init()
#Load and transform the background image
background_image = pygame.transform.scale(pygame.image.load("bge.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
#LOAD FONT OCE AT THE BEGINNING
font = pygame.font.SysFont("Times New Roman",FONT_SIZE)
class Sprite(pygame.sprite.Sprite):
   def __init__(self,color,height,width) :
      super().__init__()
      self.image = pygame.Surface([width,height])
      self.image.fill(pygame.Color('dodgerblue'))#Background color of sprite
      pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
      self.rect = self.image.get_rect()
   def move(self, x_change, y_change):
      self.rect.x = max(
         min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width),0)
      self.rect.y = max(
         min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height),0)
#setup
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()
#Create sprites
sprite1 = Sprite(pygame.Color('black'),20,30)
sprite1.rect.x,sprite1.rect.y = random.randint(0,SCREEN_WIDTH-sprite1.rect.width),random.randint(
   0,SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color('red'),20,30)
sprite2.rect.x,sprite2.rect.y = random.randint(0,SCREEN_WIDTH-sprite2.rect.width),random.randint(
   0,SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)
sprite3 = Sprite(pygame.Color('pink'),20,30)
sprite3.rect.x,sprite3.rect.y = random.randint(0,SCREEN_WIDTH-sprite3.rect.width),random.randint(
   0,SCREEN_HEIGHT - sprite3.rect.height)
all_sprites.add(sprite3)
#Game loop control variables
running,won = True,False
clock = pygame.time.Clock()
#Main game loop
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
         running = False
   if  not won:
      keys = pygame.key.get_pressed()
         