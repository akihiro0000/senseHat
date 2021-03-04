from sense_hat import SenseHat
import time
import paho.mqtt.client as mqtt
from datetime import datetime

sense = SenseHat()
t0 = time.time()

mqtt_client = mqtt.Client()
mqtt_client.connect("fluent-bit",1883, 60)

while True:
 
  if (time.time() - t0) % 60==0:
    t = '"' + "temperature[degree]" + '"' + ":" + '"' + str(round(sense.get_temperature(), 1)) + '"'
    p = '"' + "pressure[hPa]" + '"' + ":" + '"' + str(round(sense.get_pressure(), 1)) + '"'
    h = '"' + "humidity[%]" + '"' + ":" + '"' + str(round(sense.get_humidity(), 1)) + '"'
    tim = '"timestamp":"'+datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')+'"'
    
    orientation = sense.get_orientation()
    pitch = '"' + "pitch" + '"' + ":" + '"' + str(round(orientation["pitch"], 0)) + '"'
    roll = '"' + "roll" + '"' + ":" + '"' + str(round(orientation["roll"], 0)) + '"'
    yaw = '"' + "yaw" + '"' + ":" + '"' + str(round(orientation["yaw"], 0)) + '"'
    
    
    acceleration = sense.get_accelerometer_raw()
    x = '"' + "x" + '"' + ":" + '"' + str(round(acceleration['x'], 0)) + '"'
    y = '"' + "y" + '"' + ":" + '"' + str(round(acceleration['y'], 0)) + '"'
    z = '"' + "z" + '"' + ":" + '"' + str(round(acceleration['z'], 0)) + '"'
    
    mylist = [tim,t,p,h,pitch,roll,yaw,x,y,z]
    mystr = '{' + ','.join(map(str,mylist))+'}'
    print(mystr)
    mqtt_client.publish("{}/{}".format("/demo",'car_count'), mystr)

    
mqtt_client.disconnect()
