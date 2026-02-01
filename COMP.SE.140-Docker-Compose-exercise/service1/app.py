import os
import socket
import requests
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def get_system_info():
    ip_address = socket.gethostbyname(socket.gethostname())

    # Split disk space into lines and format as list of dicts
    disk_space_raw = subprocess.getoutput("df -h /").splitlines()
    disk_space = {
        "Filesystem": disk_space_raw[1].split()[0],
        "Size": disk_space_raw[1].split()[1],
        "Used": disk_space_raw[1].split()[2],
        "Available": disk_space_raw[1].split()[3],
        "Use%": disk_space_raw[1].split()[4],
        "Mounted on": disk_space_raw[1].split()[5]
    }

    # Split processes into lines and format as list of dicts
    processes_raw = subprocess.getoutput("ps -ax").splitlines()
    processes = []
    for process in processes_raw[1:]:  # Skip header row
        parts = process.split(maxsplit=4)
        processes.append({
            "PID": parts[0],
            "TTY": parts[1],
            "STAT": parts[2],
            "TIME": parts[3],
            "COMMAND": parts[4]
        })

    uptime = subprocess.getoutput("uptime -p")

    return {
        "IP Address": ip_address,
        "Processes": processes,
        "Disk Space": disk_space,
        "Uptime": uptime
    }

@app.route('/')
def index():
    service1_info = get_system_info()
    service2_info = requests.get('http://service2:5000').json()
    # Use json.dumps to pretty-print with indentation before returning
    return app.response_class(
        response=app.json.dumps({"Service1": service1_info, "Service2": service2_info}, indent=4),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8199)
