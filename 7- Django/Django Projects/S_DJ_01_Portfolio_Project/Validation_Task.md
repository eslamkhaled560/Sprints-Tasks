# Django Session 3 - Task 3 - Forms and Validations

**Presented to:**    
_Aya Gebreel_    

**Presented by:**   
_Islam Khaled_    

15 May 2023

__The complete project exists in the repo you can check it from the path above or from this link [Project](https://github.com/eslamkhaled560/Sprints-Tasks/tree/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project), You will find another ```README.md```, It was for Task 2.    
Sorry for any inconvenience.__
-----------------------------------------
## Project Initialization:

- Activate the environment and work inside last project app ```myapp```:

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/fea9f967-dfcd-4031-abe7-1577324d7dde)
![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/6ac18a7f-9ee8-488d-a8a0-89a5cd85f01c)

-----------------------------------------
## Model, Form and Validation:

- Create new model called ```Post```:
- Code File >> [models.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/models.py)

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/5acb8945-3d29-4502-a6bc-1146aa197873)

- Make migrations and migrate:
- Code File >> [0002_post.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/migrations/0002_post.py)

![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2a8e664e-5a6d-4c46-b8cd-34255c7d0c88)
![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/6818cf2f-762e-400d-9db1-b1550c159003)

- Create ```forms.py``` with validation function ```clean```:
- Code File >> [forms.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/forms.py)

![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/9c2702aa-2657-4208-9a0b-c2d170a549ee)

- Create two fuctions in ```views.py```: ```home_list``` function is used after clicking submit to view the data if it's valid.
- Code File >> [views.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/views.py)

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/66857333-6c8a-4b37-8a31-3c2cad5dc2f7)

- Create ```home.html``` in myapp/templates that contains the form:
- Code File >> [home.html](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/templates/home.html)

![8](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/76498732-19c6-45b7-b45f-0120b3f2a655)

- Create ```home_list.html``` that return the data list, with a button goes back to home page to add more data:
- Code File >> [home_list.html](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/templates/home_list.html)

![9](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/b3bae06f-d441-475d-8585-7a33ffb9eb44)

- Add path for the new html files in ```urls.py```:
- Code File >> [urls.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/urls.py)

![10](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/41e40fd0-3a50-4dd6-a4be-c2e3cf8185f6)

- Run server and view form output:

![11](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/4a814dc2-ac02-48c4-aa62-f55760b2f7e3)
![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/88624ea2-ab17-4361-9cd0-d360bce4253a)

- Check shell to make sure:

![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/baf41580-55a2-4c14-8846-443ccf0fcfd2)

-----------------------------------------
## Django Admin:

- Create a super user:

![13](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/80510061-d26a-450c-afda-ac20c226209c)

- Update ```admin.py``` to include ```Post``` table with a better layout:
- Code File >> [admin.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/admin.py)

![14](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/51332f38-39a5-428e-ab77-8cd9f824003e)

- Run server and log into Django admin:

![15](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/36b50c98-71ab-4251-87b6-c4db4c09a637)
![16](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/e52673e3-eb84-4bd9-b3eb-b3fec9288a34)

- Manipulte Django Admin:

![20](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/6c7f810e-f507-4da2-8ced-ca2a892f4db0)

-----------------------------------------
