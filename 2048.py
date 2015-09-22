"""
Clone of 2048 game.
"""
# Originally developed in CodeSkulptor
# link is http://www.codeskulptor.org/#user40_wBPLhuhWx9iZh2H.py

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = []
    merged_line = []
    counter = 0
    
    # Move zeros to end of list
    for num in line:
        if num != 0:
            new_line.insert(0 + counter, num)
            counter += 1
    while len(new_line) < len(line): 
        new_line.append(0)
    
    # Double value if sequential numbers equal
    for num in range(0, len(new_line) - 1):
        if new_line[num] == new_line[num + 1] and new_line[num] != 0:
            merged_line.append(new_line[num] * 2)
            new_line.pop(num + 1)
            new_line.append(0)
        else:
            merged_line.append(new_line[num])
    if new_line[-1] != 0:
        merged_line.append(new_line[-1])
    while len(merged_line) < len(new_line):
        merged_line.append(0)
        
    return merged_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
       
        # generate initial tile indices
        self._up_indices = self._grid_width * [('', '')]
        self._down_indices = self._grid_width * [('', '')]
        self._right_indices = self._grid_height * [('', '')]
        self._left_indices = self._grid_height * [('', '')]
        
        for num in range(self._grid_width):
            self._up_indices[num] = (0, num)
            self._down_indices[num] = (self._grid_height - 1, num)
        for val in range(self._grid_height):
            self._left_indices[val] = (val, 0)
            self._right_indices[val] = (val, self._grid_width - 1)
        
        self._init_indices = {UP: self._up_indices, DOWN: self._down_indices, 
                             LEFT: self._left_indices, RIGHT: self._right_indices}
      
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for col in range(self._grid_width)]
                        for row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()
                
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str([x for x in self._grid]).replace("],", "]\n")    
                
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tiles_moved = False
        
        for val in self._init_indices[direction]:
            new_list = []
            sel_row = val[0]
            sel_col = val[1]
            
            # iterate through grid to create lists to merge
            if direction == UP or direction == DOWN:
                counter = self._grid_height
            else:
                counter = self._grid_width
            
            
            for num in range(counter):
                new_list.append(self._grid[sel_row][sel_col])
                sel_row += OFFSETS[direction][0]
                sel_col += OFFSETS[direction][1]
            
            new_list = merge(new_list)
            
            # traverse grid again and populate with merged values
            sel_row = val[0]
            sel_col = val[1]
            ind = 0
            
            for num in range(counter):
                if self._grid[sel_row] [sel_col] != new_list[ind]:
                    tiles_moved = True
                    
                self._grid[sel_row][sel_col] = new_list[ind]
                sel_row += OFFSETS[direction][0]
                sel_col += OFFSETS[direction][1]
                ind += 1
            

        if tiles_moved:
            self.new_tile()
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        two_or_four = random.random()
        if two_or_four <= 0.1:
            new_tile_value = 4
        else:
            new_tile_value = 2
        
        new_tile_row = random.randint(0, self._grid_height - 1)
        new_tile_col = random.randint(0, self._grid_width - 1)
        
        while self.get_tile(new_tile_row, new_tile_col) != 0:
            new_tile_row = random.randint(0, self._grid_height - 1)
            new_tile_col = random.randint(0, self._grid_width - 1)
        
        self.set_tile(new_tile_row, new_tile_col, new_tile_value)
        
        
        
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]





            
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

