# Django-School-Portal API Documentation

Detailed Documentation of the API's endpoints, as well as others concepts.

---

# Table of Contents
- [API Overview](#api-overview)
    - [Authentication](#authentication)
    - [Users](#users)
    - [Student Profiles](#student-profiles)
    - [Teacher Profiles](#teacher-profiles)
    - [Admin Profiles](#admin-profiles)
    - [Subjects](#subjects)
    - [Grades](#grades)
    - [Messages](#messages)


## API Overview 🔬

There are dozens of API endpoints, and each of them allow for a trailing backslash or not, depending on the preferences of the developer consuming the endpoints.

<br>

### Authentication

METHOD   | ENDPOINT                   | FUNCTIONALITY
------   | -------------------------- | -------------
_GET_    | `/api/auth/login/`         | Get a user's access and refresh token
_POST_   | `/api/auth/login/refresh/` | Generate an access token from a refresh token
_PUT_    | `/api/auth/logout/`        | Blacklist a user's refresh token 

<br>

### Users

METHOD   | ENDPOINT           | FUNCTIONALITY 
------   | ------------------ | ------------- 
_GET_    | `/api/users/`      | Get all users 
_POST_   | `/api/users/`      | Create a user 
_PUT_    | `/api/users/{pk}/` | Completely update a user
_PATCH_  | `/api/users/{pk}/` | Partially update a user
_DELETE_ | `/api/users/{pk}/` | Delete a user

<br>

### Student Profiles

METHOD   | ENDPOINT                      | FUNCTIONALITY
------   | ----------------------------- | -------------
_GET_    | `/api/student-profiles/`      | Get all student profiles
_POST_   | `/api/student-profiles/`      | Create a student profile
_PUT_    | `/api/student-profiles/{pk}/` | Completely update a student profile
_PATCH_  | `/api/student-profiles/{pk}/` | Partially update a student profile
_DELETE_ | `/api/student-profiles/{pk}/` | Delete a student profile

<br>

### Teacher Profiles

METHOD   | ENDPOINT                      | FUNCTIONALITY
------   | ----------------------------- | -------------
_GET_    | `/api/teacher-profiles/`      | Get all teacher profiles
_POST_   | `/api/teacher-profiles/`      | Create a teacher profile
_PUT_    | `/api/teacher-profiles/{pk}/` | Completely update a teacher profile
_PATCH_  | `/api/teacher-profiles/{pk}/` | Partially update a teacher profile
_DELETE_ | `/api/teacher-profiles/{pk}/` | Delete a teacher profile

<br>

### Admin Profiles

METHOD   | ENDPOINT                    | FUNCTIONALITY
------   | --------------------------- | -------------
_GET_    | `/api/admin-profiles/`      | Get all admin profiles
_POST_   | `/api/admin-profiles/`      | Create an admin profile
_PUT_    | `/api/admin-profiles/{pk}/` | Completely update an admin profile
_PATCH_  | `/api/admin-profiles/{pk}/` | Partially update an admin profile
_DELETE_ | `/api/admin-profiles/{pk}/` | Delete an admin profile

<br>

### Subjects

METHOD   | ENDPOINT              | FUNCTIONALITY
------   | --------------------- | -------------
_GET_    | `/api/subjects/`      | Get all subjects
_POST_   | `/api/subjects/`      | Create a subject
_PUT_    | `/api/subjects/{pk}/` | Completely update a subject
_PATCH_  | `/api/subjects/{pk}/` | Partially update a subject
_DELETE_ | `/api/subjects/{pk}/` | Delete a subject

<br>

### Grades

METHOD   | ENDPOINT            | FUNCTIONALITY
------   | ------------------- | -------------
_GET_    | `/api/grades/`      | Get all grades
_POST_   | `/api/grades/`      | Create a grade
_PUT_    | `/api/grades/{pk}/` | Completely update a grade
_PATCH_  | `/api/grades/{pk}/` | Partially update a grade
_DELETE_ | `/api/grades/{pk}/` | Delete a grade

<br>

### Messages

Alias - #ftcau (from the currently authenticated user)   
Alias - #otcau (of the currently authenticated user)

`ALL` 

METHOD   | ENDPOINT              | FUNCTIONALITY
------   | --------------------- | -------------
_GET_    | `/api/messages/`      | Get all messages
_GET_    | `/api/messages/{pk}/` | Retrieve a message

`Sent`

METHOD   | ENDPOINT                   | FUNCTIONALITY
------   | -------------------------- | -------------
_GET_    | `/api/messages/sent/`      | Get all sent messages #ftcau
_POST_   | `/api/messages/sent/`      | Send a messsage #ftcau
_GET_    | `/api/messages/sent/{pk}`  | Retrieve a message sent #ftcau
_PUT_    | `/api/messages/sent/{pk}/` | Completely update a sent message #ftcau
_PATCH_  | `/api/messages/sent/{pk}/` | Partially update a sent message #ftcau
_DELETE_ | `/api/messages/sent/{pk}/` | Delete a sent message #ftcau

`Received`

METHOD   | ENDPOINT                       | FUNCTIONALITY
------   | ------------------------------ | -------------
_GET_    | `/api/messages/received/`      | Get all received messages #otcau
_GET_    | `/api/messages/received/{pk}/` | Retrieve a received message #otcau
