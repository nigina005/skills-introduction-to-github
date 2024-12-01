import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 400, 500
square_size=20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tet")

# Цвета R,G,B
colors={'O':(255,255,0),
        'I':(0,255,255),
        'Z':(244,4,4),
        'L':(255, 137, 9),
        'J':(255,0,204),
        'T':(192,110,247)}
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 10




TETROMINOES = {
    'I': [
        [[0, 0, 0, 0], 
         [1, 1, 1, 1], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]],
         
        [[0, 0, 1, 0], 
         [0, 0, 1, 0], 
         [0, 0, 1, 0], 
         [0, 0, 1, 0]]
    ],
    'O': [
        [[1, 1], 
         [1, 1]]
    ],
    'T': [
        [[0, 1, 0], 
         [1, 1, 1], 
         [0, 0, 0]],
         
        [[0, 1, 0], 
         [0, 1, 1], 
         [0, 1, 0]],
         
        [[0, 0, 0], 
         [1, 1, 1], 
         [0, 1, 0]],
         
        [[0, 1, 0], 
         [1, 1, 0], 
         [0, 1, 0]]
    ],
    'L': [
        [[0, 0, 1], 
         [1, 1, 1], 
         [0, 0, 0]],
         
        [[0, 1, 0], 
         [0, 1, 0], 
         [0, 1, 1]],
         
        [[0, 0, 0], 
         [1, 1, 1], 
         [1, 0, 0]],
         
        [[1, 1, 0], 
         [0, 1, 0], 
         [0, 1, 0]]
    ],
    'J': [
        [[1, 0, 0], 
         [1, 1, 1], 
         [0, 0, 0]],
         
        [[0, 1, 1], 
         [0, 1, 0], 
         [0, 1, 0]],
         
        [[0, 0, 0], 
         [1, 1, 1], 
         [0, 0, 1]],
         
        [[0, 1, 0], 
         [0, 1, 0], 
         [1, 1, 0]]
    ],
    'Z': [
        [[1, 1, 0], 
         [0, 1, 1], 
         [0, 0, 0]],
         
        [[0, 0, 1], 
         [0, 1, 1], 
         [0, 1, 0]]
    ]
    
}

def get_random_tetromino():
    tetromino_key = random.choice(list(TETROMINOES.keys()))  
    tetromino_state = random.choice(TETROMINOES[tetromino_key])  
    return tetromino_state

def check_collision(game_field,TETROMINOES, start_x, start_y):
    for row_idx,row in enumerate(TETROMINOES):
        for col_idx,value in enumerate(row):
            if value == 1:
                field_x=start_x+col_idx
                field_y=start_y+row_idx
                if field_x<0 or field_x>=len(game_field[0]) or field_y>=len(game_field):
                    return True
                if game_field[field_y][field_x]==1:
                    return True
    return False
                
    


def move_tetromino_down(game_field,TETROMINOES,start_x,start_y):
    new_ind=start_y+1

    if check_collision(game_field,TETROMINOES, start_x,new_ind):
        for row_idx,row in enumerate(TETROMINOES):            
            for col_idx,value in enumerate(row):
                if value == 1:
                    field_x = start_x + col_idx
                    field_y = new_ind + row_idx
                    game_field[field_y][field_x] = 1 
        return game_field, start_x, start_y
            
                

    for row_idx,row in enumerate(TETROMINOES):
        for col_idx,value in enumerate(row):
            if value == 1:
                field_x = start_x + col_idx
                field_y = start_y + row_idx        
                game_field[field_y][field_x] = 0

    for row_idx,row in enumerate(TETROMINOES):
        for col_idx,value in enumerate(row):
            if value == 1:
                field_x = start_x + col_idx
                field_y = new_ind + row_idx
                game_field[field_y][field_x] = 1

    return game_field, start_x, new_ind

#20,19
game_field = [[0 for _ in range(20)] for _ in range(19)]
tetromino_state = get_random_tetromino()
start_x,start_y=4,0
                
    
running = True

while running:        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game_field,start_x, start_y = move_tetromino_down(game_field, tetromino_state, start_x, start_y)
    screen.fill(WHITE)
    
    for row_idx,row in enumerate(game_field):
        for col_idx,cell in enumerate(row):
            if cell==1:
                pygame.draw.rect(screen,(255,255,0),(col_idx*square_size,row_idx*square_size,square_size,square_size))
            
        
    for i in range(20):
        pygame.draw.line(screen, RED, (0, i * square_size), (WIDTH, i * square_size))
        pygame.draw.line(screen, RED, (i * square_size, 0), (i * square_size, HEIGHT))


    pygame.display.flip()  
    clock.tick(FPS) 

pygame.quit()
sys.exit()

