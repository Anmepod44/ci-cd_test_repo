# Use the official Nginx image as the base image
FROM nginx:alpine

# Create a simple HTML page
RUN echo "<!DOCTYPE html><html><head><title>Hello World</title></head><body style="background:blue"><h1>Hello, World!</h1><p>This is a dummy backend container 18/14:19</p></body></html>" > /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 5001

# Nginx will automatically start serving the HTML file on port 80
