# Use Node.js 16.13 as the base image
FROM node:16.13

# Set the working directory
WORKDIR /app

# Installs the dependencies first to cache if rebuilding is necessary
COPY package*.json .

# Install the libraries
RUN npm install

# Add the @elastic/search-ui-elasticsearch-connector package
RUN npm add @elastic/search-ui-elasticsearch-connector

# Copy the entire current directory into the working directory
COPY . .

# Expose the necessary ports, if needed
EXPOSE 3000

# Enter the copied folder and run npm start
CMD ["npm", "start"]