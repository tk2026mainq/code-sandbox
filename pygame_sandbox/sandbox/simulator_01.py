import pygame

#screen
screen_title = "Pygame Sandbox - Simulator 01"
screen_width = 800
screen_height = 600

# objects
class Player:
    def __init__(self, x, y):
        #shape (circle)
        self.radius = 25
        player_color_0 = (0, 255, 0)  # Green color

        #position
        self.x = x
        self.y = y

        #max position
        self.max_x = screen_width - self.radius
        self.max_y = screen_height - self.radius

        #speed
        self.speed_x = 0
        self.speed_y = 0
        self.move_speed = 200  # pixels per second

        #acceleration
        self.acceleration_x = 0.0  # pixels per second squared
        self.acceleration_y = 0.0  # pixels per second squared

    def update(self, dt, keys):

        # Handle player input
        self.speed_x = 0
        self.speed_y = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speed_x -= self.move_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speed_x += self.move_speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed_y -= self.move_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speed_y += self.move_speed

        # Update player position
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt
        # Keep player within screen bounds
        self.x = max(0, min(self.x, self.max_x))
        self.y = max(0, min(self.y, self.max_y))

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), 25)

def main():
    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(screen_title)
    clock = pygame.time.Clock()

    #create player
    player = Player(screen_width // 2, screen_height - 50)


    #game loop
    running = True
    runtime = 0.0  # Initialize runtime variable
    while running:
        #delta time
        dt_ms = clock.tick(60)  # Limit the frame rate to 60 FPS
        dt_seconds = dt_ms / 1000.0  # Convert milliseconds to seconds
        runtime += dt_seconds  # Update runtime

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #update game state
        keys = pygame.key.get_pressed()
        player.update(dt_seconds, keys)
        #draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        player.draw(screen)  # Draw the player

        #update the display
        pygame.display.flip()

        print(f"[ LOG runtime: {runtime:.2f} seconds ]  Delta time: {dt_seconds:.4f} seconds    ") 

    pygame.quit()

if __name__ == "__main__":
    main()
