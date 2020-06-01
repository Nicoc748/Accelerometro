#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
import serial
import time

ACC=[]
ACCX=[]
ACCY=[]
ACCZ=[]

arduinodata=serial.Serial('/dev/ttyUSB0',9600) 

def accel_value(a):
    g=(((a*3300)/1024)-1650)/300    #Vs=3300mV  1024=2^10 (ADC)  Vs/2=1650    Sensitivity=330 mV/g
    return g    #Viene preso come 0g (offset) Vs/2 ma forse occorre modificarlo con la calibratura

for k in range(10):
    while (arduinodata.inWaiting()==0):
        pass
    arduinostring=arduinodata.readline()
    DataArray=" ".join(arduinostring.split())   #Eliminazione spazi vuoti
    DataArray=DataArray.split(",")
    accxtemp=accel_value(float(DataArray[0]))
    accytemp=accel_value(float(DataArray[1]))
    accztemp=accel_value(float(DataArray[2]))
    ACCLX.append(accxtemp)
    ACCLY.append(accytemp)
    ACCLZ.append(accztemp)
ACC.append(ACCLX)
ACC.append(ACCLY)
ACC.append(ACCLZ)    #Matrice 3x10

#Occorre modificare software arduino e questo per la lettura delle accelerazioni angolari

def publisheracc():
    pub = rospy.Publisher('accelerazioni', Float32MultiArray , queue_size=10)
    rospy.init_node('publisheracc', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo(ACC)
        pub.publish(ACC)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisheracc()
    except rospy.ROSInterruptException:
        pass