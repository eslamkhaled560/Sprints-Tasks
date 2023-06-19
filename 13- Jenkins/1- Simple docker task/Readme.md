# Jenkins Task 1

**Presented to:**    
_Mohamed Swelam_    

**Presented by:**   
_Islam Khaled_    

19 June 2023

-----------------------------------------
## 1- What is Jenkins used for?

Jenkins is an open source continuous integration/continuous delivery and 
deployment (CI/CD) automation software DevOps tool.    
- Jenkins allows developers to integrate their code changes frequently into a shared repository.
- Jenkins facilitates the automation of software delivery pipelines. It can deploy applications to various environments.
- Jenkins supports various build tools, such as Maven, Gradle.
- Jenkins has a vast plugin ecosystem that extends its functionality. 

-----------------------------------------
## 2- Install jenkins with docker image.

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/0c2aad4b-1880-40eb-a943-d095753a9000)
![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d3eb487d-5d65-45b7-b366-946ff5cac758)
![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/b46d1284-fb36-4c31-934c-61229c188686)

-----------------------------------------
## 3- what is plugins in jenkins ?

Plugins are the primary means of enhancing the functionality of a Jenkins 
environment to suit organization needs. They help extend 
Jenkins' capabilities and integrate Jenkins with other software such as building tools
like ```maven``` and ```npm```.

-----------------------------------------
## 4- Create free style project and link it to private git repo containing any dockerfile then build an image from this dockerfile and push it to private docker repo

I used 2 approaches __(VM, WSL)__ in this section because I encouuntered and error using VMm and it will be illustrated below and how i fixed it.

- [Link to the used repository.](https://github.com/ianmiell/simple-dockerfile)

### 1- VM approach

- Creating ```simple-docker``` freestyle

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/4be31141-21dd-4f5f-8b0d-0bba4381957e)

- Configuring ```github``` and ```docker hub``` credentials:

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/9389fcfb-c5fc-44c8-ab1a-47c34acf626f)
![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1b8dc362-d7e8-42ed-b1c8-3e6db989b6c3)
![8](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/23712649-dd3a-4ad1-a670-85f984abcdc9)

- Execute Shell

![9](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/9dbba99c-84b5-4885-b023-17a2910c0ea2)

- Build output

![10](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/7f0cd12a-c688-4129-90c6-28217a7c2f9b)
![11](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/91971cee-5f07-4652-8476-7c5e8f371c03)

- My docker hub repo

![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/24174030-ed24-4340-ab3c-d6b9c0c78492)

### 2- WSL (Windows Subsystem Linux) approach

- Run jenkins container with docker configuration

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/18ecf18f-afa1-4e40-80bb-7741bf6ca18c)

- As we saw, there was a denied permission to run docker inside the jenkins container, so I should change permissions for ```docker.sock```

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/c0165c8e-182f-42c1-b42b-33182c7a0d4a)

- Configure credentials

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/ef7165ef-58cd-4ffd-9536-e2948f9bffc7)

- ```docker-simple``` freestyle configurations

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d8cfdc32-8fd4-4daf-8c9f-966c45fe0878)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/99917b21-ec95-4344-b9a4-7a07702a66b7)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1aa07e61-c4ee-4e92-96ba-b158f8fede4b)

- Build output

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1c460ef9-446a-4f01-a55b-f559dd711334)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/619c4084-690d-473d-b88f-1c123961694d)

- My docker hub

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e117b401-d81a-4ebc-83a1-9d6400eaa5af)

-----------------------------------------
