import time
import webbrowser

total_B = 3
Break_C = 0

print ("This program started on " + time.ctime())
while Break_C < total_B:
    time.sleep(2)
    webbrowser.open_new("www.youtube.com")
    Break_C = Break_C + 1
