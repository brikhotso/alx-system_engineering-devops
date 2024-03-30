**Load balancer**

This document provides instructions for setting up a load-balanced environment with two web servers using Nginx as the web server software and HAProxy as the load balancer. Additionally, it covers setting up HTTP responses with custom headers on both servers and configuring the second server using Puppet.

### Setting Up Two Web Servers with Nginx

1. **Install Nginx on both servers**:
   - Access each server individually via SSH or another remote access method using its IP address. Once logged in, run the commands to install Nginx.
   - After logging in, update the package index and install Nginx:
     ```bash
     sudo apt update
     sudo apt install nginx
     ```
   - Repeat this process for each server.

2. **Configure custom HTTP response headers**:
   - After installing Nginx, configure custom HTTP response headers by editing the Nginx configuration files.
   - Log in to each server and edit the Nginx configuration file, typically located at `/etc/nginx/nginx.conf` or within a specific site configuration under `/etc/nginx/sites-available`.
   - Add custom headers within the appropriate server block:
     ```
     http {
         ...
         server {
             ...
             add_header Custom-Header "Your_Custom_Value";
             ...
         }
         ...
     }
     ```
   - Save the configuration file and restart Nginx for changes to take effect.

### Setting Up Load Balancer with HAProxy

1. **Install HAProxy**:
   - Log in to the server where you want to install HAProxy using its IP address.
   - Update the package index and install HAProxy:
     ```bash
     sudo apt update
     sudo apt install haproxy
     ```

2. **Configure HAProxy**:
   - Edit the HAProxy configuration file, typically located at `/etc/haproxy/haproxy.cfg`, to define the load-balancing behavior and servers.
   - Inside this file, specify the frontend and backend configurations, including the load-balancing algorithm (e.g., Round Robin) and server definitions.
   - Replace `<server1_IP>:<port>` and `<server2_IP>:<port>` with the appropriate IP addresses and port numbers of your Nginx servers.
   - Save the configuration file and restart HAProxy to apply the changes.

### Setting Up Second Server with Nginx Using Puppet

1. **Install Puppet on the Puppet Master and Nodes**:
   - Follow the official Puppet documentation to install Puppet on the Puppet Master and each Node.

2. **Create Puppet Manifests**:
   - Define Puppet manifests for configuring Nginx and custom headers on the second server.
   - Specify the configurations in Puppet manifests, including Nginx installation, server setup, and custom header configuration.

3. **Apply Puppet Manifests**:
   - Apply the Puppet manifests to the Puppet Agent (Node) representing the second server.
   - Use the `puppet agent` command on the Node to initiate the Puppet run and apply the configurations defined in the manifests.

### Conclusion

By following these detailed steps, you can effectively set up the web servers, load balancer, and automate the configuration of the second server using Puppet. Remember to log in to each server individually and execute the necessary commands or configurations as described.
