from time import localtime, mktime, strftime


start_time = localtime()

print(f"Timer started at {strftime('%X', start_time)}")

# wait for user to stop timer

input("Pres any enter to stop timer")

stop_time = localtime()
diff = mktime(stop_time) - mktime(start_time)

print(f"Stop time is {strftime('%X', stop_time)}")
print(f"Total time : {diff} seconds")