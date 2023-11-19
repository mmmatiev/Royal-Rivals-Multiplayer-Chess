import pygame

pygame.init()

# параметры окна
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = 80
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Сhees')

# Цвета
WHITE = (200, 200, 200)
BLACK = (100, 100, 100)

# фигурки импортируем
black_queen = pygame.transform.scale(pygame.image.load('image/black queen.png'), (70, 70))
black_king = pygame.transform.scale(pygame.image.load('image/black king.png'), (70, 70))
black_rook = pygame.transform.scale(pygame.image.load('image/black rook.png'), (70, 70))
black_bishop = pygame.transform.scale(pygame.image.load('image/black bishop.png'), (70, 70))
black_knight = pygame.transform.scale(pygame.image.load('image/black knight.png'), (70, 70))
black_pawn = pygame.transform.scale(pygame.image.load('image/black pawn.png'), (60, 60))
white_queen = pygame.transform.scale(pygame.image.load('image/white queen.png'), (70, 70))
white_king = pygame.transform.scale(pygame.image.load('image/white king.png'), (70, 70))
white_rook = pygame.transform.scale(pygame.image.load('image/white rook.png'), (70, 70))
white_bishop = pygame.transform.scale(pygame.image.load('image/white bishop.png'), (70, 70))
white_knight = pygame.transform.scale(pygame.image.load('image/white knight.png'), (70, 70))
white_pawn = pygame.transform.scale(pygame.image.load('image/white pawn.png'), (60, 60))


# тупа рисуем доску
def draw_board():
    for horizontal in range(8):
        for vertical in range(8):
            if (horizontal + vertical) % 2 == 0:
                pygame.draw.rect(screen, WHITE,
                                 (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, BLACK,
                                 (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if horizontal == 1:
                screen.blit(black_pawn, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
            if horizontal == 6:
                screen.blit(white_pawn, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
            if horizontal == 7:
                if vertical == 0 or vertical == 7:
                    screen.blit(white_rook, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 1 or vertical == 6:
                    screen.blit(white_rook,(vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 2 or vertical == 5:
                    screen.blit(white_bishop, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 3:
                    screen.blit(white_queen, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                else:
                    screen.blit(white_king,(vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
            if horizontal == 0:
                if vertical == 0 or vertical == 7:
                    screen.blit(black_rook, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 1 or vertical == 6:
                    screen.blit(black_rook,(vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 2 or vertical == 5:
                    screen.blit(black_bishop, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                elif vertical == 3:
                    screen.blit(black_queen, (vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))
                else:
                    screen.blit(black_king,(vertical * SQUARE_SIZE, horizontal * SQUARE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()

pygame.quit()
