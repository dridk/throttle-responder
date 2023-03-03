from flask import Flask, request
import hashlib
import logging
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/throttle', methods=['POST'])
def throttle():
    data = request.get_json()
    ms = data.get('throttle')
    id = hashlib.sha1(str(data).encode('utf-8')).hexdigest()
    app.logger.info(f'Received request: {data}')
    time.sleep(ms/1000.0)
    response_data = {'id': id, 'throttle_time': ms}
    return response_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
