import rospy
from std_msgs.msg import String


rospy.init_node('2016001100.py')

def timerCallBack(event):
    msg = String()
    msg.data = '2016001100'
    pub.publish(msg)
    
    
pub = rospy.Publisher('/topic', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.2), timerCallBack)

rospy.spin()