'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 19:20  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 19:21
* @Title: Simulate stop watch to calculate elapsed time
'''
import time

# Start time when hit enter
input("Press Enter to start")
start_time = time.time()

# Stop time when hit enter
input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
print(time_lapsed)