from sense_hat import SenseHat
import time

sense = SenseHat()
t0 = time.time()
while True:
 
  if (time.time() - t0) % 60==0:
    t = '"' + "temperature[degree]" + '"' + ":" + '"' + str(round(sense.get_temperature(), 1)) + '"'
    p = '"' + "pressure[hPa]" + '"' + ":" + '"' + str(round(sense.get_pressure(), 1)) + '"'
    h = '"' + "humidity[%]" + '"' + ":" + '"' + str(round(sense.get_humidity(), 1)) + '"'
    
    orientation = sense.get_orientation()
    pitch = '"' + "pitch" + '"' + ":" + '"' + str(round(orientation["pitch"], 0)) + '"'
    roll = '"' + "roll" + '"' + ":" + '"' + str(round(orientation["roll"], 0)) + '"'
    yaw = '"' + "roll" + '"' + ":" + '"' + str(round(orientation["yaw"], 0)) + '"'
    
    
    acceleration = sense.get_accelerometer_raw()
    x = '"' + "x" + '"' + ":" + '"' + round(str(acceleration['x']),0) + '"'
    y = '"' + "y" + '"' + ":" + '"' + round(str(acceleration['y']),0) + '"'
    z = '"' + "z" + '"' + ":" + '"' + round(str(acceleration['z']),0) + '"'
    
    mylist = [t,p,h,pitch,roll,yaw,x,y,z]
    mystr = '{' + ','.join(map(str,mylist))+'}'
    print(mystr)
