# NGINX TASK Part 2

**Presented to:**    
_Mohammed Omar_    

**Presented by:**   
_Islam Khaled_    

11 June 2023

-----------------------------------------
I used AWS ubuntu instance to complete this task.

-----------------------------------------
## Configure the same website to serve traffic with SSL self signed certificate
1- AWS instance

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/7b67a74d-65b4-411d-a958-bc7b0d0ca4b8)

2- Configure domain name in ```hosts``` file

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/cfea2f10-9dfa-4f6d-b978-102b7eff3c32)
![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2d666065-1f31-405a-b9d8-536f770fe7e6)

3- Configure ```/etc/nginx/sites-enabled/default``` with SSL certificate

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/44996333-f9b3-4d40-8d79-05fa68935ed8)

4- Self-trust certificate authority

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/b6d8c9c7-5a04-447d-a4b1-962dc2d2253e)

5- Secured Domain ```https://islam-khaled.com```

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/40334a23-7199-480e-b42b-d677d83c4ef1)

-----------------------------------------