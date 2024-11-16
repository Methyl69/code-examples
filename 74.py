import math
import time

PI =math.pi

def calchypotenuse (sidea, sideb):
    sidec = 0.0
    sidec = math.sqrt ((sidea **2) + (sideb ** 2))
    return (sidec)

print("waiting for 1 second.")

time.sleep (1)
print(calchypotenuse(3.0, 4.0))

print("waiting for 2 seconds.")
time.sleep(2)
print ("PI:",PI)

print("waiting for 2 seconds.")
time.sleep(2)
print("ceiling", math.ceil (PI))

print("waiting for 2 seconds.")
time.sleep(2)
print("floor:", math.floor(PI))

print("waiting for 2 seconds.")
time.sleep(2)

print("goodbye")
