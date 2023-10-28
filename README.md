# School Management System
The School Management System is a Python command-line application that simplifies the management of student records, subjects, and marks.
This system offers an efficient way to maintain and access essential data related to students and subjects in an educational institution.

**Table of Contents**
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Documentation](#documentation)
  - [Main Menu](#main-menu)
  - [Student Management](#student-management)
  - [Subject Management](#subject-management)
  - [Marks Management](#marks-management)
  - [View Information](#view-information)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The School Management System is a command-line application designed to help you manage student records, subjects, and marks efficiently. This system provides functionalities for:

- Adding, updating, and deleting student records.
- Adding, updating, and deleting subject records.
- Adding, updating, and deleting marks for students in specific subjects.
- Viewing student details, marks, and filtering students based on various criteria.

## Installation

To set up the required database and tables for the School Management System, follow these steps:

### 1. **Clone the Repository**: Begin by cloning the repository to your local machine. Use the following command:
    git clone https://github.com/AllTechz/school-management-system.git

### 2. **Navigate to the Project Directory**: Move to the project directory using the `cd` command:
cd school-management-system

### 3. **Install Required Python Packages**: Install the necessary Python packages, primarily the `mysql-connector-python`. You can do this by running:
pip install mysql-connector-python

### 4. **Database Setup**: Execute the following SQL commands to create the required database and tables:

```sql
-- Create the school_management database
CREATE DATABASE school_management;

-- Switch to the new database
USE school_management;

-- Create the Students table
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    contact_info VARCHAR(20) NOT NULL,
    class VARCHAR(10) NOT NULL
);

-- Create the Subjects table
CREATE TABLE Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(255) NOT NULL
);

-- Create the Marks table
CREATE TABLE Marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    mark DECIMAL(5,2),
    date_recorded DATE
);
```
These SQL commands will create the necessary database and tables for the School Management System to function.

These tables serve as the backbone of the application, enabling the seamless management of student records, subjects, and marks. Here's a brief overview of each table's purpose:

- The `Students` table stores student information, including names, dates of birth, contact details, and class levels. Each student is uniquely identified by a `student_id`.

- The `Subjects` table keeps track of the subjects offered at your educational institution. It uses `subject_id` for identification.

- The `Marks` table records students' marks in various subjects, including the student's `student_id`, the subject's `subject_id`, the mark itself, and the date when the mark was recorded.

By executing these SQL commands, you establish the foundation for efficient school management and academic record-keeping.

### 5. **Setting up MySQL Connector and Database Configuration**

Before you can run the School Management System, you need to configure the MySQL connector with your database credentials. Follow these steps to set it up:

 1. **Open the `main.py` file**: In the `main.py` file, look for the following lines of code near the beginning of the script:

    ```python
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="school_management"
    )
    ```

 2. **Modify the MySQL Connection Parameters**: Replace the default values for `user`, `password`, and other connection parameters with your MySQL database credentials. You'll need to change the `user` and `password` values to match your MySQL username and password. Update the `host` if your MySQL server is running on a different host or port.

    For example:

    ```python
    db = mysql.connector.connect(
        host="your-mysql-server",
        user="your-username",
        password="your-password",
        database="school_management"
    ```

    Make sure to replace `"your-mysql-server"`, `"your-username"`, and `"your-password"` with your specific MySQL server details.

 3. **Populate the Database with Sample Data (Optional)**:

    In this repository, you'll find a Python script named `populate_database.py` that you can use to add sample data to your database. It's a helpful tool for testing and understanding how the School Management System works.
    - Before using this script, you need to chnage the values of database credentials in `populate_database.py`.

    - To use the script, run the following command in your terminal:

          python populate_database.py

    - The script will populate the database with sample student records, subjects, and marks.


### 6. **Run the Application**: Finally, run the Python script to launch the School Management System:
python school_management.py

With the database and tables in place, the application is ready to help you streamline your school's administrative tasks and academic management.

By including the additional information, users gain a deeper understanding of the purpose of each table and how they contribute to the functionality of the School Management System.

## Usage

Upon running the program, you will have access to a menu-driven interface. You can navigate through the available options to perform various actions, such as managing student records, subjects, and marks. The system provides detailed feedback on the actions you perform.

## Features

- **Student Management**: Add, update, and delete student records.
- **Subject Management**: Add, update, and delete subject records.
- **Marks Management**: Add, update, and delete marks for students in specific subjects.
- **View Information**: View student details, marks, and filter students based on criteria like class, name, and average percentage.

## Documentation

### Main Menu

The main menu provides the following options:

1. **Student Management**: Access student management features.
2. **Subject Management**: Access subject management features.
3. **Marks Management**: Access marks management features.
4. **View Information**: Access features to view student and subject information.
5. **Exit**: Close the program.

### Student Management

Under Student Management, you can perform the following actions:

1. **Add Student Record**: Add a new student record to the system.
2. **Update Student Information**: Update an existing student's information.
3. **Delete Student Record**: Delete a student's record from the system.
4. **Back to Main Menu**: Return to the main menu.

### Subject Management

Subject Management offers the following options:

1. **Add Subject**: Add a new subject to the system.
2. **Update Subject**: Update an existing subject's name.
3. **Delete Subject**: Delete a subject from the system.
4. **Back to Main Menu**: Return to the main menu.

### Marks Management

In the Marks Management section, you can perform the following actions:

1. **Add Marks**: Add marks for a student in a specific subject.
2. **Update Marks**: Update the marks for a student in a specific subject.
3. **Delete Marks**: Delete marks for a student in a specific subject.
4. **Back to Main Menu**: Return to the main menu.

### View Information

View Information provides the following options:

1. **View Student Details**: View detailed information about a specific student.
2. **View Student Marks**: View marks for a specific student.
3. **Filter Students by (class, name, avg percentage)**: Filter and view a list of students based on class, name, or average percentage.
4. **View all Subjects**: View a list of all subjects.
5. **Back to Main Menu**: Return to the main menu.

## Contributing

We welcome contributions to this project. If you have any improvements, bug fixes, or new features to add, please feel free to create a pull request on our GitHub repository.

## License

This School Management System is licensed under the [MIT License](LICENSE). You are free to use and modify the code as per the terms of this license.
