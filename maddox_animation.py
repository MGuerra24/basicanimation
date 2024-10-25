def main():
    import pygame
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Floatin'")
        
    water = pygame.image.load("water.png")
    water = pygame.transform.scale(water, (640,480))
    
    floatie = pygame.image.load("floatie.png")
    floatie = floatie.convert_alpha()
    floatie = pygame.transform.scale(floatie, (100, 100))
    floatie_x = 0
    floatie_y = 200
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing :
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        floatie_x += 5
        if floatie_x > screen.get_width():
            floatie_x = 0
        
        screen.blit(water, (0,0))
        screen.blit(floatie, (floatie_x, floatie_y))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()