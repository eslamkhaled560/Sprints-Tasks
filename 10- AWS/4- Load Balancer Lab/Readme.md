# AWS Lab 4 - Load Balancers

**Presented to:**    
_Sabreen Salama_    

**Presented by:**   
_Islam Khaled_    

9 June 2023

-----------------------------------------
## 1- Launch a jump host

- Instances Ips

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/f2c1b586-71a7-4ad6-953d-275b3f6dde88)
![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/18b951ff-21f4-4d0d-8a07-eab0aa721887)

- SSH to the jumphost

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/0abf6f2b-4107-40a6-ad64-f46269fca842)

- SSH from bastion to the private machine

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/91c6c423-ca6f-4e5a-9aba-2f3480b8fe1f)

-----------------------------------------
## 2- Implement the below diagram

- Private apache IPs

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/777ddf22-528b-4784-9ee0-a61e80faab57)
![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/66b595ac-d870-4668-afee-bd316096dbf1)

- Healthy target groups

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d7fd5039-3727-4d92-9e7b-69db3e3a2f91)
![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/03da3d68-14be-4ef3-9683-8b4a764d0f24)

- DNS of the public load balancer 

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/12c0f942-7ede-45d8-921c-c037eba27d19)
![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/c0154802-3266-482d-8e6d-ff32b46c0303)

-----------------------------------------
## 3- Implement the below diagram with autoscaling:

- Autoscaling group

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/9fedd831-2ca0-4a58-befe-2ad1f8b95216)

- Healthy target groups

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/61d65e37-7cf0-4852-b366-9e63b8a28ab8)
![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e739866f-ee52-47bf-ad33-c9b5048d4af6)

- Private apache instances

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/47dd5d09-db3b-4134-a3cf-e639b66c0a3f)
![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/8580ba57-2ec9-4347-b554-6b29d5207ea6)

- Public load balancers dns

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/73a49b6d-4a7a-4ddb-85f5-d8bc095ff310)
![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/3c84f7fa-d93f-46cd-8e41-765df8a78bdb)

-----------------------------------------
