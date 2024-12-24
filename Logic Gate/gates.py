import pygame

pygame.init()

TILE = 25
button_size = TILE*2
line_length = TILE*2

#images and asserts
red_button_image = pygame.image.load("img/red_b.png")
red_button_image = pygame.transform.scale(red_button_image,(button_size,button_size))

green_button_image = pygame.image.load("img/green_b.png")
green_button_image = pygame.transform.scale(green_button_image,(button_size,button_size))

and_gate_img = pygame.image.load("img\AND_gate.png")
and_gate_img = pygame.transform.scale(and_gate_img,(TILE*8,TILE*8))

or_gate_img = pygame.image.load("img\OR_gate.png")
or_gate_img = pygame.transform.scale(or_gate_img,(TILE*8,TILE*8))

nor_gate_img = pygame.image.load("img\\NOR_gate.png")
nor_gate_img = pygame.transform.scale(nor_gate_img,(TILE*8,TILE*8))

nand_gate_img = pygame.image.load("img\\NAND_gate.png")
nand_gate_img = pygame.transform.scale(nand_gate_img,(TILE*8,TILE*8))

xor_gate_img = pygame.image.load("img\XOR_gate.png")
xor_gate_img = pygame.transform.scale(xor_gate_img,(TILE*8,TILE*8))

xnor_gate_img = pygame.image.load("img\XNOR_gate.png")
xnor_gate_img = pygame.transform.scale(xnor_gate_img,(TILE*8,TILE*8))

not_gate_img = pygame.image.load("img\\NOT_gate.png")
not_gate_img = pygame.transform.scale(not_gate_img,(TILE*8,TILE*8))

# logic gates 

class NOT_GATE:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.input_button = Button(x*TILE,(y+3)*TILE)
        self.output_button = Button((x+14)*TILE,(y+3)*TILE,side="left")

    def draw(self,screen):
        self.input_button.draw(screen)
        self.output_button.draw(screen)
        screen.blit(not_gate_img,((self.x+4)*TILE,self.y*TILE))

    def handle_event(self,event):
        self.input_button.handle_event(event)

    def logic(self):
        if self.input_button.state:
            self.output_button.state = False
        else:
            self.output_button.state = True


# ALL 2 input Gates
class Gate_2I:
    
    def __init__(self,x,y,gate_name):
        self.x = x
        self.y = y
        self.input_button_1 = Button(x*TILE,(y+1)*TILE)
        self.input_button_2 = Button(x*TILE,(y+5)*TILE)
        self.output_button = Button((x+14)*TILE,(y+3)*TILE,side="left")
        self.gate_name = gate_name
        self.image = self.__get_image()

    def __get_image(self):
        if self.gate_name == "and":
            return and_gate_img
        elif self.gate_name == "or":
            return or_gate_img
        elif self.gate_name == "xor":
            return xor_gate_img
        elif self.gate_name == "nor":
            return nor_gate_img
        elif self.gate_name == "xnor":
            return xnor_gate_img
        elif self.gate_name == "nand":
            return nand_gate_img

    def draw(self,screen):
        self.input_button_1.draw(screen)
        self.input_button_2.draw(screen)
        self.output_button.draw(screen)
        screen.blit(self.image,((self.x+4)*TILE,self.y*TILE))

    def handle_event(self,event):
        self.input_button_1.handle_event(event)
        self.input_button_2.handle_event(event)

    def logic(self):
        if self.gate_name == "and":
            if self.input_button_1.state and self.input_button_2.state:
                self.output_button.state = True
            else:
                self.output_button.state = False

        elif self.gate_name == "or":
            if self.input_button_1.state or self.input_button_2.state:
                self.output_button.state = True
            else:
                self.output_button.state = False

        elif self.gate_name == "xor":
            if self.input_button_1.state != self.input_button_2.state:
                self.output_button.state = True
            else:
                self.output_button.state = False

        elif self.gate_name == "xnor":
            if self.input_button_1.state == self.input_button_2.state:
                self.output_button.state = True
            else:
                self.output_button.state = False

        elif self.gate_name == "nor":
            if not(self.input_button_1.state or self.input_button_2.state):
                self.output_button.state = True
            else:
                self.output_button.state = False

        if self.gate_name == "nand":
            if not(self.input_button_1.state and self.input_button_2.state):
                self.output_button.state = True
            else:
                self.output_button.state = False

#functions and classes
class Button:

    def __init__(self, x, y,initial_state=False,side="right"):
        self.x = x
        self.y = y
        self.state = initial_state
        self.true_image = green_button_image
        self.false_image = red_button_image
        self.image = self.true_image if self.state else self.false_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.line = Line(self,side)

    def draw(self, screen):
        self.image = self.true_image if self.state else self.false_image
        screen.blit(self.image, (self.x, self.y))
        self.line.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.state = not self.state

class Line:

    def __init__(self,button,side):
        self.side = side
        self.length = line_length
        self.width = button_size//5
        self.button = button
        self.state = self.button.state
        self.color = (40,207,138) if self.state else (0,0,0)
        self.side_chose(side)
    
    def side_chose(self,side):
        if side == "right":
            self.start_pos = (self.button.x + button_size ,self.button.y + (button_size//2))
            self.end_pos = (self.start_pos[0]+line_length,self.start_pos[1])
        elif side == "left":
            self.start_pos = (self.button.x ,self.button.y + (button_size//2))
            self.end_pos = (self.start_pos[0]-line_length,self.start_pos[1])
        elif side == "top":
            self.start_pos = (self.button.x + (button_size//2) ,self.button.y)
            self.end_pos = (self.start_pos[0],self.start_pos[1]-line_length)
        elif side == "bottom":
            self.start_pos = (self.button.x + (button_size//2) ,self.button.y+button_size)
            self.end_pos = (self.start_pos[0],self.start_pos[1]+line_length)

    def draw(self,screen):
        self.state = self.button.state
        self.color =  (40,207,138) if self.state else (0,0,0)
        pygame.draw.line(screen,self.color,self.start_pos,self.end_pos,self.width)