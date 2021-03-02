from sense_hat import SenseHat
import time

sense = SenseHat()
t0 = time.time()
while True:
 
  if (time.time() - t0) % 60==0:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    print(t)
