import pygame
import gates as g

pygame.init()

#for screen/window basic
WIDTH = 600
HEIGHT = 400
RES = WIDTH,HEIGHT
win = pygame.display.set_mode(RES)
pygame.display.set_caption("All Logic Gates")
clock = pygame.Clock()
FPS = 30
font = pygame.font.Font(None,36)

# Functions and Classes
class Tab:
    def __init__(self, x, y, width, height, text, image_path, font, default_color, selected_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width // 2, height // 3))  # Scale the image to fit the tab
        self.font = font
        self.default_color = default_color
        self.selected_color = selected_color
        self.color = default_color
        self.is_selected = False

    def draw(self, screen):
        # Draw the tab background with specific corner radius
        pygame.draw.rect(screen, self.color, self.rect, border_top_left_radius=10, border_top_right_radius=10)
        
        # Draw the image
        image_rect = self.image.get_rect(center=(self.rect.centerx, self.rect.y + self.rect.height // 3))
        screen.blit(self.image, image_rect)
        
        # Draw the text
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.y + self.rect.height * 2 // 3 + 10))  # Added padding
        screen.blit(text_surface, text_rect)

    def select(self):
        self.is_selected = True
        self.color = self.selected_color

    def deselect(self):
        self.is_selected = False
        self.color = self.default_color

class NavigationBar:
    def __init__(self, screen_width, screen_height):
        self.tabs = []
        self.selected_index = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def add_tab(self, text, image_path, font, default_color, selected_color):
        tab_width = (self.screen_width // 7) +1
        x = len(self.tabs) * tab_width
        y = self.screen_height - 100  # Double the height of the navigation bar
        tab = Tab(x, y, tab_width, 100, text, image_path, font, default_color, selected_color)  # Height set to 100
        self.tabs.append(tab)

    def draw(self, screen):
        for i, tab in enumerate(self.tabs):
            if i == self.selected_index:
                tab.select()
                tab.rect.y = self.screen_height - 120
                tab.rect.height = 120
            else:
                tab.deselect()
                tab.rect.y = self.screen_height - 100
                tab.rect.height = 100
            tab.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, tab in enumerate(self.tabs):
                if tab.rect.collidepoint(event.pos):
                    self.selected_index = i

    def get_current_gate(self):
        index = self.selected_index
        if index == 0:
            return g.NOT_GATE(4,2)
        elif index == 1:
            return g.Gate_2I(4,2,"and")
        elif index == 2:
            return g.Gate_2I(4,2,"or")
        elif index == 3:
            return g.Gate_2I(4,2,"nand")
        elif index == 4:
            return g.Gate_2I(4,2,"nor")
        elif index == 5:
            return g.Gate_2I(4,2,"xor")
        elif index == 6:
            return g.Gate_2I(4,2,"xnor")
            
def main():
    
    # Gates
    # gate = g.Gate_2I(4,2,"xnor")
    gate = g.NOT_GATE(4,2)

    # Initialize NavigationBar
    nav_bar = NavigationBar(WIDTH,HEIGHT)
    tab_info = [
        ('NOT', 'img//NOT_gate.png'),
        ('AND', 'img/AND_gate.png'),
        ('OR', 'img/OR_gate.png'),
        ('NAND', 'img//NAND_gate.png'),
        ('NOR', 'img//NOR_gate.png'),
        ('XOR', 'img/XOR_gate.png'),
        ('XNOR', 'img/XNOR_gate.png')
    ]
    for text, image_path in tab_info:
        nav_bar.add_tab(text, image_path, font, (118, 120, 131), (22, 187, 119))

    last_index = nav_bar.selected_index

    #for gameloop
    while True:
        
        #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            # for navigation bar event handling
            nav_bar.handle_event(event)

            # for gate button event handling
            gate.handle_event(event)

        # for logic of gate
        gate.logic()

        #for navigation bar at bottom
        current_index = nav_bar.selected_index
        if current_index != last_index:
            gate = nav_bar.get_current_gate()
            last_index = current_index

        # drawing images and background in order
        win.fill((99, 143, 214))

        # for button drawing
        gate.draw(win)

        # for navbar drawing
        nav_bar.draw(win)

        pygame.display.flip()
        clock.tick(FPS)

if __name__=="__main__":
    main()
    pygame.quit()
    exit()