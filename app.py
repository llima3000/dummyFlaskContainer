from flask import Flask, jsonify, request
from time import sleep
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def rootpath():
   response = {}
   response['startTime'] = datetime.now()
   sleep(5)
   response['stopTime'] = datetime.now()
   response['totalSpent'] = response['stopTime'] - response['startTime']
   response['totalSpent'] = response['totalSpent'].total_seconds()
   response['startTime'] = response['startTime'].strftime('%Y-%m-%d %H:%M:%S')
   response['stopTime'] = response['stopTime'].strftime('%Y-%m-%d %H:%M:%S')
   if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      response['REQUESTER'] = request.environ['REMOTE_ADDR']
   else:
      response['REQUESTER'] = request.environ['HTTP_X_FORWARDED_FOR']
   
   return jsonify(response)

@app.route('/hm/')
def health_monitor():
   response = {}
   response['startTime'] = datetime.now()
   response['stopTime'] = datetime.now()
   response['totalSpent'] = response['stopTime'] - response['startTime']
   response['totalSpent'] = response['totalSpent'].total_seconds()
   response['startTime'] = response['startTime'].strftime('%Y-%m-%d %H:%M:%S')
   response['stopTime'] = response['stopTime'].strftime('%Y-%m-%d %H:%M:%S')
   if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
      response['REQUESTER'] = request.environ['REMOTE_ADDR']
   else:
      response['REQUESTER'] = request.environ['HTTP_X_FORWARDED_FOR']
   
   return jsonify(response)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)