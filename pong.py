import pygame
game_display = pygame.display.set_mode((500, 400)) # game_display is our surface

def main():
    pygame.init() # Initializes paygame
    def screen(): 
        # Setting up the screen
        pygame.display.set_mode((500, 400))
        pygame.display.set_caption("Pong")
        pygame.display.get_surface()
        
       
    screen() 
    
    var_game = Game(game_display) 
    var_game.play()
    pygame.quit()
    
class Game: 
        def __init__(self, surface): 
                # Initializes game class
                self.surface = surface
                self.bg_color = pygame.Color('black')
                self.close_clicked = False
                self.continue_game = True 
                self.var_ball = Ball((255,255,255), 5, [250,200], [2,1] , game_display) # Creates a ball instance with respective parameters in the middle of the screen (Check below to see the Ball class)
                self.var_paddle_1 = Paddle(game_display, 100, 180, 40, 10, (255, 255, 255), 1) # Creates the first paddle instance with respective parameters (Check below to see the Paddle class)
                self.var_paddle_2 = Paddle(game_display, 400, 180, 40, 10, (255, 255, 255), 1) # Creates the second paddle instance with respective parameters (Check below to see the Paddle class)
                self.player1_score = 0
                self.player2_score = 0
                self.FPS = 60
                self.game_Clock = pygame.time.Clock()
                self.a = False # This 4 lines of code to see if user pressed any of these buttons. We are going to use this variables later
                self.q = False
                self.p = False
                self.l = False
                
        def draw(self):
                # Draws game content
                self.surface.fill(self.bg_color)
                self.var_paddle_1.draw()        
                self.var_paddle_2.draw()
                self.var_ball.draw()                
                self.draw_score_board_p1()
                self.draw_score_board_p2()                
                pygame.display.update()
                
        def play(self):
            # This is our main play method which continues until game ends or user decided to quit the game
            while self.close_clicked == False:
                self.draw()
                self.decide_continue()
                self.handle_events()
                if self.continue_game == True:
                    self.update()
                self.game_Clock.tick(self.FPS)
         
        def decide_continue(self):
            # Checks if any user hit score 11. Game ends when one of the players does
            if self.player1_score == 11 or self.player2_score == 11:
                self.close_clicked = True 
            
        def handle_events(self): 
            # Handles all events happen in the game
           events = pygame.event.get()
           for event in events:
               if event.type == pygame.QUIT: # Checks if user clicked "X" button to quit the game
                   self.close_clicked = True 
               if event.type == pygame.KEYDOWN: ### We use pygame.KEYDOWN to check if user pressed that button which in the first if statements is "q" if user does, then self.q becomse True (We will use it later on)
                   if event.key == pygame.K_q:
                       self.q = True 
               if event.type == pygame.KEYUP: ### We use pygame.KEYUP to check if user releases that button
                   if event.key == pygame.K_q:
                        self.q = False
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_a:
                       self.a = True
               if event.type == pygame.KEYUP:
                   if event.key == pygame.K_a:
                       self.a = False
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_p:
                       self.p = True
               if event.type == pygame.KEYUP:
                   if event.key == pygame.K_p:
                       self.p = False
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_l:
                       self.l = True
               if event.type == pygame.KEYUP:
                   if event.key == pygame.K_l:
                        self.l = False
                   
                       
            
                   
        def score1(self):
            # Player 1 scores when the ball hits right side of the screen    
            if self.var_ball.center[0] >= 495:
                self.player1_score += 1

        def score2(self):
            # Player 2 scores when the ball hits right side of the screen   
            if self.var_ball.center[0] <= 5:
                self.player2_score += 1

        def draw_score_board_p1(self):
            # Draws the scoreboard's player1 side according to self.player1_score      
            font_color = pygame.Color("white")
            font_bg = pygame.Color("black")
            font = pygame.font.SysFont("arial", 50)
            text_img   = font.render(str(self.player1_score), True, font_color, font_bg)     
            text_pos   = (30,10)
            self.surface.blit(text_img, text_pos)
            
    
        def draw_score_board_p2(self):
            # Draws the scoreboard's player2 side according to self.player2_score
            font_color = pygame.Color("white")
            font_bg = pygame.Color("black")
            font = pygame.font.SysFont("arial", 50)
            text_img   = font.render(str(self.player2_score), True, font_color, font_bg)     
            text_pos   = (435,10)
            self.surface.blit(text_img, text_pos)
            
        def update(self):
            # Updates the game

            self.var_ball.move() # Moves the ball 
            self.score1()
            self.score2()
            self.collision_ball_paddle() # Ball counces when it hits the screen or one of the paddles from front (Check collision_ball_paddle() method)
            if self.var_paddle_1.rect.top <= 0:
                # If paddle is touching the ceiling, it can't go up anymore. Other if statements below are similar
                self.q = False
            if self.q == True:
                self.var_paddle_1.move(0)
                
            if self.var_paddle_1.rect.top + 40 >= 400:
                self.a = False
            if self.a == True:
                self.var_paddle_1.move(1)
            
            if self.var_paddle_2.rect.top <= 0:
                self.p = False
            if self.p == True:
                self.var_paddle_2.move(0)
                
            if self.var_paddle_2.rect.top + 40 >= 400:
                self.l = False
            if self.l == True:
                self.var_paddle_2.move(1)
                
        def collision_ball_paddle(self):
            # Detects if ball touched any of the paddles from front or to any border of the screen. Ball changed directions if it hits any of them
            if self.var_paddle_1.collidepoint(self.var_ball.center)  and self.var_ball.velocity[0] < 0:
                self.var_ball.velocity[0] = self.var_ball.velocity[0] * -1
                        
            if self.var_paddle_2.collidepoint(self.var_ball.center) and self.var_ball.velocity[0] > 0:
                self.var_ball.velocity[0] = self.var_ball.velocity[0] * -1            
            
            
                
class Paddle:
    def __init__(self, surface, top, left,  height, width, color, velocity):
        # Initializes our paddle class
        self.surface = surface
        self.color = color   
        self.rect = pygame.Rect(top, left, width, height)
        self.velocity = velocity
        self.top = top
        self.left = left
        
    
    def draw(self):
        # Draws the paddle
        pygame.draw.rect(self.surface, self.color, self.rect)
            
    def collidepoint(self, center_ball):
        # Checks if ball collided with this paddle
        return self.rect.collidepoint(center_ball)
    
    def move(self, direction):
        # Moves the paddle up if the direction is 0 and to down if the direction is 1
        if direction == 1:
            self.rect = self.rect.move(0, self.velocity)
            
        if direction == 0:
            self.rect = self.rect.move(0, -self.velocity)
    
                      

class Ball:
    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
        # Initializes the ball class
        self.color = ball_color
        self.radius = ball_radius
        self.center = ball_center
        self.velocity = ball_velocity
        self.surface = surface
                       
    def draw(self):
        # Draws the ball to screen
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
    
    def move(self):
            # Moves the ball with respective velocity (User can change the velocity however they like while initializing the Ball class   
            for i in range(0,2):
                        self.center[i] = (self.center[i] + self.velocity[i])
                         
            if self.center[0] <= 5 or self.center[0] >= 495:
                        self.velocity[0] = self.velocity[0] * -1
                    
            if self.center[1] <= 5 or self.center[1] >= 395:
                        self.velocity[1] = self.velocity[1] * -1
                
                         
    
            
main()
        