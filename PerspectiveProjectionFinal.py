import turtle as t

Vertices = []
Edges = []
Cords = {}
FCords = {}

CamDist = float(input("Enter Camera Distance"))

while True:
    Vertex = input("Enter Vertex (A, B, C, etc.), Leave blank if finished")
    if len(Vertex) == 0:
        break
    else:
        Vertices.append(Vertex)

while True:
    Edge = input("Enter Edges (AB, BD , etc.), Leave blank if finished")
    if len(Edge) == 0:
        break
    else:
        Edges.append((Edge[0], Edge[1]))
        print(Edges)

for i in range(len(Vertices)):
    Coordinate = str(input(("Enter  Coordinate of the point:", Vertices[i])))
    Coordinate = Coordinate.replace(")", "")
    Coordinate = Coordinate.replace("(", "")
    Coordinate = Coordinate.split(",")
    Cords[Vertices[i]] = Coordinate

def focalX(Cord, CamDist):
    X = float(Cord[0])
    Z = float(Cord[2])
    fX = CamDist * X
    fX = fX / (CamDist + Z)
    try:
        fX = fX**-1
        fX = fX * -1
    except ZeroDivisionError:
        fX = fX
    return fX * 50

def focalY(Cord, CamDist):
    Y = float(Cord[1])
    Z = float(Cord[2])
    fY = CamDist * Y
    fY = fY / (CamDist + Z)
    try:
        fY = fY ** -1
        fY = fY * -1
    except ZeroDivisionError:
        fY = fY
    return fY * 50

for i in range(len(Cords)):
    focX = focalX(Cords[Vertices[i]], CamDist)
    focY = focalY(Cords[Vertices[i]], CamDist)
    print(focX, focY)
    FocalCord = (focX, focY)
    FCords[Vertices[i]] = FocalCord

def Draw(Vertices, Edges, FCords):
    t.penup()
    for i in range(len(Edges)):
        Point1 = Edges[i][0]
        Point2 = Edges[i][1]
        t.goto(FCords[Point1])
        t.pendown()
        t.goto(FCords[Point2])
        t.penup()
    t.hideturtle()
while True:
    t.clear()
    Draw(Vertices, Edges, FCords)
    print("Change points? (Y/N)")
    change = input()
    if change.upper() == "Y":
        pointToChange = input("Which point to change?")
        Coordinate = str(input(("Enter  Coordinate of the point:", pointToChange)))
        Coordinate = Coordinate.replace(")", "")
        Coordinate = Coordinate.replace("(", "")
        Coordinate = Coordinate.split(",")
        Cords[pointToChange] = Coordinate
        focX = focalX(Cords[pointToChange], CamDist)
        focY = focalY(Cords[pointToChange], CamDist)
        FocalCord = (focX, focY)
        FCords[pointToChange] = FocalCord
    elif change.upper() == "CAM":
        CamDist = float(input("Change distance of cam:"))
        print(CamDist)
        for i in range(len(Cords)):
            focX = focalX(Cords[Vertices[i]], CamDist)
            focY = focalY(Cords[Vertices[i]], CamDist)
            print(focX, focY)
            FocalCord = (focX, focY)
            FCords[Vertices[i]] = FocalCord
    else:
        break
