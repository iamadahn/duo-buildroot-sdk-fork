# -*- coding: utf-8 -*-
import time
from pinpong.board import Board
from pinpong.libs.dfrobot_bmi160 import BMI160

Board("RPI").begin()#初始化


bmi = BMI160(bus_num=1)

bmi.begin(bmi.acc)

while True:
  gyr_x = bmi.get_gyr_x()
  acc_x = bmi.get_acc_x()
  gyr_y = bmi.get_gyr_y()
  acc_y = bmi.get_acc_y()
  gyr_z = bmi.get_gyr_z()
  acc_z = bmi.get_acc_z()
  print("{}  {}  {}  {}  {}  {}".format(gyr_x, gyr_y, gyr_z, acc_x, acc_y, acc_z))
  time.sleep(0.5)