# Use the official Nginx image as the base image
FROM nginx:alpine

# Create a simple HTML page
RUN echo "<!DOCTYPE html><html><head><title>Hello World</title></head><body style="background:green"><h1>Hello, World!</h1><p>This is a simple web server running in a Docker container on port 80.</p></body></html>" > /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Nginx will automatically start serving the HTML file on port 80
