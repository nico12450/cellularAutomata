from typing import Match
from copy import deepcopy


class grid:

    def __init__(self,height = 10, width = 10, isFull = False):

        self.height = height
        self.width = width
        self.grid = []

        for i in range(height):

            self.grid.append([isFull] * self.width)


    def checkCoordinates(self, x, y):

        if x<0 or x>=self.width or y<0 or y>=self.height:
            raise ValueError('bad coordinates')

        return


    def setTrue(self, x, y):

        self.checkCoordinates(x, y)
        self.grid[self.height - y - 1][x] = True


    def setFalse(self, x, y):

        self.checkCoordinates(x, y)
        self.grid[self.height - y - 1][x] = False


    def toggle(self, x, y):

        self.checkCoordinates(x, y)
        self.grid[self.height - y - 1][x] = not self.grid[self.height - y - 1][x]


    def get(self, x, y):

        try:

            self.checkCoordinates(x, y)

        except ValueError:

            return None

        return self.grid[self.height - y - 1][x]

    def neighbors(self, x, y):

        return [self.get(x-1, y+1), self.get(x, y+1), self.get(x+1, y+1), self.get(x-1, y), self.get(x+1, y), self.get(x-1, y-1), self.get(x, y-1), self.get(x+1, y-1)]

    def neighborsCount(self, x, y):

        result = 0

        for cell in self.neighbors(x, y):

            if cell:

                result += 1

        return result

    def display(self):

        for row in self.grid:

            print(row)

    def copy(self):
        return deepcopy(self)




class gridGame:

    def __init__(self, rules, grid = grid()):
        
        self.grid = grid
        self.gridTemp = None
        self.rules = rules

    def nextState(self):

        self.gridTemp = self.grid.copy()

        for x in range(self.grid.width):
            for y in range(self.grid.height):
                for rule in self.rules:

                    if self.grid.get(x, y) == rule.isAlive:
                        self.apply(rule, x, y)

        self.grid = self.gridTemp.copy()

    def applyAction(self, x, y, cellAction):

        match cellAction:

            case 'born':

                self.gridTemp.setTrue(x, y)

            case 'die':

                self.gridTemp.setFalse(x, y)

            case 'change':

                self.gridTemp.toggle(x, y)

    def apply(self, rule, x, y):

        match rule.comparator:

            case '<' :

                if self.grid.neighborsCount(x, y) < rule.neighborsCount:

                    self.applyAction(x, y, rule.cellAction)

            case '>' :

                if self.grid.neighborsCount(x, y) > rule.neighborsCount:

                    self.applyAction(x, y, rule.cellAction)

            case '=' :

                if self.grid.neighborsCount(x, y) == rule.neighborsCount:

                    self.applyAction(x, y, rule.cellAction)

    def display(self):

        self.grid.display()


class rule:

    def __init__(self, isAlive, neighborsCount, comparator, cellAction):

        self.isAlive = isAlive
        self.neighborsCount = neighborsCount
        self.comparator = comparator
        self.cellAction = cellAction