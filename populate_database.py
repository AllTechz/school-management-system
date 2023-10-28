import random
from datetime import datetime, timedelta
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="school_management"
)

cursor = db.cursor()

indian_names = [
    "Aarav Sharma",
    "Priya Patel",
    "Arjun Singh",
    "Ananya Gupta",
    "Siddharth Verma",
    "Ishita Kapoor",
    "Rohan Mehta",
    "Kritika Pandey",
    "Aditya Jain",
    "Divya Mishra",
    "Rishabh Kumar",
    "Alisha Choudhary",
    "Harsh Joshi",
    "Nisha Shah",
    "Aditi Tiwari",
    "Vikram Khanna",
    "Swati Reddy",
    "Sameer Malhotra",
    "Tanvi Singhania",
    "Virat Kapoor",
    "Simran Bajaj",
    "Aryan Desai",
    "Pooja Rana",
    "Yash Saxena",
    "Neha Dhawan",
    "Shubham Sharma",
    "Megha Patel",
    "Varun Kumar",
    "Priyanka Singh",
    "Rohit Agarwal",
    "Kavita Mishra",
    "Ravi Verma",
    "Anjali Suri",
    "Deepak Gupta",
    "Shreya Khatri",
    "Sahil Jain",
    "Riya Agnihotri",
    "Karan Chawla",
    "Nandini Bhatia",
    "Pranav Sharma",
    "Aishwarya Iyer",
    "Ritika Verma",
    "Amit Choudhary",
    "Sanjana Pandey",
    "Akshay Kapoor",
    "Mehak Ahuja",
    "Vishal Srivastava",
    "Preeti Sharma",
    "Rajat Tiwari",
    "Shikha Yadav",
    "Vivek Mehra",
    "Sanya Kapoor",
    "Kunal Patel",
    "Sneha Arora",
    "Rahul Bajaj",
    "Anika Chawla",
    "Nitin Malhotra",
    "Sheetal Gupta",
    "Ankur Rana",
    "Payal Joshi",
    "Rohan Sharma",
    "Ishita Agarwal",
    "Saurabh Mehta",
    "Nandini Kapoor",
    "Ravi Pandey",
    "Neha Singhania",
    "Aryan Sharma",
    "Tanisha Verma",
    "Varun Reddy",
    "Kavita Kumar",
    "Rahul Yadav",
    "Shweta Tiwari",
    "Rohit Mehta",
    "Simran Khanna",
    "Aarush Suri",
    "Naina Malhotra",
    "Gaurav Singh",
    "Shreya Rana",
    "Amit Patel",
    "Riya Agarwal",
    "Avinash Gupta",
    "Ankita Sharma",
    "Sandeep Kumar",
    "Prisha Saxena",
    "Kunal Verma",
    "Nikita Joshi",
    "Arun Choudhary",
    "Tanvi Kapoor",
    "Mohan Tiwari",
    "Nandini Verma",
    "Rajesh Kumar",
    "Simran Sharma",
    "Amit Verma",
    "Vidya Singh",
    "Rahul Arora",
    "Akansha Pandey",
    "Harish Patel",
    "Sanya Jain",
    "Sahil Verma",
    "Kriti Kapoor",
    "Vishal Mehta",
    "Deepa Chawla",
    "Neha Yadav",
    "Abhishek Srivastava",
    "Rajni Malhotra",
    "Manish Bajaj",
    "Poonam Tiwari",
    "Shashank Gupta",
    "Aishwarya Reddy",
    "Shiv Verma",
    "Nikita Rana",
    "Rohit Mehra",
    "Anjali Agarwal",
    "Vijay Kapoor",
    "Ritu Jain",
    "Rahul Sharma",
    "Kavita Choudhary",
    "Rohit Yadav",
    "Anu Verma",
    "Ankit Tiwari",
    "Vivek Suri",
    "Preeti Malhotra",
    "Akash Singh",
    "Jyoti Kapoor",
    "Sanjay Verma",
    "Arpita Sharma",
    "Alok Mehta",
    "Anushka Reddy",
    "Rajat Gupta",
    "Nidhi Patel",
    "Aaditya Roy",
    "Khushi Mehta",
    "Avinash Verma",
    "Sneha Sharma",
    "Pranav Agnihotri",
    "Tanushree Reddy",
    "Vikas Kapoor",
    "Pooja Singhania",
    "Gaurav Chawla",
    "Arya Malhotra",
    "Sahil Mehta",
    "Shivani Rana",
    "Rishabh Kapoor",
    "Nisha Verma",
    "Vivek Yadav",
    "Kavita Reddy",
    "Ankur Choudhary",
    "Amita Tiwari",
    "Neha Mehta",
    "Rohit Malhotra",
    "Simran Mehra",
    "Shubham Chawla",
    "Vijay Sharma",
    "Mehak Rana",
    "Aditya Joshi",
    "Arpita Mehra",
    "Vishal Agarwal",
    "Ishita Verma",
    "Rohit Suri",
    "Shreya Kapoor",
    "Aarav Gupta",
    "Nidhi Srivastava",
    "Rajat Mehta",
    "Anjali Choudhary",
    "Alok Yadav",
    "Priyanka Kapoor",
    "Khushi Mehra",
    "Rishabh Choudhary",
    "Deepika Reddy",
    "Aarush Verma",
    "Kriti Rana",
    "Vikram Tiwari",
    "Akash Mehta",
    "Neha Malhotra",
    "Vivek Singh",
    "Aditi Bajaj",
    "Arjun Kapoor",
    "Anika Mehra",
    "Sahil Malhotra",
    "Pooja Arora",
    "Rohan Suri",
    "Ishita Mehra",
    "Ritika Srivastava",
    "Amit Khanna",
    "Mohan Sharma",
    "Shubham Verma",
    "Varun Chawla",
    "Vikas Bajaj",
    "Nikita Choudhary",
    "Ankita Sharma",
    "Ravi Mehta",
    "Aryan Reddy",
    "Swati Agarwal",
    "Akansha Rana",
    "Manish Verma",
    "Naina Mehra",
    "Deepak Srivastava",
    "Sanjana Arora",
    "Alok Tiwari",
    "Shashank Kumar",
    "Rahul Suri",
    "Avinash Kapoor",
    "Simran Arora",
    "Harsh Patel",
    "Kritika Yadav",
    "Aarav Mehta",
    "Mehak Agarwal",
    "Preeti Malhotra",
    "Rohan Choudhary",
    "Ishita Rana",
    "Sanya Mehra",
    "Ananya Srivastava",
]


