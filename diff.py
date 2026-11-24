import sys

'''
LCS (least common subsequence) diff algorithm using 2D dynamic programming
'''

def getDiff(file1, file2):
    list1, list2 = fileToList(file1), fileToList(file2) 
    grid = createGrid(list1, list2)
    print(grid)
    fillGrid(grid, list1, list2)
    diff = retraceDiff(grid, list1, list2)
    printAndHighlight(diff)


def fileToList(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            return lines
    except FileNotFoundError:
        sys.exit("Error: " + file + " does not exist")
    except PermissionError:
        sys.exit("Error: Permisison delined while reading " + file)

def createGrid(list1, list2):
    rows, cols = len(list2) + 1, len(list1) + 1
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid

# main algorithm
def fillGrid(grid, list1, list2):
    # diagonal + 1 if match
    # max(top, left) if no match
    for r in range(1, len(grid)):
        for c in range(1, len(grid[0])):
            print('grid', len(grid), 'grid[0]', len(grid[0]), 'list1', len(list1), 'list2', len(list2), r, c)
            print('curr state', r, c)
            if list1[c - 1] == list2[r - 1]:
                grid[r][c] = grid[r-1][c-1] + 1
            else:
                grid[r][c] = max(grid[r-1][c], grid[r][c-1])




def retraceDiff(grid, list1, list2):
    outputStack = []
    # start at end
    r, c = len(grid) - 1, len(grid[0]) - 1
    while r > 0 or c > 0:
        curr = grid[r][c]
        if (r>0 and c>0):
            if list1[c-1] == list2[r-1]:
                outputStack.append([list1[c-1], "keep"])
                r-=1
                c-=1
            elif grid[r-1][c] > grid[r][c-1]:
                outputStack.append([list2[r-1], "+"])
                r-=1
            else:
                outputStack.append([list1[c-1], "-"])
                c-=1

        else:
            if c > 0:
                outputStack.append([list1[c-1], "-"])
                c-=1
            else:
                outputStack.append([list2[r-1], "+"])
                r-=1

    outputStack.reverse()
    return outputStack

def printAndHighlight(diffList):
    for diffLine in diffList:
        print(diffLine[1] + " __________ ", diffLine[0])



args = sys.argv[1:]
file1, file2 = args[0], args[1]
getDiff(file1, file2)
