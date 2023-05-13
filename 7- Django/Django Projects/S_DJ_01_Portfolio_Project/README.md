# Django Session 2 - Task 2 - Django Models

**Presented to:**    
_Aya Gebreel_    

**Presented by:**   
_Islam Khaled_    

13 May 2023

-----------------------------------------
## Project Initialization:

- I worked with the same environment from the first task ```Dj-env```, as all I need is Django and It's already installed there.

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/d15d2c41-ad21-45a4-9094-2f2b8b280499)

- Activate existing environment and start new project called ```S_DJ_01_Portfolio_Project```:

![1](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/35ec6239-922c-44bf-9cea-824eae40b5cd)

- Start new app called ```myapp```:

![2](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/516509a7-108d-43ef-8e46-05597bcd1a82)

- Run the server on port 8000 and check it:

![3](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/86fee5e3-af17-4c83-8537-075c490f0e2a)
![4](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2e1f1af9-24df-447e-9ca6-16e55ea73662)

-----------------------------------------
## Creating Models:

- Open project on PyCharm and Define our two models in ```myapp/models.py``` file:
- Code File >> [myapp/models.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/models.py)

![5](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/94ff1ec8-314b-4dd2-b1ee-15416d226125)

- Create the database tables for our models:   
                  
  > It looks like there is something wrong! the system didn't detect changes in models.py file.                
![6](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/89bf17d8-7602-482c-9839-01c929918b33)

- Add ```myapp``` to INSTALLED_APPS in ```settings.py``` file:
- Code File >> [S_DJ_01_Portfolio_Project/settings.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/S_DJ_01_Portfolio_Project/settings.py)

![7](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/5f2de9b3-00d2-45bd-ac61-a5fb46b99b63)

- Create the database tables again:

![9](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/1b2b7537-b280-4ee5-8bbe-928266656447)

- Check ```myapp/migrations``` directory:
- Code File >> [myapp/migrations](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/migrations/0001_initial.py)

![8](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/7b7acd3a-02e6-411b-854c-f2c98dda9e02)

-----------------------------------------
## Shell CRUD Operations:

- Open the Django shell and Import models:

### Students CRUD:

- Create:

![10](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/197e083c-1133-4d45-935d-4930de42f239)

- Retrieve:

![11](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/a49be41b-00a6-4d60-845a-387bdc02eb03)

- Update:

![12](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/484c6d25-478e-4583-802e-b122a37daf59)

- Delete:

![13](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/86bc25ec-9923-457e-8dff-4255fd505b5c)

### Courses CRUD:

- Create and Retrieve:

![14](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/b22df7ba-d85e-4986-b8cc-f89d0fb69557)

- Update:

![15](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/90979684-88c1-4d02-933c-faa9969dd269)

- Delete:

![16](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/adce3525-c07d-4d38-8e00-aa48a9924402)

-----------------------------------------
## Function-Based Views:

- Create two views called __student_list__ and __course_list__ in ```myapp/views.py```:
- Code File >> [myapp/views.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/views.py)

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/164c9541-937b-4c36-8f81-97f58f40e4ad)

- Create new templates __student_list.html__ and __course_list.html__ in the ```myapp/templates``` directory:
- Code Files >> [myapp/templates/student_list.html](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/templates/student_list.html)  [myapp/templates/course_list.html](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/templates/course_list.html)

![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2910ce88-580a-4ff0-b88b-7b3cbd8ed91f)
![image](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/63488427-dad2-4f54-9edc-8c3c430eb134)

- Update path in ```myapp/urls.py```:
- Code File >> [myapp/urls.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/myapp/urls.py)

![20](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/65579709-8a30-45da-9202-73c0ad4a664f)

- Include ```myapp/urls.py``` path in the main project ```S_DJ_01_Portfolio_Project/urls.py```:
- Code File >> [S_DJ_01_Portfolio_Project/urls.py](https://github.com/eslamkhaled560/Sprints-Tasks/blob/main/7-%20Django/Django%20Projects/S_DJ_01_Portfolio_Project/S_DJ_01_Portfolio_Project/urls.py)

![21](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/087f6ce9-6e90-488e-a0f5-6c99ee4a136e)

-----------------------------------------
## View Models Output:

- Run server:

![22](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/2e714dbf-a0dc-416d-b4b4-492d144b04b9)

- Student List:

![23](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/95c7f7af-a126-496d-a296-ff2fcf1d9203)

- Course List:

![24](https://github.com/eslamkhaled560/Sprints-Tasks/assets/54172897/dfdd2d7c-2f47-41c2-8ba6-fedfd84c313a)

-----------------------------------------
