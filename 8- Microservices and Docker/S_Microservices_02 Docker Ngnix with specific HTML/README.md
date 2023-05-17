# Microservices 1 - Task 1 - NGINX With Docker Container

**Presented to:**    
_Mohammed Amr_    

**Presented by:**   
_Islam Khaled_    

17 May 2023

-----------------------------------------
## Code Files:

- Code files Provided here : 
- [Dockerfile](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/8-%20Microservices%20and%20Docker/S_Microservices_02%20Docker%20Ngnix%20with%20specific%20HTML/Dockerfile)
```
# Use the official Nginx base image
FROM nginx

# Copy the HTML content to the default Nginx web server directory
COPY index.html /usr/share/nginx/html
```
- [index.heml](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/8-%20Microservices%20and%20Docker/S_Microservices_02%20Docker%20Ngnix%20with%20specific%20HTML/index.html)
```
<!DOCTYPE html>
<html>
<head>
    <title>My Dockerized Web Server</title>
</head>
<body>
    <h1>Welcome to my Dockerized Web Server!</h1>
    <p>This is a sample HTML file served by Nginx inside a Docker container.</p>
</body>
</html>
```

-----------------------------------------
## Build and Run Image:

- Build and run docker image:

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2a1d8f71-65b3-4fa8-b11f-2d31369c4a3b)

- Check ```Docker Desktop```:

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/95f030c2-6d56-47f7-b59a-fb6dea69b290)
![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/08e6b873-4bfe-44d8-b3fe-3c061bae4042)

- Terminal output:

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/527c5aa5-4213-47f1-b273-02410df6b7b5)

- Web output:

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/34374f68-0359-42cc-bb5f-b6297735e901)

-----------------------------------------
