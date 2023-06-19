# Jenkins Task 1

**Presented to:**    
_Mohamed Swelam_    

**Presented by:**   
_Islam Khaled_    

19 June 2023

-----------------------------------------
-----------------------------------------
## 1- What is Jenkins used for?

Jenkins is an open source continuous integration/continuous delivery and 
deployment (CI/CD) automation software DevOps tool.    
- Jenkins allows developers to integrate their code changes frequently into a shared repository.
- Jenkins facilitates the automation of software delivery pipelines. It can deploy applications to various environments.
- Jenkins supports various build tools, such as Maven, Gradle.
- Jenkins has a vast plugin ecosystem that extends its functionality. 

-----------------------------------------
-----------------------------------------
## 2- Install jenkins with docker image.

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e4694e49-3db5-4db3-8da8-b26277edea42)
![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d3eb487d-5d65-45b7-b366-946ff5cac758)
![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/b46d1284-fb36-4c31-934c-61229c188686)

-----------------------------------------
-----------------------------------------
## 3- what is plugins in jenkins ?

Plugins are the primary means of enhancing the functionality of a Jenkins 
environment to suit organization needs. They help extend 
Jenkins' capabilities and integrate Jenkins with other software such as building tools
like ```maven``` and ```npm```.

-----------------------------------------
-----------------------------------------
## 4- Create free style project and link it to private git repo containing any dockerfile then build an image from this dockerfile and push it to private docker repo

I used 2 approaches __(VM, WSL)__ in this section because I encountered and error using VM and I fixed it. everything will be illustrated below.

- [Link to the used repository.](https://github.com/ianmiell/simple-dockerfile)

-----------------------------------------
### 1- VM approach with modified jenkins image

- When I try to access docker inside the jenkins container I get this error

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/21e0e6d3-9926-431a-9656-65409b0a0925)

- After searching I knew the reason

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/5dfe6fc4-446a-466f-ad02-6a94fea0f174)

- The solusion is to use this [Dockerfile](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/13-%20Jenkins/1-%20Simple%20docker%20task/Dockerfile) to build the jenkins image with docker
```
FROM jenkins/jenkins:lts
USER root
RUN apt-get update -y
RUN apt-get install apt-transport-https curl gnupg-agent ca-certificates software-properties-common -y
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y
RUN apt-get update -y
RUN apt-get install docker-ce docker-ce-cli containerd.io -y

RUN usermod -aG docker jenkins
```
- Build modified image

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/6e379c72-3a45-4b3c-9017-ae3aa0e839a0)

- Run modified image, now docker is working inside the jenkins container

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/49e5de8c-fc99-4a70-81f7-2fcf46da6c10)

- Configuring ```github``` and ```docker hub``` credentials:

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/324fce43-8bf8-4239-9b93-d9c0be4a253f)

- Configure ```simple-docker``` freestyle

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1b8dc362-d7e8-42ed-b1c8-3e6db989b6c3)
![8](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/23712649-dd3a-4ad1-a670-85f984abcdc9)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/38bd2116-1a28-4fa5-9874-3b5121fc97c8)

- Build output

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/c674da41-ac69-4041-943d-bad9b22984e8)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/15a73f51-8c51-4f8e-9f04-1896940aadcf)

- My private docker hub repo 
  > Note that the ```wsl``` tag created first, steps are provided below

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/7d99a663-0159-4a18-b9a3-5dcddbd0bfe9)

-----------------------------------------
### 2- WSL (Windows Subsystem Linux) approach with basic jenkins lts image

- Run jenkins container with docker configuration

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/18ecf18f-afa1-4e40-80bb-7741bf6ca18c)

- As we saw, there was a denied permission to run docker inside the jenkins container, so I should change permissions for ```docker.sock```

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/c0165c8e-182f-42c1-b42b-33182c7a0d4a)

- Configure credentials

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/ef7165ef-58cd-4ffd-9536-e2948f9bffc7)

- ```docker-simple``` freestyle configurations

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d8cfdc32-8fd4-4daf-8c9f-966c45fe0878)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/99917b21-ec95-4344-b9a4-7a07702a66b7)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/f0b5715a-a30b-4c4e-a6c1-78f7a5b631d2)

- Build output

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/dd8068f9-2683-40b3-9da9-58378e8d0252)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/91fc7e8d-3bfb-4faf-9c00-c0af0f38b6ff)

- My private docker hub repo

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/8291c8c8-f865-42f0-a240-223a95218a0d)

-----------------------------------------
-----------------------------------------
