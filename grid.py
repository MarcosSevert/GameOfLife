import pygame
import numpy as np
import random

class Grid:
    def __init__(self,width,height,scale,offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows,self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = random.randint(0,1)

    def game(self,off_color, on_color, surface):
        for i in range(self.rows):
            for j in range(self.columns):
                i_p = i * self.scale
                j_p = j * self.scale

                # Draw state
                if self.grid_array[i][j] == 1:
                    pygame.draw.rect(surface,on_color,[i_p,j_p,self.scale-self.offset,self.scale-self.offset])
                else:
                    pygame.draw.rect(surface,off_color,[i_p,j_p,self.scale-self.offset,self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        for i in range(self.rows):
            for j in range(self.columns):
                state = self.grid_array[i][j]
                neighbours = self.get_neighbours(i,j)
                # RULES
                if state == 0 and neighbours == 3:
                    next[i][j] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[i][j] = 0
                else:
                    next[i][j] = state
        self.grid_array = next

    def get_neighbours(self,i,j):
        total = 0
        for x in range(-1,2):
            for y in range(-1,2):
                i_edge = (i+x+self.rows) % self.rows
                j_edge = (j+y+self.columns) % self.columns
                total += self.grid_array[i_edge][j_edge]

        total -= self.grid_array[i][j]
        return total
