import math
PI = math.pi
def areaosquare (pside):
    area = 0
    area = pside **2
    return(area)

def areaofrectangle (pwidth, pheight):
    area = 0
    area = pwidth * pheight
    return (area)

def areaoftriangle (pbase, pheight):
    area = 0
    area = (1/2) * pbase *pheight
    return (area)

def areaofcircle (pradius):
    area = 0
    area = PI *(pradius**2)
    return (area)
answer = areaosquare (33.33)
print("square :", round (answer, 0))
answer = areaofrectangle (101.10, 20.20)
print("recatngle: ", round(answer, 1))
answer = areaofrectangle (5.5, 25.25)
print("trinagle:", round(answer, 2))
answer =  areaofcircle(22.22)
print ("circle: ", round(answer, 3))
