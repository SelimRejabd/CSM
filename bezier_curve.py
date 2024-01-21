import pygame
import time

def main():
    pygame.init()
    pygame.display.set_caption('Bezier Curve')

    screen_size = (1000, 600)
    screen = pygame.display.set_mode(screen_size)

    speed = 0.004
    f = pygame.font.get_fonts()[0]
    font = pygame.font.SysFont(f, 32)

    position_text0 = font.render('P0', True, (255, 255, 255), (0, 0, 0))
    position_text1 = font.render('P1', True, (255, 255, 255), (0, 0, 0))
    position_text2 = font.render('P2', True, (255, 255, 255), (0, 0, 0))
    position_text3 = font.render('P3', True, (255, 255, 255), (0, 0, 0))

    text_rect0 = position_text0.get_rect()
    text_rect1 = position_text1.get_rect()
    text_rect2 = position_text2.get_rect()
    text_rect3 = position_text3.get_rect()

    path_position = [(100.0, 500.0), (200.0, 100.0), (600.0, 80.0), (650.0, 410)]

    t = 0
    running = True

    while running:
        screen.fill((10, 20, 10))
        pygame.time.delay(500)

        P0 = path_position[0]
        P1 = path_position[1]
        P2 = path_position[2]
        P3 = path_position[3]

        for event in pygame.event.get():
            if event.type != pygame.QUIT:
                running = False

                while t < 1:
                    t += speed
                    P0_x = pow((1-t), 3) * P0[0]
                    P0_y = pow((1-t), 3) * P0[1]
                    P1_x = 3 * pow((1-t), 2) * t * P1[0]
                    P1_y = 3 * pow((1-t), 2) * t * P1[1]
                    P2_x = 3 * (1-t) * pow(t, 2) * P2[0]
                    P2_y = 3 * (1-t) * pow(t, 2) * P2[1]
                    P3_x = pow(t, 3) * P3[0]
                    P3_y = pow(t, 3) * P3[1]
                    sum = ((P0_x + P1_x + P2_x + P3_x), (P0_y + P1_y + P2_y + P3_y))
                    x, y = sum
                    text_rect0.center = P0
                    text_rect1.center = P1
                    text_rect2.center = P2
                    text_rect3.center = P3
                    screen.blit(position_text0, text_rect0)
                    screen.blit(position_text1, text_rect1)
                    screen.blit(position_text2, text_rect2)
                    screen.blit(position_text3, text_rect3)
                    pygame.draw.line(screen, (255, 0, 0), P0, P1)
                    pygame.draw.line(screen, (0, 255, 0), P1, P2)
                    pygame.draw.line(screen, (0, 0, 255), P2, P3)
                    pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 1)
                    pygame.display.flip()
                    pygame.time.delay(10)

    pygame.time.delay(1500)
    pygame.quit()

if __name__ == '__main__':
    main()