import os

trees = []

def findVisibleTrees() -> int:
    visibleTrees = 0
    maxScenicScore = 0
    maxUp = [-1] * len(trees[0])
    maxLeft = [-1] * len(trees)
    for treeRow in range(len(trees)):
        for treeCol in range(len(trees[treeRow])):
            height = trees[treeRow][treeCol]
            # if we're on an edge, the tree is automatically visible
            # and our scenic score cannot benefit
            if treeRow == 0 or treeCol == 0 or \
                treeRow == len(trees)-1 or treeCol == len(trees[treeRow])-1:
                visibleTrees += 1
                maxUp[treeCol] = max(maxUp[treeCol], height)
                maxLeft[treeRow] = max(maxLeft[treeRow], height)
                continue

            # otherwise we have to calculate things the hard way
            # (but our scenic score _can_ benefit 😌)
            maxRight = max(trees[treeRow][treeCol+1:])
            maxDown = max([row[treeCol] for row in trees[treeRow+1:]])

            if height > min(maxRight, maxLeft[treeRow], maxUp[treeCol], maxDown):
                visibleTrees += 1
            
            # basically a small optimization to keep track of the tallest tree
            # above the current tree and to the left of it
            maxUp[treeCol] = max(maxUp[treeCol], height)
            maxLeft[treeRow] = max(maxLeft[treeRow], height)

            # part 2 - look for what trees _are_ visible from the current tree,
            # and count those
            # sidenote i always hate how up/left/right/down calculations look
            # but idk how to make them look better :o(
            
            # up
            localScenicScore = 1
            for lTreeRow in range(treeRow-1, -1, -1):
                if lTreeRow == 0 or trees[lTreeRow][treeCol] >= height:
                    localScenicScore *= (treeRow - lTreeRow)
                    break
            
            # left
            for lTreeCol in range(treeCol-1, -1, -1):
                if lTreeCol == 0 or trees[treeRow][lTreeCol] >= height:
                    localScenicScore *= (treeCol - lTreeCol)
                    break
            
            # down
            for lTreeRow in range(treeRow+1, len(trees)):
                if lTreeRow == len(trees)-1 or trees[lTreeRow][treeCol] >= height:
                    localScenicScore *= (lTreeRow - treeRow)
                    break
            
            # right
            for lTreeCol in range(treeCol+1, len(trees[treeRow])):
                if lTreeCol == len(trees[treeRow])-1 or trees[treeRow][lTreeCol] >= height:
                    localScenicScore *= (lTreeCol - treeCol)
                    break
            
            maxScenicScore = max(maxScenicScore, localScenicScore)
    return (visibleTrees, maxScenicScore)

input = open(os.path.join(os.getcwd(), "inputs/input08.txt"))
for line in input.readlines():
    intLine = list(map(int, line.strip()))
    trees.append(intLine)
input.close()

part1, part2 = findVisibleTrees()

assert part1 == 1700, f'Part 1: expected 1700 but got {part1}'
assert part2 == 470596, f'Part 2: expected 470596 but got {part2}'

print("part 1: ", part1)
print("part 2: ", part2)