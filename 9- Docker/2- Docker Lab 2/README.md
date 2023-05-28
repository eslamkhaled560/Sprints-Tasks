# Docker Lab 2

**Presented to:**    
_Sabreen Salama_    

**Presented by:**   
_Islam Khaled_    

26 May 2023

-----------------------------------------
## 1- Run an instance of nginx:alpine with a name nginx and map port 80 on the container to 3828 on the host.

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/81d379b0-1127-4360-a8cd-221566e4ddee)

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e430ca3c-1ec9-4d9c-8bb0-32e4e57d2fa8)

## 2- Create ubuntu image and check the size of it.

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/60266130-95a4-4a0a-b5cd-22aab000009c)

## 3- Run a container named blue-app using image KodeKloud/simple-webapp and set the environmet variable APP_COLOR to blue. make the app available on port 38282 on the host. the app listens on port 8080.

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/44bec7b4-dae6-49c9-bbfc-d0b0abc0799d)

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2cd571da-8a74-436a-aa15-4d04a46c1b31)

## 4- Deploy a mysql database using the mysql image and name it mysql-db. set the database password to use db_pass123 then inspect it to check the value.

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/79ae432b-6653-408c-9ab5-6a1dce98f1a0)

![61](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/5b9efdfb-7538-4e7c-9871-72f2cc863b80)

## 5- Pull the code from https://github.com/sabreensalama/dockerize-node-app-task and create a docker file for this node app.

[Dockerfile](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/9-%20Docker/2-%20Docker%20Lab%202/dockerize-node-app-task/Dockerfile):
```
FROM node:16
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD [ "node", "server.js" ]
```

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/3aa8ff24-e99e-4cc2-844a-634c8378d928)

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/bafcf8f6-be13-4601-aae0-72bd53744c22)

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/30ad33b9-12fc-4cb5-acba-3f9c03d442aa)

## 6- Create a volume called mysql_data, run a mysql container again, but this time map a volume to the container so that the data stored by the container is stored at /opt/data on the host. use the same name : mysql-db and same password : db_pass123 as before. Mysql stores data at /var/lib/mysql inside the container.

![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/8a4bca5d-c5f0-4419-8403-101e064b0f92)

-----------------------------------------
