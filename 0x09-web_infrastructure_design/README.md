# Web Infrastructure Design:

# Components of the Infrastructures:

* User access the website hosted at www.foobar.com.
* User's computer resolves www.foobar.com to the server's IP address, 8.8.8.8, using DNS (Domain Name System).
* Server: A physical or virtual machine responsible for hosting all components of the web infrastructure.
* Web Server (Nginx): Handles HTTP requests from clients, serving static content, and passing dynamic requests to the application server.
* Application Server: Executes the application code and generates dynamic content based on client requests.
* Application Files (Code Base): The source code and related files that comprise the website or web application.
* Database (MySQL): Stores and manages data persistently for the web application. MySQL is a popular relational database management system (RDBMS).
* Domain Name: Acts as a human-readable alias for the server's IP address.
* www Record: The www record in www.foobar.com is a CNAME record, which stands for Canonical Name record. It aliases one domain name to another, allowing the www subdomain to point to foobar.com.
* Load Balancer (HAproxy): distributes incoming network traffic across multiple servers to ensure no single server becomes overwhelmed, thus improving reliability and scalability.
* Firewalls : security devices or software that monitor and control incoming and outgoing network traffic based on predetermined security rules.
* SSL Certificate: (Secure Sockets Layer) certificate encrypts data exchanged between a user's browser and the web server, ensuring secure communication over HTTPS.
* Monitoring Clients (Data Collector): gather and aggregate data from various sources for analysis and visualization.
* Sumo Logic: Helps organizations monitor, troubleshoot, and secure IT infrastructure.

## Simple web stack:

![Image_1](https://i.imgur.com/d4c0t5D.png)

### Issues with the Infrastructure:

* Single Point of Failure (SPOF): Since there's only one server, any failure in hardware or software components could lead to downtime for the entire website.
* Downtime During Maintenance: Performing maintenance tasks, such as deploying new code that requires restarting the web server, will result in downtime for the website.
* Limited Scalability: The infrastructure cannot easily handle a sudden increase in incoming traffic. Scaling options are limited due to the single server setup, potentially leading to performance issues or downtime during traffic spikes.

## Distributed web infrastructure:

![Image_2](https://i.imgur.com/qQAUyiQ.png)

### Issues with the Infrastructure:

* No Firewall: Without a firewall, the infrastructure is vulnerable to unauthorized access, malicious attacks, and data breaches.
* No HTTPS: exposes it to interception, eavesdropping, and tampering, jeopardizing user privacy and data integrity.Negatively impacts SEO rankings and user trust.
* Lack of Monitoring: Without monitoring, the infrastructure is blind to potential security breaches, unauthorized access attempts, resource utilization spikes, and system failures.
* Single Point of Failure (SPOF): If either server fails, the entire system could become inaccessible or experience downtime.

## Secured and monitored web infrastructure

![Image_3](https://i.imgur.com/1MU6EzK.png)

### Issues with the Infrastructure:

* Terminating SSL at the Load Balancer Level: presents security risks by exposing sensitive data to potential interception within the internal network. Additionally, it may fail to meet compliance requirements for end-to-end encryption, potentially leaving data vulnerable to unauthorized access. Moreover, the practice limits visibility into encrypted traffic for security monitoring and inspection purposes, hindering the detection of potential threats or anomalies.

* Single MySQL Server Accepting Writes: poses significant risks, as any failure or downtime can disrupt critical write operations and impact the application's availability. Furthermore, scalability becomes a concern as the server may struggle to handle increasing write loads or data volumes, potentially leading to degraded performance. Without redundancy or backup measures in place, there's a heightened risk of data loss in the event of a catastrophic failure or hardware/software issues.

* Servers with Same Components: introduces a homogeneous failure risk, where issues affecting one component may propagate across all servers simultaneously, increasing the likelihood of widespread downtime. Moreover, the lack of flexibility inherent in identical configurations may hinder adaptability to changing requirements or workload patterns. Additionally, managing dependencies and troubleshooting issues becomes more complex.

## Scale up

![Image_4](https://i.imgur.com/0bIHl7M.png)

* Load-Balancer (HAproxy) Configured as Cluster: enhances the infrastructure's availability and fault tolerance. Load balancer clustering enables automatic failover between instances, ensuring uninterrupted traffic distribution even if one load balancer becomes unavailable.

* Split Components with their Own Server: enhances modularity, scalability, and fault isolation. Each component (web server, application server, database) has its dedicated server, allowing for independent scaling and resource allocation based on individual requirements. This separation isolates potential issues, preventing one component's failure from impacting others and improving overall system resilience. Additionally, it facilitates efficient resource utilization and easier maintenance, as updates or changes can be applied to specific components without affecting others.
