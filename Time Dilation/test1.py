import pygame

pygame.init()

#for screen/window basic
WIDTH = 900
HEIGHT = 600
RES = WIDTH,HEIGHT
win = pygame.display.set_mode(RES)
pygame.display.set_caption("TIME DILATION - TEST 1")
clock = pygame.Clock()
FPS = 30

speed_of_light = 1 # just for example 3 pixel per frame

# MATHS
# here is FPS = 30 so light travel 30 x 1 = 30 PIXEL/SECOND

def circle_rect_collision(circle_center, circle_radius, rect):
    """Check if a circle and a rectangle are colliding."""
    closest_x = max(rect.left, min(circle_center[0], rect.right))
    closest_y = max(rect.top, min(circle_center[1], rect.bottom))
    
    distance_x = circle_center[0] - closest_x
    distance_y = circle_center[1] - closest_y
    
    return (distance_x ** 2 + distance_y ** 2) < (circle_radius ** 2)

def main():

    end_point_1 = [450,200]
    end_point_2 = [450,200]

    rect_1 = pygame.draw.line(win,(255,255,255),(450,200),tuple(end_point_1),10)
    rect_2 = pygame.draw.line(win,(255,255,255),(450,200),tuple(end_point_2),10)

    circle_1 = pygame.draw.circle(win,(0,0,255),(100,200),20)
    circle_2 = pygame.draw.circle(win,(0,0,255),(800,200),20)

    #for gameloop
    while True:

        #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Foe update endpoint in every Frame
        if not circle_rect_collision(circle_1.center,20,rect_1):
            end_point_1[0] += speed_of_light

        if not circle_rect_collision(circle_2.center,20,rect_2):
            end_point_2[0] -= speed_of_light
            
        # For Background color
        win.fill((50,50,50))

        pygame.draw.circle(win,(255,255,0),(450,200),20)

        rect_1 = pygame.draw.line(win,(255,255,255),(450,200),tuple(end_point_1),10)
        rect_2 = pygame.draw.line(win,(255,255,255),(450,200),tuple(end_point_2),10)

        circle_1 = pygame.draw.circle(win,(0,0,255),(100,200),20)
        circle_2 = pygame.draw.circle(win,(0,0,255),(800,200),20)

        pygame.display.flip()
        clock.tick(FPS)

if __name__=="__main__":
    main()
    pygame.quit()
    exit()