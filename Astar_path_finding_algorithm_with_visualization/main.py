import math
import pygame 
from queue import PriorityQueue

WIDTH = 600
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path finding algorithm")

#Defining color RGB valeus
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

#Single square od the maze grid class
class Spot:
    def __init__(self, row , coll, width, total_rows):
        self.row = row
        self.coll = coll
        self.x = row * width
        self.y = coll * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.coll

    def is_closed(self):
        return self.color == RED

    def is_opened(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, Window):
        pygame.draw.rect(Window, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        #Checking the square below
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.coll].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.coll])
        #Checking the square above 
        if self.row > 0 and not grid[self.row - 1][self.coll].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.coll])
        #Checking the square on the right
        if self.coll < self.total_rows - 1 and not grid[self.row][self.coll + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.coll + 1])
        #Checking the square on the left
        if self.coll > 0 and not grid[self.row][self.coll - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.coll - 1])



    def __lt__(self, other):
        return False


#Function for calsulating H(n) distance from current node to last one
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruckt_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

#A* algorithm code
def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start} #Keeping truck off items in PriorityQueue

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            print("Path found!!!")
            reconstruckt_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()
        if current != start:
            current.make_closed()

    return False
    
#Function defineing the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

#Function drwaing the grid in between spots
def draw_grid(Window, rows, width):
    gap = width // rows
    for i in range(rows):
        #Drwaing wertical lines beetwen spots
        pygame.draw.line(Window, GREY, (0, i * gap), (width, i * gap))
        #Drwaing horizontal lines beetwen spots
        pygame.draw.line(Window, GREY, (i * gap, 0), (i * gap, width))

#Main frwaing function
def draw(Window, grid, rows, width):
    Window.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(Window)

    draw_grid(Window, rows, width)
    pygame.display.update()

#Funtction to translate mouse postition on sqyare in the grid
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    coll = x // gap

    return row, coll

#Main function of the script drwaing the visualization and running the algorithm
def main(Window, width):
    ROWS = 50 
    grid = make_grid(ROWS, width)

    start = None
    end = None
    run = True

    while run:
        draw(Window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, coll = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][coll]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, coll = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][coll]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    print("Running the algorytm....")
                    algorithm(lambda: draw(Window, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)
    pygame.quit()

main(WINDOW, WIDTH)