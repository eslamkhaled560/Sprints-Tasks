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

- [Link to used repo](https://github.com/ianmiell/simple-dockerfile).
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

-----------------------------------------
