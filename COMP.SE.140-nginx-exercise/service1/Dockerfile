# Use Python base image
FROM python:3.9-slim

# Install necessary Linux utilities (procps for ps, util-linux for uptime)
RUN apt-get update && apt-get install -y procps util-linux && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py /app

# Install necessary Python packages
RUN pip install flask requests

# Expose port 8199 for the service
EXPOSE 8199

# Command to run the application
CMD ["python", "app.py"]
