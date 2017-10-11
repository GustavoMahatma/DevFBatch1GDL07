import webbrowser
import time

a=1
v1 = "https://www.youtube.com/watch?v=dPPi2D6GK7A&list=RDdPPi2D6GK7A&t=19"
v2 = "https://www.youtube.com/watch?v=EHfx9LXzxpw&index=4&list=RDdPPi2D6GK7A"
vx = v2
x = 1

if (x < 3):
    print("Hola!")
    print("Son las: ", time.ctime())
    print("clock: ", time.clock())
    time.sleep(10)
    print("Son las: ", time.ctime())
    print("clock: ", time.clock())
    print("Ver Video: ", time.ctime())
    print("Descansa con el video")
    webbrowser.open(vx)
    time.sleep(10)
    x = x + 1

