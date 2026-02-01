# Use the official NGINX base image
FROM nginx:latest

# Install apache2-utils to get htpasswd utility
RUN apt-get update && apt-get install -y apache2-utils && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /etc/nginx

# Copy your custom nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your HTML files
COPY html /usr/share/nginx/html

# Generate .htpasswd file
# Replace 'username' and 'password' with your desired credentials
RUN htpasswd -bc /etc/nginx/.htpasswd username password

# Expose port 80
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
