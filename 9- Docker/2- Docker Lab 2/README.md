# Docker Lab 2

**Presented to:**    
_Sabreen Salama_    

**Presented by:**   
_Islam Khaled_    

26 May 2023

-----------------------------------------
## 11- Run an instance of nginx:alpine with a name nginx and map port 80 on the container to 3828 on the host.

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/81d379b0-1127-4360-a8cd-221566e4ddee)

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e430ca3c-1ec9-4d9c-8bb0-32e4e57d2fa8)

## 12- Create ubuntu image and check the size of it.

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/60266130-95a4-4a0a-b5cd-22aab000009c)

## 13- Run a container named blue-app using image KodeKloud/simple-webapp and set the environmet variable APP_COLOR to blue. make the app available on port 38282 on the host. the app listens on port 8080.

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/44bec7b4-dae6-49c9-bbfc-d0b0abc0799d)

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2cd571da-8a74-436a-aa15-4d04a46c1b31)

## 14- Deploy a mysql database using the mysql image and name it mysql-db. set the database password to use db_pass123 then inspect it to check the value.

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/79ae432b-6653-408c-9ab5-6a1dce98f1a0)

![61](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/5b9efdfb-7538-4e7c-9871-72f2cc863b80)

## 15- Pull the code from https://github.com/sabreensalama/simple-flask-app/tree/main and create a docker file for this flask app.

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/25be8b9d-6bd2-487d-8cee-3dbab4979a99)

Dockerfile:
```
FROM python:3.8
WORKDIR /flask-app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

requirements.txt:
```
Flask==1.1.4
jinja2==2.11.3
markupsafe==2.0.1
```

![10](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2f051e54-87c9-4f76-b2b4-e09bfd633747)

![11](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/537fd918-f7c1-47b1-8ad4-d83c353664e1)

## 16- Create a volume called mysql_data, run a mysql container again, but this time map a volume to the container so that the data stored by the container is stored at /opt/data on the host. use the same name : mysql-db and same password : db_pass123 as before. Mysql stores data at /var/lib/mysql inside the container.

![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/8a4bca5d-c5f0-4419-8403-101e064b0f92)

-----------------------------------------
