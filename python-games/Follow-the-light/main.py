import pygame
import random

pygame.init()

win = pygame.display.set_mode((600, 640))
pygame.display.set_caption("Follow The Light")
font = pygame.font.SysFont("Arial", 35)
# four boxes
pygame.draw.rect(win, (255, 54, 54), (20, 60, 270, 270))  # red
pygame.draw.rect(win, (54, 255, 54), (20, 360, 270, 270))  # green
pygame.draw.rect(win, (54, 54, 255), (310, 60, 270, 270))  # blue
pygame.draw.rect(win, (255, 255, 54), (310, 360, 270, 270))  # yellow
current_round_label = font.render("Round: 1", True, (255, 255, 255))
win.blit(current_round_label, [250, 10])
pygame.display.update()
# helps decide which box to glow
options = [1, 2, 3, 4]
lost = False
current_round = 1


# randomly picks square to glow and returns which square glowed
def glow():
    to_glow = random.choice(options)
    if to_glow == 1:    # top left
        pygame.draw.rect(win, (127, 127, 127), (20, 60, 270, 270))
    elif to_glow == 2:  # bottom left
        pygame.draw.rect(win, (127, 127, 127), (20, 360, 270, 270))
    elif to_glow == 3:  # top right
        pygame.draw.rect(win, (127, 127, 127), (310, 60, 270, 270))
    else:  # 4          # bottom right
        pygame.draw.rect(win, (127, 127, 127), (310, 360, 270, 270))
    pygame.display.update()
    pygame.time.delay(800)
    pygame.draw.rect(win, (255, 54, 54), (20, 60, 270, 270))
    pygame.draw.rect(win, (54, 255, 54), (20, 360, 270, 270))
    pygame.draw.rect(win, (54, 54, 255), (310, 60, 270, 270))
    pygame.draw.rect(win, (255, 255, 54), (310, 360, 270, 270))
    pygame.display.update()
    pygame.time.delay(300)
    return to_glow


# locates where the click occurred
def spot_clicked(point):
    if 20 <= point[0] <= 290:        # x limit
        if 60 <= point[1] <= 325:
            return 1        # top left
        elif 360 <= point[1] <= 625:
            return 2       # bottom left

    elif 310 <= point[0] <= 575:
        if 60 <= point[1] <= 325:
            return 3       # top right
        elif 360 <= point[1] <= 625:
            return 4      # bottom right
    return 0


# allows program to be closed
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    while True:
        light_order = []    # list to store the order of the light pattern

        for i in range(current_round):
            light_order.append(glow())      # adding the pattern
        user_clicks = []
        print(f"Answer: {light_order}")
        while len(user_clicks) < current_round:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if spot_clicked(event.pos) != 0:
                        user_clicks.append(spot_clicked(event.pos))
        print(f"User Input: {user_clicks}")

        for i in range(len(user_clicks)):
            if user_clicks[0] != light_order[0]:        # checks if the user clicked the same box
                lost = True
                break
            else:
                light_order.pop(0)
                user_clicks.pop(0)
        if lost:
            break
        current_round += 1
        win.fill(pygame.Color("black"), (250, 10, 200, 50))
        current_round_label = font.render("Round: {}".format(current_round), True, (255, 255, 255))
        win.blit(current_round_label, [250, 10])
        pygame.display.update()

    run = False
pygame.quit()
