import rospy
from std_msgs.msg import String


rospy.init_node('2016001100_no_2.py')

matricula = 0

def pega_valor(valor_publicado):
    global matricula
    matricula = valor_publicado.data


sub = rospy.Subscriber('/topic', String, pega_valor)

    
def timerCallBack(event):
    soma = 0
    for digito in str(matricula):
        soma += int(digito)
    msg = String()
    msg.data = str(soma)
    pub.publish(msg)
    
    
    
pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.5), timerCallBack)


rospy.spin()