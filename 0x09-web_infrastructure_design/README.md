# Web infrastructure design


[0. Simple web stack](0-simple_web_stack)
- This is a simple web infrastructure composed of a single server with a LAMP stack.
- It features the following:
	- 1 server
	- 1 web server (Nginx)
	- 1 application server
	- 1 application files (code base)
	- 1 database (MySQL)
	- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

[1. Distributed web infrastructure](1-distributed_web_infrastructure)
- This is a three server web infrastructure that hosts the website www.foobar.com.
- It features the following:
	- 3 servers
	- 2 web server (Nginx)
	- 2 application server
	- 1 load-balancer (HAproxy)
	- 2 set of application files (code base)
	- 2 database (MySQL)

[2. Secured and monitored web infrastructure](2-secured_and_monitored_web_infrastructure)
- This is a three server web infrastructure that hosts the website www.foobar.com where meeting the demands that it is secured, serve encrypted traffic, and monitored.
- It features the following:
	- 3 servers
	- 2 web server (Nginx)
	- 2 application server
	- 1 load-balancer (HAproxy)
	- 2 set of application files (code base)
	- 2 database (MySQL)
	- 3 firewalls
	- 1 SSL certificate to serve www.foobar.com over HTTPS
	- 3 monitoring clients (data collector for Sumologic or other monitoring services)

[3. Scale up](3-scale_up)
- This is a three server web infrastructure that hosts the website www.foobar.com where meeting the demands that it is secured, serve encrypted traffic, and monitored.
	- 4 servers
	- 2 web server (Nginx)
	- 2 application server
	- 2 load-balancer (HAproxy) configured as cluster 
	- 2 set of application files (code base)
	- 2 database (MySQL)
	- 3 firewalls
	- 2 SSL certificate to serve www.foobar.com over HTTPS
	- 4 monitoring clients (data collector for Sumologic or other monitoring services)
