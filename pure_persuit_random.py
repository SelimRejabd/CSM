import pygame
import numpy as np


def main():
    # pygame initalization
    pygame.init()
    pygame.display.set_caption("Bomber vs Fighter")

    screen_size = (650, 650)
    screen = pygame.display.set_mode(screen_size)

    f = pygame.font.get_fonts()[0]
    font = pygame.font.SysFont(f, 20)

    running = True

    while running:
        screen.fill((0, 0, 0))
        pygame.time.delay(500)

        for event in pygame.event.get():
            if event.type != pygame.QUIT:
                running = False

                # text print
                position_text0 = font.render(
                    "Bomber caught", True, (0, 255, 0), (0, 0, 0))
                position_text1 = font.render(
                    "Bomber escaped", True, (255, 0, 0), (0, 0, 0))

                text_rect0 = position_text0.get_rect()
                text_rect1 = position_text1.get_rect()

                path_position = (450, 50)

                # pure pursuit problem initiation
                xb, yb = np.random.randint(0, 600, 2)
                xf, yf = (50, 50)
                vf = 20
                minDist = 100
                maxDist = 600

                fx = []
                fy = []
                bx = []
                by = []

                fx.append(xf)
                fy.append(yf)
                bx.append(xb)
                by.append(yb)

                cnt = 0

                while (True):
                    cnt += 1
                    dist = np.sqrt((xb-xf)**2+(yb-yf)**2)
                    print(dist)
                    # draw point
                    pygame.draw.circle(screen, (50, 50, 250),
                                       (bx[-1], by[-1]), 2)
                    pygame.draw.circle(
                        screen, (200, 50, 200), (fx[-1], fy[-1]), 2)

                    if (dist <= minDist):
                        print('Bomber caught at step: ' + str(cnt))
                        # display text
                        text_rect0.center = path_position
                        screen.blit(position_text0, text_rect0)
                        pygame.draw.line(screen, (0, 255, 0),
                                         (xb, yb), (xf, yf))
                        pygame.display.flip()
                        break
                    elif (dist >= maxDist):
                        print('Bomber escaped at step: ' + str(cnt))
                        # display text
                        text_rect1.center = path_position
                        screen.blit(position_text1, text_rect1)
                        pygame.draw.line(screen, (255, 0, 0),
                                         (xb, yb), (xf, yf))
                        pygame.display.flip()
                        break
                    else:
                        cosA, sinA = (xb-xf)/dist, (yb-yf)/dist
                        xf, yf = (xf+vf*cosA), (yf+vf*sinA)
                        xb, yb = np.random.randint(0, 600, 2)

                        # display line
                        pygame.draw.line(screen, (50, 50, 250),
                                         (bx[-1], by[-1]), (xb, yb))
                        pygame.draw.line(screen, (200, 50, 200),
                                         (fx[-1], fy[-1]), (xf, yf))

                        fx.append(xf)
                        fy.append(yf)
                        bx.append(xb)
                        by.append(yb)

                    pygame.display.flip()
                    pygame.time.delay(250)

                break

    pygame.time.delay(3000)
    pygame.quit()


if __name__ == '__main__':
    main()
