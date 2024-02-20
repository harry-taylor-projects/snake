import pygame
import random

# initialise game
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
rows = [pygame.Rect(0, 50 * i + 50, 1000, 1) for i in range(19)]
columns = [pygame.Rect(50 * i + 50, 0, 1, 1000) for i in range(19)]

# initialise snake
snake_direction = 'right'
snake_head = [6, 5]
snake_body = [[5, 5], [4, 5]]
apple = [12, 5]

# running game
run = True
while run:

    # draw grids
    screen.fill((0, 0, 0))
    for row in rows:
        pygame.draw.rect(screen, (255, 255, 255), row)
    for column in columns:
        pygame.draw.rect(screen, (255, 255, 255), column)

    # draw snake
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(snake_head[0]*50 + 1, snake_head[1]*50 + 1, 49, 49))
    for body in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(body[0]*50 + 1, body[1]*50 + 1, 49, 49))

    # draw apple
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple[0] * 50 + 1, apple[1] * 50 + 1, 49, 49))

    # move snake body
    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i] = snake_body[i-1].copy()
    snake_body[0] = snake_head.copy()

    # change direction of snake if key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and snake_direction != 'right':
        snake_direction = 'left'
    if key[pygame.K_d] and snake_direction != 'left':
        snake_direction = 'right'
    if key[pygame.K_w] and snake_direction != 'down':
        snake_direction = 'up'
    if key[pygame.K_s] and snake_direction != 'up':
        snake_direction = 'down'

    # move snake head in direction of movement
    if snake_direction == 'left':
        snake_head[0] -= 1
    elif snake_direction == 'right':
        snake_head[0] += 1
    elif snake_direction == 'up':
        snake_head[1] -= 1
    elif snake_direction == 'down':
        snake_head[1] += 1

    # eating the apple
    if snake_head == apple:
        snake_body.extend([snake_body[len(snake_body)-1]])

        # move apple to empty square
        square_taken = True
        while square_taken:
            apple[0] = random.randrange(0, 20)
            apple[1] = random.randrange(0, 20)
            square_taken = False
            if apple == snake_head:
                square_taken = True
            else:
                for body in snake_body:
                    if apple == body:
                        square_taken = True

    # stop game if snake is out of bounds
    if min(snake_head) < 0 or max(snake_head) > 19:
        run = False

    # stop game if snake collides with itself
    for body in snake_body:
        if snake_head == body:
            run = False

    # stop the game if user closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    # 10 fps
    pygame.time.wait(100)

pygame.quit()
