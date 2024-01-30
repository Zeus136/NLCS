#them thu vien pygame
import math
import pygame
# truy cap toi toa do chinh
from pygame.locals import *
#khoi tao thu vien pygame de truy cap cac ham trong pygame
pygame.init()
#khoi tao cua so game voi win la mot lop co kich thuoc bang cua so game va nam o cuoi cung cua game
win = pygame.display.set_mode((500,500))
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
pipe_gap = 150
scroll_speed = 4


#khoi tao background
bg =  pygame.image.load('IMG/background.png').convert()
bg_width, bg_height = bg.get_size()
scale_bg = pygame.transform.scale(bg, (bg_width*2, bg_height*2))
ground = pygame.image.load('IMG/ground.png')
tiles = math.ceil(500/bg_width) + 1
#Cac ham chinh trong game
run = True
while run: 
  clock.tick(fps)
  #ve background game
  for i in range(0,tiles):
    win.blit(scale_bg, (i*bg_width+ground_scroll,0))
  win.blit(ground, (ground_scroll, bg_height*1.9))
  ground_scroll-= scroll_speed
  if abs(ground_scroll) > bg_width :
    ground_scroll = 0
  pygame.time.delay(50) #thoi gian phan hoi
  #bat su kien nguoi
  for event in pygame.event.get(): 
    #cac su kien duoc bat dan den cac hanh dong
    if event.type == pygame.QUIT: # su kien bat duoc chinh la nguoi dung an dau X thoat cua so 
      run = False #gan lai gia tri cua bien run
    elif event.type == pygame.MOUSEBUTTONDOWN:
      jump = True 
      
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and x > vel:
    x -= vel
  if keys[pygame.K_RIGHT] and x < 500 - weight - vel:
    x += vel
  if not(jump):
    if keys[pygame.K_UP] and y > vel:
      y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
      y += vel
    if keys[pygame.K_SPACE]:
      jump = True
  else:
    if jump_count >= -10:
      neg = 1
      if(jump_count < 0):
        neg = -1
      y -= (jump_count ** 2) / 2 * neg
      jump_count -= 1
    else:
      jump = False
      jump_count = 10
  # win.fill(bg)
  pygame.draw.rect(win, (255, 0, 0), (x, y, weight, height))
  pygame.display.update()
pygame.quit()
  