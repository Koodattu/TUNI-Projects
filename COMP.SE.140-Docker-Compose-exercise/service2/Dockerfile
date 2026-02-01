# Use the official Node.js image
FROM node:18-slim

# Install necessary Linux utilities (procps for ps, util-linux for uptime)
RUN apt-get update && apt-get install -y procps util-linux && rm -rf /var/lib/apt/lists/*

# Create a directory for the app
WORKDIR /app

# Copy the application code
COPY package*.json ./
COPY index.js ./

# Install the dependencies
RUN npm install

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["node", "index.js"]
