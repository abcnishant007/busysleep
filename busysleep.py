import time 
import sys

def calibrate_busysleep(N = 100000000):
    """
    calibrates the value of loop counter to run it for 1 second
    input N can be increased to increase accuracy of the calculated time
    """
    try:
        assert (N>=1000000)
    except:
        print ("N too small, this will result in very high error, consider increasing N\
         to 10^8\n Cosinder increasing N while calling calibrate_busysleep")
        sys.exit()

    starttime = time.time()
    for i in range(N):
        waste_some_time = "running_meaningless_loop"
    timedelta = time.time() - starttime
    return int(N*1.0/timedelta)  # 1.0 to ensure running on python 2 as well

    
    
def busysleep(t, calibrated_N):
    """
    busy waits for t seconds; calibrated N muse be produced using 
    the calibrate_busy_wait_function
    """
    N = int(calibrated_N * t)

    for i in range(N):
        dummy = "busy wait"

    return 

