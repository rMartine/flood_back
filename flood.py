# Description: This function takes a grid, a cell position and a new color and
#              returns a new grid with the cell position and all the cells
#              connected to it with the same color as the cell position flooded
#              with the new color.
# Parameters: originalGrid - a grid of cells. Each cell has a dictionary with a single key 'color'.
#             cellPosition - a dictionary with the keys 'row' and 'col' that represents
#                            the cell position to be flooded
#             newColor - A dictionary witha single key 'color' which has an Hex RGB color that represents the new color to flood
#                        the cells with.
# Return value: a new grid of cells with the cell position and all the cells
#               connected to it with the same color as the cell position flooded
#               with the new color. The rest of the cells will keep their original color.

def flood(grid, cellPosition, originalColor, newColor, visitedCells):
    if cellPosition['row'] < 0 or cellPosition['row'] >= len(grid) or cellPosition['col'] < 0 or cellPosition['col'] >= len(grid[0]):
        return grid
    if cellPosition in visitedCells:
        return grid
    if grid[cellPosition['row']][cellPosition['col']]['color'] != originalColor['color']:
        return grid
    visitedCells.append(cellPosition)
    grid[cellPosition['row']][cellPosition['col']] = newColor
    grid = flood(grid, {'row': cellPosition['row'], 'col': cellPosition['col'] - 1}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'], 'col': cellPosition['col'] + 1}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] - 1, 'col': cellPosition['col']}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] + 1, 'col': cellPosition['col']}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] - 1, 'col': cellPosition['col'] - 1}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] - 1, 'col': cellPosition['col'] + 1}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] + 1, 'col': cellPosition['col'] - 1}, originalColor, newColor, visitedCells)
    grid = flood(grid, {'row': cellPosition['row'] + 1, 'col': cellPosition['col'] + 1}, originalColor, newColor, visitedCells)
    return grid

def generated_flooded_grid(originalGrid, cellPosition, newColor):
    floodedGrid = []
    for row in originalGrid:
        floodedGrid.append(row.copy())
    visitedCells = []
    originalColor = originalGrid[cellPosition['row']][cellPosition['col']]
    try:
        floodedGrid = flood(floodedGrid, cellPosition, originalColor, newColor, visitedCells)
        print('Returned flooded grid')
        return floodedGrid
    except Exception as e:
        print('Error flooding the grid', e)
        return originalGrid