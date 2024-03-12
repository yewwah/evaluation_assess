# Use Node.js 16.13 as the base image
FROM node:16.13 as builder

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the working directory
COPY ./ /app

# Add the @elastic/search-ui-elasticsearch-connector package
RUN npm add @elastic/search-ui-elasticsearch-connector

RUN npm run build

# Stage 2: Use Nginx to Serve the Built React App
FROM nginx:alpine

# Copy the built app from the previous stage
COPY --from=builder /app/build /usr/share/nginx/html

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf 

# Expose port 3000
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

