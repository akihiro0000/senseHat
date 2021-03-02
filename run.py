from sense_hat import SenseHat
sense = SenseHat()
while True:
  t0 = time.time()
  
  if ((time.time() - t0) > 60):
    # 温度と湿度、気圧を測定
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    # 小数点以下第1位に四捨五入
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    # 文字表示内容の設定

    print(t)
