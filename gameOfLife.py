class grid:

    def __init__(self,height = 10, width = 10, isFull = False):

        self.height = height
        self.width = width
        self.grid = []

        for i in range(height):

            self.grid.append([isFull] * self.width)


    def checkCoordinates(self, x, y):

        if x<0 or x>self.width or y<0 or y>self.height:
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

        self.checkCoordinates(self, x, y)
        return self.grid[self.height - y - 1][x]


    def display(self):

        for row in self.grid:

            print(row)

# class gridGame:

#     def __init__(self, grid, rules = None):
        
#         self.grid = grid
#         self.rules = rules

#     def nextState(self):

#         for x in range(self.grid.width):
#             for y in range(self.grid.height):
#                 for rule in self.rules:
#                     rule.apply(self.grid, x, y)


grilleTest = grid()
grilleTest.display()
# grilleTest.setTrue(0,0)
# grilleTest.setTrue(2,3)
# grilleTest.setFalse(2,3)
# grilleTest.toggle(2,3)
# grilleTest.display()

# print(grilleTest.grid[0][0])