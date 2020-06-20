# API YAMDB

Second project completed at Yandex Praktikum

### Description

YAMDB allows users to review and rate music, movies, books etc. Reviews can be commented. 

Multiple **user roles** are available.

* **Administrator**. Assigned by Project-manager (superuser). Has rights to assign user roles, create, modify and delete genres, categories, users and titles.
* **Moderator**. Assigned by Administrator. Can create, modify and delete reviews and comments.
* **User**. Default role after registration. Can modify his own profile. Has rights to create reviews, comment reviews and rate titles. Modification of his own reviews and comments is allowed.
* **Anonymous user** can retrieve all reviews, titles, categories, genres and comments or specific instance of them.

**Registration pattern.**

* Make **POST** request with a **_username_** and **_email_** to ```api/v1/auth/email/``` in order to obtain **_confirmation code_**.
* Make **POST** request with used **_email_** and **_confirmation code_** to ```api/v1/auth/token/``` in order to obtain **_JWT Token_**.
* _optional_ Modify your own profile by making **PATCH** request to ```users/me/```.
 
#### Request samples and full documentation is available at ```/redoc/``` ####

### Usage

Install requirements using

```pip install -r requirements.txt```

and you will be able to run project locally.
