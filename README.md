# busysleep
A miniature package with auto-calibration to use busy wait. 

# usage: 
```pip install busysleep

from busysleep import calibrate_busysleep, busysleep


# Passing N<1000000 will throw an error 
# because of lower accuracy, higher N
# implies higher accuracy but will take longer to calibrate
calibrated_N = calibrate_busysleep(N=1000000)  


import time

startTime = time.time()
busysleep(4, calibrated_N)
timedelta = time.time() - startTime 

print ("actual run time: for 4 seconds: ", timedelta, " seconds" )
print ("error ", abs(4-timedelta)/4*100, ' %')
```
