current_courses = ["COMP 163", "MATH 131", "ENG 100", "HIS 106", "GEEN 111", "COMPSCI 121"]
credit_hrs = [3, 3, 3, 4, 1, 1]
course_credits = {
    "COMP 163" : 3,
    "MATH 131" : 4,
    "ENG 100" : 3,
    "HIS 106" : 3,
    "GEEN 111" : 1,
    "COMPSCI 121" : 1
}
# Shows the name of the teacher in each course.
course_professors = {
    "COMP 163" : "Prof. Rhodes",
    "MATH 131" : "Dr. Johnson",
    "ENG 100" : "Dr. Ayisha Jefferson",
    "HIS 106" : "Dr. Johneta Devoe",
    "GEEN 111" : "Dr. Parrish",
    "COMPSCI 121" : "Prof. Rhodes"
}
# Shows the room hall and number of each course.
course_rooms = {
    "COMP 163" : "M-Eric 300",
    "MATH 131" : "Marteena 233",
    "ENG 100" : "Online",
    "GEEN 111" : "Mcnair 204",
    "COMPSCI 121" : "Graham 210",
    "HIS 106" : "Online"
}
study_hrs = {
    "Programming" : 6,
    "Math" : 4,
    "English" : 3,
    "History" : 3
}

total_credits = sum(credit_hrs)
total_study_hrs = study_hrs["Programming"] + study_hrs["Math"] + study_hrs["English"] + study_hrs["History"]
academic_load = total_credits + total_study_hrs

print("=== ACADEMIC DATA COMMIT ===")
print("Current Semester:", total_credits, "credits across", len(current_courses), "courses")
print("Weekly Study Time:", total_study_hrs, "hours")

print("\nCurrent Courses:")
print("COMP 163 -", course_credits["COMP 163"], "credits -", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print("MATH 150 -", course_credits["MATH 150"], "credits -", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print("ENG 101 -", course_credits["ENG 101"], "credits -", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print("HIS 105 -", course_credits["HIS 105"], "credits -", course_professors["HIS 105"], "-", course_rooms["HIS 105"])