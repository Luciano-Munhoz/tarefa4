import rospy
from std_msgs.msg import String

rospy.init_node('2016001100.py')

v = 0

def retorna_valor(valor):
    global v
    v = valor.data

def timerCallBack(event):
    print(v)
    msg = String()
    msg.data = str(2016001100)
    pub.publish(msg)
    
    
    
pub = rospy.Publisher('/topic', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.5), timerCallBack)
sub = rospy.Subscriber('/topic1', String, retorna_valor)

rospy.spin()