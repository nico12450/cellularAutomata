from Engine import *

gameOfLife = gridGame([rule(False, 3, '=', 'born'), rule(True, 2, '<', 'die'), rule(True, 3, '>', 'die')])
# gameOfLife.grid.setTrue(4, 4)
# gameOfLife.grid.setTrue(5, 4)
# gameOfLife.grid.setTrue(6, 4)
# gameOfLife.display()
# gameOfLife.nextState()
# gameOfLife.display()