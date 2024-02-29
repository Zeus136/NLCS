#them thu vien pygame
import math
import pygame


# truy cap toi toa do chinh
from pygame.locals import *


#khoi tao thu vien pygame de truy cap cac ham trong pygame
pygame.init()


#khoi tao cua so game voi win la mot lop co kich thuoc bang cua so game va nam o cuoi cung cua game
win = pygame.display.set_mode((650, 800))


#dat tieu de
pygame.display.set_caption("demo")


#khoi tao cac bien toan cuc
"""
  chieu cua X tu trai sang phai
  chieu cua y tu tren xuon duoi
"""
x = 50
y = 425
height = 60  #chieu cao cua vat the
weight = 40  #chieu rong cua vat the
vel = 5      #bien luu do dich chuyen
jump = False #luu thong tin cua mot su kien
jump_count = 10 
fps = 60
clock = pygame.time.Clock()

#khoi tao cac bien tro choi
ground_scroll = 0
bg_scroll = 0
pipe_gap = 150
scroll_speed = 4


#khoi tao background
bg =  pygame.image.load('IMG/bg.png')
bg_width, bg_height = bg.get_size()
scale_bg = pygame.transform.scale(bg, (bg_width/1.2, bg_height/1.2))
ground = pygame.image.load('IMG/ground.png')
ground_width, ground_height = ground.get_size()
tiles = math.ceil(500/bg_width) + 1

  #tao lop bird
class bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f'IMG/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):

		#handle the animation
		self.counter += 1
		flap_cooldown = 6

		if self.counter > flap_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
		self.image = self.images[self.index]
    
    
bird_group = pygame.sprite.Group()
flappy = bird(100, int(800/2))
bird_group.add(flappy)

#Cac ham chinh trong game
run = True
while run: 
  clock.tick(fps)
  #ve background game
  win.blit(scale_bg, (0,0))
  win.blit(ground, (ground_scroll, bg_height/1.2))
  ground_scroll-=scroll_speed
  if abs(ground_scroll) >= ground_width - 650:
    ground_scroll = 0
  pygame.time.delay(10) #thoi gian phan hoi
  
  bird_group.draw(win) 
  bird_group.update()
  # #bat su kien:
  for event in pygame.event.get(): 
    #cac su kien duoc bat dan den cac hanh dong
    if event.type == pygame.QUIT: # su kien bat duoc chinh la nguoi dung an dau X thoat cua so 
      run = False #gan lai gia tri cua bien run
  #   elif event.type == pygame.MOUSEBUTTONDOWN:
  #     jump = True 
      
  # keys = pygame.key.get_pressed()

  # if keys[pygame.K_LEFT] and x > vel:
  #   x -= vel
  # if keys[pygame.K_RIGHT] and x < 500 - weight - vel:
  #   x += vel
  # if not(jump):
  #   if keys[pygame.K_UP] and y > vel:
  #     y -= vel
  #   if keys[pygame.K_DOWN] and y < 500 - height - vel:
  #     y += vel
  #   if keys[pygame.K_SPACE]:
  #     jump = True
  # else:
  #   if jump_count >= -10:
  #     neg = 1
  #     if(jump_count < 0):
  #       neg = -1
  #     y -= (jump_count ** 2) / 2 * neg
  #     jump_count -= 1
  #   else:
  #     jump = False
  #     jump_count = 10
  # # win.fill(bg)
  

  # pygame.draw.rect(win, (255, 0, 0), (x, y, weight, height))
  pygame.display.update()
pygame.quit()
  