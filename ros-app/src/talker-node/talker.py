#!/usr/bin/env python
import os
import rospy
#import threading

from flask import Flask, request
from std_msgs.msg import String

#import html

app = Flask(__name__)

#threading.Thread(target=lambda: rospy.init_node('talker', disable_signals=True)).start()
rospy.init_node('talker', anonymous=True)
pubMotion = rospy.Publisher('/recieved_data', String, queue_size=10)
#pubStop = rospy.Publisher('/requestStop01', String, queue_size=1)

@app.route('/api/log', methods = ['POST'])
def send_message():
    pubMotion.publish(request.json['data'])
    return ''
    #if request.method == 'POST': pubMotion.publish('post request')
    #content = request.json
    #if content['data'].find('error') != -1:
    #    pubMotion.publish('post request contains error substring')
    #    return 'true'
    #    #return request.form
    #else:
    #    pubMotion.publish('post request does not contains error substring')
    #    return 'false'

if __name__ == '__main__':
    # from og server
	app.run(host='0.0.0.0', port=5000, debug=True)
