# Library Management System

The Library Management System (LMS) is a comprehensive software solution designed to streamline the management and organization of library resources. It facilitates efficient handling of book collections, user authentication, and administrative operations. Key features include:

- Book Management: Add, update, and delete book records with ease, ensuring an up-to-date catalog.
- User Authentication: Provides secure login and role-based access control for administrators, librarians, and members.
- Book Issuance and Returns: Simplifies the process of issuing and returning books, reducing manual effort and errors.
- Tracking and Monitoring: Enables real-time tracking of issued books, due dates, and overdue notifications.

Designed with scalability and user-friendliness in mind, the LMS enhances operational efficiency, minimizes paperwork, and ensures seamless interaction between users and library resources. Whether for schools, universities, or public libraries, this system provides a robust framework to manage library operations effectively.

# Setting up the environment  

## MYSQL Setup

```sql
CREATE DATABASE pylibrary;
USE pylibrary;
create table books (bid varchar(20) primary key , title varchar(30) , author varchar(30) , status varchar(30));
create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
```

## Python Environment  

1. Create a Virtual Environment  

    ```
    python -m venv iimt_library
    ```

1. Activate the environment 

    - for Windows
        ```
        iimt_library\Scripts\activate
        ```
    - for MacOS / Linux
        ```
        source iimt_library/bin/activate
        ```
    > ⚠️ After activation, the terminal/command prompt will show the virtual environment name in the prompt, like `(iimt_library)`.
    
1. To Deactivate the environment after use

    ```
    deactivate
    ```

1. Install all the required packages from `requirements.txt` 

    ```
    pip install -r requirements.txt
    ```
---