# Define the list of subject names
subject_names = [
    "mathematics",
    "english",
    "science",
    "history",
    "geography",
    "computer_science",
    "physics",
    "chemistry",
    "biology",
    "economics",
    "music",
    "art",
    "physical_education",
    "foreign_language",
    "social_studies",
    "literature",
    "algebra",
    "geometry",
    "calculus",
    "statistics",
    "philosophy",
    "psychology",
    "sociology",
    "environmental_science",
    "programming",
    "business",
    "marketing",
    "finance",
    "medicine",
    "engineering",
    "architecture","sanskrit"
]

sample_students = []

students = sample_students
class_levels = list([str(c)+s for c in range(1, 13) for s in "ABCDEFGHIJK "[:random.randint(1, 6)*-1]])

for student_id in range(1, 1001):
    name = ' '.join([random.choice(indian_names).split(' ')[0], random.choice(indian_names).split(' ')[-1]])
    date_of_birth = (datetime.now() - timedelta(days=random.randint(4000, 7000))).date()
    contact_info = f"+91 {random.randint(6000000000, 9999999999)}"
    class_level = random.choice(class_levels)

    # Generate random marks for subjects
    subjects = {
        "mathematics": round(random.uniform(25, 100), 2),
        "english": round(random.uniform(25, 100), 2),
        "science": round(random.uniform(25, 100), 2),
        "history": round(random.uniform(25, 100), 2),
        "geography": round(random.uniform(25, 100), 2),
        "computer_science": round(random.uniform(25, 100), 2),
    }

    students.append(
        {
            "name": name,
            "date_of_birth": date_of_birth,
            "phone_number": contact_info,
            "class": class_level,
            "subjects": subjects,
        }
    )

# Generate SQL queries to insert data
insert_student_queries = []
insert_subject_queries = []
insert_marks_queries = []

for subject_name in subject_names:
    insert_subject_queries.append(
        "INSERT INTO Subjects (subject_name) VALUES ('{}')".format(
            subject_name
        )
    )

for student_id, student_data in enumerate(students, start=1):
    name = student_data["name"]
    date_of_birth = student_data["date_of_birth"]
    contact_info = student_data["phone_number"]
    class_level = student_data["class"]
    insert_student_queries.append(
        "INSERT INTO Students (student_id, name, date_of_birth, contact_info, class) VALUES ({}, '{}', '{}', '{}', '{}')".format(
            student_id, name, date_of_birth, contact_info, class_level
        )
    )

    subjects = student_data["subjects"]
    for subject, mark in subjects.items():
        subject_id = subject_names.index(subject) + 1  # Get subject ID from the list
        date_recorded = (datetime.now() - timedelta(days=random.randint(0, 2500))).date()
        insert_marks_queries.append(
            "INSERT INTO Marks (student_id, subject_id, mark, date_recorded) VALUES ({}, {}, {}, '{}')".format(
                student_id, subject_id, mark, date_recorded
            )
        )

sql_queries = []
sql_queries.extend(insert_student_queries)
sql_queries.extend(insert_subject_queries)
sql_queries.extend(insert_marks_queries)

try:
    for query in sql_queries:
        cursor.execute(query)
        
    # Commit the changes
    db.commit()
    print("SQL queries executed successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    db.close()
