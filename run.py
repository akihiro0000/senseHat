from sense_hat import SenseHat
import time

sense = SenseHat()
t0 = time.time()
while True:
 
  if (time.time() - t0) % 60==0:
    t = '"' + "temperature[degree]" + '"' + ":" + '"' + str(round(sense.get_temperature(), 1)) + '"'
    p = '"' + "pressure[hPa]" + '"' + ":" + '"' + str(round(sense.get_pressure(), 1)) + '"'
    h = '"' + "humidity[%]" + '"' + ":" + '"' + str(round(sense.get_humidity(), 1)) + '"'
    mylist = [t,p,h]
    mystr = '{' + ','.join(map(str,mylist))+'}'
    print(mystr)
