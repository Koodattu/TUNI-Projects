import os
import socket
import requests
import subprocess
import time  # Import time module
from flask import Flask, jsonify, make_response, request
import platform

app = Flask(__name__)

busy_until = 0  # Global variable to track service availability

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    hostname = platform.node()

    # Disk space
    disk_space_raw = subprocess.getoutput("df -h /").splitlines()
    disk_space = {
        "Filesystem": disk_space_raw[1].split()[0],
        "Size": disk_space_raw[1].split()[1],
        "Used": disk_space_raw[1].split()[2],
        "Available": disk_space_raw[1].split()[3],
        "Use%": disk_space_raw[1].split()[4],
        "Mounted on": disk_space_raw[1].split()[5]
    }

    # Processes
    processes_raw = subprocess.getoutput("ps -ax").splitlines()
    processes = []
    for process in processes_raw[1:]:
        parts = process.split(maxsplit=4)
        processes.append({
            "PID": parts[0],
            "TTY": parts[1],
            "STAT": parts[2],
            "TIME": parts[3],
            "COMMAND": parts[4] if len(parts) > 4 else ""
        })

    uptime = subprocess.getoutput("uptime -p")

    return {
        "Hostname": hostname,
        "IP Address": ip_address,
        "Processes": processes,
        "Disk Space": disk_space,
        "Uptime": uptime
    }

@app.route('/')
def index():
    global busy_until
    current_time = time.time()
    if current_time < busy_until:
        # Service is busy, return 503 Service Unavailable
        return make_response('Service is busy, please try again later.', 503)
    else:
        # Process the request
        service1_info = get_system_info()
        service2_info = requests.get('http://service2:5000').json()
        response_data = {"Service1": service1_info, "Service2": service2_info}

        # Send the response immediately
        response = app.response_class(
            response=app.json.dumps(response_data, indent=4),
            mimetype='application/json'
        )

        # Update busy_until to current time + 2 seconds
        busy_until = current_time + 2

        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)
