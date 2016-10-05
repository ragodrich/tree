import sys
from sys import argv
import os


def tree(currDir, space):

    dirCount = 0
    fileCount = 0
    dirPath = os.listdir(currDir)
    childSpacing = '├── '
    lineSpacing = '│   '
    endSpacing = '└── '
    genSpacing = '    '
    files = []

    for file in dirPath:
        if file[0] != '.':
            files.append(file)
    files = sorted(files, key=lambda s: s.lower())
    for i in range(len(files)):
        if i < len(files) - 1:
            print(space + childSpacing + files[i])
            choice = lineSpacing
        else:
            print(space + endSpacing + files[i])
            choice = genSpacing
        nextUp = str(currDir + '/' + files[i])
        if os.path.isfile(nextUp):
            fileCount += 1
        else:
            dirCount += 1
            tdc, tfc = tree(nextUp, str(space + choice))
            dirCount += tdc
            fileCount += tfc

    return dirCount, fileCount


if __name__ == '__main__':
    os.getcwd()
    if(len(argv) >= 2):
        currDir = argv[1]
    else:
        currDir = "."
    print(currDir)
    dirCount, fileCount = tree(currDir, "")
    print()
    if (dirCount > 1 or dirCount == 0) and (fileCount > 1 or fileCount == 0):
        print(str(dirCount) + ' directories, ' + str(fileCount) + ' files')
    elif dirCount == 1 and fileCount > 1:
        print(str(dirCount) + ' directory, ' + str(fileCount) + ' files')
    elif dirCount > 1 and fileCount == 1:
        print(str(dirCount) + ' directories, ' + str(fileCount) + ' file')
    else:
        print(str(dirCount) + ' directory, ' + str(fileCount) + ' file')
