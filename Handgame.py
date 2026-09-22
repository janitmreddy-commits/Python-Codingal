import random
import pygame
class Button():
    def __init__(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked(self,pos):
        self.pos = pygame.mouse.get_pos()
       if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.pos[1] < self.y +self.height:
                return True
            return False
class RpsGame():
         def __init__(self):
              pygame.init()

              self.screen = pygame.dispaly.set_mode((960,640))
              pygame.dispaly.set_caption("RPS Smasher")

              self.bg = pygame.image.load("background.jpg")
              self.r_btn = pygame.image.load("r_button.png").convert_alpha
              self.p_btn = pygame.image.load("r_button.png").convert_alpha
              self.s_btn = pygame.image.load("r_button.png").convert_alpha

              self.choose_rock = pygame.image.load("rock.png").convert_alpha
              self.paper_rock = pygame.image.load("paper.png").convert_alpha
              self.choose_scissors =pygame.image.load("scissors.png")..convert_alpha


              self.screen.blit(self.bg, (0, 0))
              self.screen.blit(self.r_btn, (20, 500))
              self.screen.blit(self.p_btn, (330, 500))
              self.screen.blit(self.s_btn, (640, 500))

              self.rock_bnt = Button(30,520,(30,520),300,140)
              self.paper_bnt = Button(340,520,(340,520),300,140)
              self.scissors_bnt = Button(640,520,(640,520),300,140)

              self.font = pygame.font.Font(('Splatch.ttf'),90)
              self.text = self.font.render(f"",True,(255,255,255))

              self.pl_score = 0
              self.pl_score = 0

          def player(self):
              if self.rock_bnt.clicked(30):    

                

