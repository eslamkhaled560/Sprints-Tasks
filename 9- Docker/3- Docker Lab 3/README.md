# Docker Lab 3

**Presented to:**    
_Sabreen Salama_    

**Presented by:**   
_Islam Khaled_    

29 May 2023

-----------------------------------------
## Problem 1:

Create bridge network with subnet 192.168.0.0/24. Run 2 containers and attach containers to this network. Create another bridge network with subnet 10.5.0.0/24. Run any container and attach it to the new network. Make sure that the containers at different network can’t ping each other

In this problem I used ```RUN apt-get update && apt-get install -y iputils-ping``` command inside the ```nginx``` container to be able to ping on the ```redis(ip=10.5.0.2)``` container.

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e2132342-7135-4a54-b5b0-cb0c014ee911)

## Problem 2:

Create static html file >> [index.html](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/2-%20Dockreized%20httpd/index.html)                
Write Dockerfile to build image based on httpd to host the html file >> [Dockerfile](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/2-%20Dockreized%20httpd/Dockerfile)        
 Copy a new configuration file to listen on port 9999 instead of 80 >> [httpd.conf](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/2-%20Dockreized%20httpd/httpd.conf)      

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/88b27243-cef2-49fd-82c2-850081a47ff3)
![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/6e1bc75a-dc7f-499e-9901-4bce79a61ab7)

## Problem 3:

Create a docker compose to up mysql container >> [docker-compose.yml](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/3-%20Docker%20compose%20mysql%20and%20node%20app/docker-compose.yml)                 
and https://github.com/sabreensalama/dockerize-node-app-task which depend on mysqldb >> [Dockerfile](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/3-%20Docker%20compose%20mysql%20and%20node%20app/Dockerfile)                               
Add volume for mysqldb

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/cd328aff-ec7e-41fd-b049-e1e45471edf7)
![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/191c2503-8035-4f57-9c9e-aab5ad4685d1)

## Problem 4:

Use docker compose to deploy ghost platform (image: ghost:1-alpine)(Ghost is a free and open source blogging platform written in JavaScript) Use mysql database instead of sqlite >> [docker-compose.yml](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/3-%20Docker%20Lab%203/4-%20Docker%20compose%20ghost/docker-compose.yml)

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/366ee803-7c9b-4be2-b416-ac28ba9c9422)
![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/856f0c0f-8530-4b86-bbf0-85ccb8ef226e)
![9](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2fd60145-fea1-41ee-a84e-4702a7c21c87)

-----------------------------------------
