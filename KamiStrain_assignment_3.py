# Personal Information Storage
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
student_hometown = "Charlotte, NC"
grad_semester = "Spring 2028"
student_major = "Computer Science"

# Academic Data Organization (Lists)
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish 2", "World History"]
credit_hrs = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

# Contact Information Storage (Tuples)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
insta_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
student_birthday = ("Birthday", "5", "22", "2006")

# Interest Tracking (Sets)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
student_hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational Mapping (Dictionaries)
# Shows how many credits the student gets in each course.
course_credits = {
    "COMP 163" : 3,
    "MATH 150" : 3,
    "ENG 101" : 3,
    "HIS 105" : 3
}
# Shows the name of the teacher in each course.
course_professors = {
    "COMP 163" : "Prof. Rhodes",
    "MATH 150" : "Dr. Lee",
    "ENG 101" : "Dr. Martinez",
    "HIS 105" : "Dr. Brown"
}
# Shows the room hall and number of each course.
course_rooms = {
    "COMP 163" : "M-Eric 300",
    "MATH 150" : "Marteena 201",
    "ENG 101" : "Crosby 121",
    "HIS 105" : "Crosby 210"
}
# Shows the student's monthly budget for food, entertainment, books, and transportation.
monthly_budget = {
    "Food" : 450,
    "Entertainment" : 200,
    "Books" : 125,
    "Transportation" : 100
}
# Shows how many hours the student studies in each course.
study_hrs = {
    "Programming" : 10,
    "Math" : 8,
    "English" : 4,
    "History" : 3
}
# Shows the students key contacts and their phone numbers.
contact_directory = {
    "Mom" : "704-555-0199",
    "Roommate" : "336-555-7821",
    "Academic Advisor" : "336-334-5000"
}

# Calculations
total_credits = sum(credit_hrs)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_study_hrs = study_hrs["Programming"] + study_hrs["Math"] + study_hrs["English"] + study_hrs["History"]
academic_load = total_credits + total_study_hrs
total_monthly_budget = monthly_budget["Food"] + monthly_budget["Entertainment"] + monthly_budget["Books"] + monthly_budget["Transportation"]
daily_food_budget = monthly_budget["Food"] / 30
annual_budget = total_monthly_budget * 12
study_cost_per_hr = monthly_budget["Books"] / total_study_hrs

# Analytics Calculations
total_media_followers = insta_info[2] + twitter_info[2]
skills_comparison = len(current_skills) / len(skills_to_learn)
entertainment_backlog_count = len(entertainment_backlog)

# Prints out the student's information as a personal portfolio
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "| Email:", student_email)
print("From:", student_hometown, "| Graduating:", grad_semester)
print("Major:", student_major)

print("\n=== ACADEMIC PROFILE ===")
print("Current Semester:", total_credits, "credits across", len(current_courses), "courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print("Weekly Study Time:", total_study_hrs, "hours")
print(f"Academic Investment: ${study_cost_per_hr} per study hour")

print("\nCurrent Courses:")
print("COMP 163 -", course_credits["COMP 163"], "credits -", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print("MATH 150 -", course_credits["MATH 150"], "credits -", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print("ENG 101 -", course_credits["ENG 101"], "credits -", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print("HIS 105 -", course_credits["HIS 105"], "credits -", course_professors["HIS 105"], "-", course_rooms["HIS 105"])

print("\n=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", current_skills)
print("Learning Goals:", skills_to_learn)
print("Career Interests:", career_interests)
print("Skills Currently Have:", len(current_skills))
print("Skills Want to Learn:", len(skills_to_learn))

print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")

print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")

print("\n=== LIFE STATISTICS ===")
print("Total Courses Completed:", completed_courses_count)
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(student_hobbies)} activities")
print("================================================================")