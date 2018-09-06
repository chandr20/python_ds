from PIL import Image
from collections import deque


def get_adjacency(n):
    x, y = n
    return [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]


def BFS(start, end, img):
    rows = img.size[0]
    columns = img.size[1]
    pixel = img.load()
    visited_matrix = [[False for row in range(rows)] for column in range(columns)]
    prev = [[None for row in range(rows)] for column in range(columns)]

    # Queue = deque([start])
    Queue = deque([start])
    visited_matrix[start[0]][start[1]] = True
    while Queue:

        s = Queue.pop()

        if s == end:
            break

        for adjacent in get_adjacency(s):

            x, y = adjacent


            if x >= 0 and x <= rows and y >= 0 and y <= columns:
                if visited_matrix[x][y] == False:
                    if pixel[x, y] == 1:
                        Queue.appendleft((x, y))
                        prev[x][y] = s
                visited_matrix[x][y] = True

    path = deque()

    current = end

    while current != None:
        path.appendleft(current)
        current = prev[current[0]][current[1]]
    return path


start = (1009,0)
end = (1897,2000)

img = Image.open('perfect2k.png')
pixel = img.load()

rows = img.size[0]
columns = img.size[1]
print(rows,columns)

#
# MAZE_MATRIX = [[pixel[row, column] for row in range(rows)] for column in range(columns)]
# print(MAZE_MATRIX)

BFS_PATH = BFS(start, end, img)
# print(BFS_PATH)
#
RGB_IMG = img.convert('RGB')

RGB = RGB_IMG.load()
#
for items in BFS_PATH:
    RGB[items[0], items[1]] = (250, 125, 100)
#
RGB_IMG.save('rosh_solved.png')

# print(BFS(start,end,img))
