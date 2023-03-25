import pygame as p
import sys
import math

p.init()
p.font.init()
p.display.set_caption("Fourier Series")

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 700
HEIGHT = 500
run = True

toggle = True
points = []
angle = 0
n = 1

font = p.font.SysFont("comicsans", 30)
clock = p.time.Clock()
screen = p.display.set_mode((WIDTH, HEIGHT))


def fourier(theta):
    global angle
    series = 0
    for x in range(n):
        x = 2 * x + 1
        num = (4 * math.sin(x * ((theta * math.pi) / 180))) / (x * math.pi)
        series += num
    points.insert(0, series)


def circle(theta):
    series = [0, 0]
    if toggle:
        p.draw.circle(screen, WHITE, (200, 250), 100, 1)
    for x in range(n):
        x_point = 100 / (2 * x + 1) * math.cos((2 * x + 1) * (theta * math.pi) / 180)
        y_point = 100 / (2 * x + 1) * math.sin((2 * x + 1) * (theta * math.pi) / 180)
        series[0] += x_point
        series[1] += y_point
        if x >= 1 and toggle:
            p.draw.circle(screen, WHITE, (200 + series[0] - x_point, 250 + series[1] - y_point), 100 / (2 * x + 1), 1)
        p.draw.circle(screen, BLUE, (200 + series[0], 250 + series[1]), 4)
    p.draw.line(screen, RED, (200 + series[0], 250 + series[1]), (350, 250 + 25 * math.pi * points[0]))


def draw():
    global angle, n
    screen.fill(BLACK)
    text = font.render("n = " + str(n), True, WHITE)
    screen.blit(text, (10, 10))
    p.draw.line(screen, GREEN, (350, 250 + 100), (350, 250 - 100), 1)
    p.draw.line(screen, GREEN, (350, 250), (700, 250), 1)
    for x, point in enumerate(points):
        p.draw.circle(screen, WHITE, (x * 7 + 350, 250 + 25 * math.pi * point), 2)

    circle(angle)

    angle += 5
    p.display.update()


def main():
    global n, toggle
    while run:
        clock.tick(20)
        fourier(angle)
        draw()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_UP:
                    n += 1
                if event.key == p.K_DOWN:
                    n -= 1
                if event.key == p.K_t:
                    toggle = not toggle
                if event.key == p.K_r:
                    n = 1


main()
