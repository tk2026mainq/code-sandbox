import pygame

# 
screen_width = 800
screen_height = 600

def main():

    # initialize Pygame
    print("Initializing Pygame...")
    pygame.init()
    print("Pygame initialized.")
    clock = pygame.time.Clock()

    # Set up the display
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Sandbox - Draw Things")

    # ball position and speed
    ball_x = screen_width // 2
    ball_y = screen_height // 2
    ball_speed_x = 2
    ball_speed_y = 2

    # player position and speed
    player_x = screen_width // 2
    player_y = screen_height - 50
    player_speed_x = 0
    player_speed_y = 0

    # Main loop
    running = True
    while running:

        dt = clock.tick(60) / 100  # Limit the frame rate to 60 FPS
        player_speed_x = 0
        player_speed_y = 0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_speed_x -=5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_speed_x +=5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_speed_y -=5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_speed_y += 5


        # Update player position
        player_x += player_speed_x * dt
        player_y += player_speed_y * dt
        # Keep player within screen bounds
        player_x = max(0, min(player_x, screen_width - 50))  
        player_y = max(0, min(player_y, screen_height - 50))
        # Update ball position
        if ball_x <= 0 or ball_x >= screen_width:
            ball_speed_x = -ball_speed_x
        if ball_y <= 0 or ball_y >= screen_height:
            ball_speed_y = -ball_speed_y
        ball_x += ball_speed_x * dt
        ball_y += ball_speed_y * dt

        

        # draw the ball
        screen.fill((0, 0, 0))  # Fill the screen with white
        pygame.draw.circle(screen, (200, 200, 200), (ball_x, ball_y), 20)  # Draw a red ball
        pygame.draw.rect(screen, (100, 100, 100), (player_x, player_y, 50, 50))  # Draw a gray player

        pygame.display.flip()  # Update the display

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
