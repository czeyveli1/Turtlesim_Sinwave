#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist  #hız mesajı için
import math

def hareket():
    rospy.init_node('sin_wave') #Düğümü başlatmak için
    turtle_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    while not rospy.is_shutdown():
        vel = Twist()
        vel.linear.x = 0.3 #lineer hız
        vel.angular.z =  math.sin(2 * math.pi * 0.1 * rospy.get_time())  #zamana bağlı oluşturulan sinüs dalgasını açısal hıza atadık.
        turtle_vel.publish(vel)

hareket()
