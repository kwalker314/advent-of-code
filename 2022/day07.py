import os

MAX_FILESIZE = 100000
TOTAL_SPACE  = 70000000
SPACE_NEEDED = 30000000
space_diff = 0
fileSystem = dict()
currentDir = ""

def addDir(destDir: str) -> str:
    """
    add the new directory to fileSystem if it doesn't exist yet
    and return the added directory's full path
    destDir should _not_ end with a slash
    if destDir is '..', the last directory of currentDir
    will be removed and the new currentDir will be one dir level up
    """
    newDir = ''
    if destDir == '..':
        # go up one directory level with some fancy string math
        newDir = '/'.join(currentDir.split('/')[:-2])+'/'
    else:
        # root directory gets special treatment
        newDir = destDir if destDir == '/' else currentDir+destDir+'/'
        # add new directory to current directory if it isn't already there
        if destDir != '/' and destDir not in fileSystem[currentDir]:
            fileSystem[currentDir].add(destDir+'/')
    
    if not newDir in fileSystem:
        fileSystem.update({newDir: set([])})
    return newDir

def addFile(file: str):
    """
    simple addition to the current directory
    file should be in the format of "{byte size} {filename}"
    """
    fileSystem[currentDir].add(file)

def getSumOfFiles(path: str) -> (int, int, int):
    """
    path is the path we're currently looking at
    
    returns:
    * the total size of directories under the limit
    * the total bytes of this directory (even if it's over the limit)
    * the size of the closest-to-ideal directory to delete found so far
    """
    bytesUnderLimit = 0
    directoryBytes = 0
    fileBytes = 0
    localSpaceDiff = space_diff
    for item in fileSystem[path]:
        #item is a directory
        if path+item in fileSystem:
            result = getSumOfFiles(path+item)
            bytesUnderLimit += result[0]
            directoryBytes += result[1]
            # part 2 logic for when it's time to play ~The Filesize Is Right(tm)~
            # keep track of the smallest directory we have that's still larger than
            # the space_diff we need
            if space_diff == localSpaceDiff:
                localSpaceDiff = max(space_diff, result[2])
            elif space_diff < result[2] < localSpaceDiff:
                localSpaceDiff = result[2]
        #item is a file with format '{filesize} {filename}'
        else:
            fileBytes += int(item.split(' ')[0])
    totalBytes = directoryBytes+fileBytes
    bytesUnderLimit += 0 if totalBytes > MAX_FILESIZE else totalBytes
    if space_diff == localSpaceDiff:
        localSpaceDiff = totalBytes
    elif space_diff < totalBytes < localSpaceDiff:
        localSpaceDiff = totalBytes
    return (bytesUnderLimit, totalBytes, localSpaceDiff)

input = open(os.path.join(os.getcwd(), "inputs/input07.txt"))
processingFiles = False
for line in input.readlines():
    lineStripped = line.strip()
    
    if lineStripped.find('$ cd') > -1:
        processingFiles = False
        #process potentially-new directory
        currentDir = addDir(lineStripped.replace('$ cd ', ''))
    elif lineStripped.find('$ ls') > -1:
        processingFiles = True #begin to process files
    elif processingFiles:
        lineSplit = lineStripped.split(' ')
        if lineSplit[0] == 'dir':
            addDir(lineSplit[1])
        else:
            addFile(lineStripped)

input.close()

part1, totalBytes, _ = getSumOfFiles('/') #begin at root directory
# inherently assuming that totalBytes+SPACE_NEEDED > TOTAL_SPACE here
# but i think that's ok lol
space_diff = totalBytes + SPACE_NEEDED - TOTAL_SPACE
# RUN THE ALGORITHM AGAIN
part2 = getSumOfFiles('/')[2]

assert part1 == 1886043, f'Part 1: expected 1886043 but got {part1}'
assert part2 == 3842121, f'Part 2: expected 3842121 but got {part2}'

print("part 1: ", part1)
print("part 2: ", part2)