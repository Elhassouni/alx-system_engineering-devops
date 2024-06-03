Web Infrastructure Design: Summary and Detailed Exercises
This repository contains projects for designing and understanding web infrastructure. Each project builds on the previous one, creating more robust and scalable systems.

Summary
Simple Web Stack: Basic infrastructure with a single server hosting a website.
Distributed Web Infrastructure: Multiple servers to distribute the load and increase reliability.
Secured and Monitored Web Infrastructure: Enhanced security and monitoring with encrypted traffic.
Scale Up: Infrastructure capable of handling more traffic by adding more servers and load balancing.
Detailed Exercises
0. Simple Web Stack
Goal: Design a basic web infrastructure with a single server.

Requirements
1 Server
1 Web Server (Nginx)
1 Application Server
1 Application Files (code base)
1 Database (MySQL)
1 Domain Name: foobar.com configured with a www record pointing to the server IP 8.8.8.8
Explanation
Server: A machine that provides resources and services to clients.
Domain Name: Human-readable address of the website (foobar.com).
DNS Record: www is a CNAME record pointing to the IP address of the server.
Web Server (Nginx): Serves static content and handles HTTP requests.
Application Server: Runs the dynamic content and business logic.
Database (MySQL): Stores and manages data.
Communication: The server communicates with the user's computer using HTTP/HTTPS protocols.
Issues
Single Point of Failure (SPOF)
Downtime: Maintenance causes downtime.
Scalability: Limited by a single server’s capacity.
1. Distributed Web Infrastructure
Goal: Improve the infrastructure with multiple servers for load distribution and increased reliability.

Requirements
2 Servers
1 Web Server (Nginx)
1 Application Server
1 Load Balancer (HAProxy)
1 Set of Application Files (code base)
1 Database (MySQL)
Explanation
Load Balancer (HAProxy): Distributes incoming traffic across multiple servers using a distribution algorithm (e.g., round-robin).
Active-Active vs. Active-Passive:
Active-Active: All servers handle traffic simultaneously.
Active-Passive: One server is on standby.
Database Cluster: Primary-Replica setup for redundancy and read scalability.
Primary Node: Handles write operations.
Replica Node: Handles read operations.
Issues
SPOF: Potential single points of failure.
Security: No firewall or HTTPS.
Monitoring: No monitoring in place.
2. Secured and Monitored Web Infrastructure
Goal: Secure the infrastructure, ensure encrypted traffic, and add monitoring.

Requirements
3 Firewalls
1 SSL Certificate: Serve www.foobar.com over HTTPS.
3 Monitoring Clients: Data collectors for monitoring services like Sumologic.
Explanation
Firewalls: Protect the network by controlling incoming and outgoing traffic.
HTTPS: Encrypts data transmitted between the client and the server.
Monitoring: Tracks system performance and alerts on issues.
Data Collection: Monitoring tools collect metrics and logs for analysis.
Monitoring QPS (Queries Per Second): Tracks the number of queries handled by the server to gauge performance.
Issues
SSL Termination: At the load balancer level might be insecure.
Single Write-capable MySQL Server: A single point of failure.
Identical Servers: Might cause inefficiencies and potential failures.
3. Scale Up
Goal: Enhance the infrastructure to handle more traffic by adding more servers and load balancing.

Requirements
1 Additional Server
1 Load Balancer (HAProxy): Configured as a cluster with the existing one.
Separate Servers: For web server, application server, and database.
Explanation
Separation of Concerns: Each server handles a specific component, improving scalability and reliability.
