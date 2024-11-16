thedetails = []
thesize = 0
def getimagedetails():
 width= 0
 height = 0
 colors  = 0
 details = []

 width= int(input("enter image width in pixels:"))
 height= int(input("enter image height in pixels:"))
 colors  =int(input("enter image color in pixels:"))

 details.append (width)
 details.append (height)
 details.append (colors)
 return (details)

def calculateimagesize (pwidth, pheight, pcolourdepth):
    size =0
    size = pwidth * pheight * pcolourdepth

    return (size)
def outputtouser (pimagesize):
    print("your image is" + str (pimagesize) + "bits")

thedetails =getimagedetails()
thesize = calculateimagesize (thedetails[0],thedetails[1],thedetails[2],)
outputtouser (thesize)
