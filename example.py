from busysleep import calibrate_busysleep, busysleep

calibrated_N = calibrate_busysleep(1000000)


import time

startTime = time.time()
busysleep(4, calibrated_N)
timedelta = time.time() - startTime 

print ("actual run time: for 4 seconds: ", timedelta, " seconds" )
print ("error ", abs(4-timedelta)/4*100, ' %')
