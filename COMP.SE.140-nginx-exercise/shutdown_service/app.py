import docker
from flask import Flask, request
import os
import threading

app = Flask(__name__)

@app.route('/stop')
def stop():
    client = docker.from_env()
    containers = client.containers.list()
    for container in containers:
        if 'shutdown_service' not in container.name:
            container.kill()
    # Stop the shutdown_service container last
    def shutdown():
        # Delay to ensure response is sent before shutting down
        import time
        time.sleep(1)  # Wait for 1 second
        # Exit the application, which stops the container
        os._exit(0)
    threading.Thread(target=shutdown).start()
    return 'System is shutting down.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
