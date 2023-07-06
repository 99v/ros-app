#!/usr/bin/env python
import rospy

from flask import Flask, request
from std_msgs.msg import String

app = Flask(__name__)

rospy.init_node('talker', anonymous=True)
pubMotion = rospy.Publisher('/recieved_data', String, queue_size=10)

@app.route('/api/log', methods = ['POST'])
def send_message():
    pubMotion.publish(request.json['data'])
    return ''

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
