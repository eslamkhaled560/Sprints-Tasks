# Docker Basic Commands - Task 1

**Presented to:**    
_Sabreen Salama_    

**Presented by:**   
_Islam Khaled_    

24 May 2023

-----------------------------------------
## 1- Check the docker version installed

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1c098e59-426b-4f72-9a95-bf877bdc2aa8)

## 2- Run docker container for hello-world

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e872a6b3-5334-438c-8644-cc9a3216628f)

## 3- Run docker container redis in detached mode

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/8f3b7da7-4241-4539-bfce-a682a8e33705)

## 4- Try to stop the running redis container and check the present container on the host

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/c733d488-67bc-4659-8e1c-0c9ed8e485db)

## 5- Check the ID of the redis container

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/ac85ae4c-4022-47c0-835f-79d605cfcf76)

## 6- Try to run a container from nginx:alpine and delete image
Can't force deletion of images with running containers, we should stop it first and then force.

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/cdab2217-7cce-4a79-b447-f548eae35f46)

## 7- Delete the image redis

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d72b4b1a-c714-4fcc-ab1a-fcaf998f0c9e)

## 8- Pull image from nginx:1.14-alpine

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/ecfa9b76-f85f-47b8-ad9c-a43e7f8f8616)

## Run an instance of the ubuntu image to run the sleep 1000 command at startup and Exec into the container and touch a file called test-file

![9](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/0f4a9048-f169-48b6-bb71-7d6ea8a4f953)

## 9- Run a container with the nginx:alpine image and name it web

![10](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/bf013e42-be36-4686-b634-38299a72f052)

## 10- Delete all the images from the host
- We can use this command on powershell to delete all images ```docker rmi -f $(docker images -q)``` as we pass images IDs to the remove command.      
- As a safer option we can use ```docker image prune -a```: This command will delete all unused images on the host, freeing up disk space.

I will delete only images used in this task.

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/17e32920-51f7-4af9-ba9f-f77709be1627)      

![13](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/cccc5e4b-85a8-42c1-94f8-da4d4d13a856)

-----------------------------------------
