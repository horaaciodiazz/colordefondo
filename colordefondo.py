import pygame, time

WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))

def lerp(start, end, steps):
    colors = []
    for i in range(steps):
        t = (1 / steps) * i 
        r = (1 - t) * start[0] + t * end[0]
        g = (1 - t) * start[1] + t * end[1]
        b = (1 - t) * start[2] + t * end[2]
        colors.append((r, g, b))

    return colors

def main():
    colors = lerp((0, 20, 50), (255, 255, 255), 100)
    totalTime = 10
    duration = totalTime / len(colors)
    i = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        color = colors[i]
        window.fill(color)
        time.sleep(duration)
        i += 1

        pygame.display.update()

main()

