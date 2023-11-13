# Django School Portal

A school management system API powered by the django web framework.

---

## Overview 🌐

This repository provides an API for a school management system. Though it's still in the development phase, on completion, 
- Students should be able to login, view their results, print them out, send messages, view announcements, e.t.c.
- Teachers should be able to upload students' results, view and edit them, view announcements, e.t.c
- Admins have a lot of control, they can create announcements, view any student's results, and perform other administrative functions on the system.  

Other functionality would be clearly stated in subsequent edits to this README.


## Documentation 📃

You can find a detailed documentation of the API's endpoints [here](DOCUMENTATION.md)

## Technologies Used 🛠

- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- Django CORS Headers
- Django Debug Toolbar
- Python-Decouple
- Whitenoise
- DRF Yasg
- Pillow

## Getting Started ✨

Here are the steps to getting this API up and running:

1.  Open your favourite terminal and navigate to a suitable directory.  

    ```bash
    cd path/to/suitable/directory/
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/TegaRorobi/Django-School-Portal.git
    ```

3. Navigate to the project directory
    ```bash
    cd Django-School-Portal
    ```

4. Set up a virtual environment  
    - Windows

        ```bash
        python -m virtualenv venv
        venv\Scripts\activate
        ```
    - Mac / Linux

        ```bash
        python3 -m virtualenv venv
        source venv/bin/activate
        ```

5. Install the project's dependencies
    - Windows

        ```bash
        python -m pip install -r requirements.txt
        ```
    - Mac / Linux

        ```bash
        python3 -m pip3 install -r requirements.txt
        ```

6. Run a Local Development server on port 8000 (or any suitable port of your choice)
    - Windows

        ```bash
        python manage.py runserver
        ```
    - Mac / Linux

        ```bash
        python3 manage.py runserver
        ```

7. That's it 🎉. Start interacting with the endpoints, as detailed in the [documentation](DOCUMENTATION.md).

    Alternatively, if you have a local server running on port 8000,
    - You could use the swagger documentation (probably [here](http://localhost:8000/api/swagger/) or at `/api/swagger/` ).
    - You could use the redoc documentation (probably [here](http://localhost:8000/api/redoc/) or at `/api/redoc/` ).
    - You could visit the endpoints URLs in the browsable API if you'd like.

