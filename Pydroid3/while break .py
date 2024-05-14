#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
i = 0
while True:
  print(i)
  i = i + 1
  if i >= 10000:
    print("Breaking")
    break

print("Finished")