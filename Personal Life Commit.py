full_name = "Kamryn Strain"
student_email = "krstrain1@aggies.ncat.edu"
student_hometown = "Charlotte, NC"
grad_semester = "Spring 2029"
student_major = "Computer Science"

# Contact Information Storage (Tuples)
emergency_contact = ("Mom", "Tisha F", "980-345-6789")
home_address = ("10330 Atkins Ridge Dr", "Charlotte, NC", "28213")
insta_info = ("Instagram", "itsskamiiraee", 1822)
twitter_info = ("Tiktok", "@itsskamiireallshii", 23198)
student_birthday = ("Birthday", "3", "21", "2007")

contact_directory = {
    "Mom" : "980-345-6789",
    "Roommate" : "704-990-0321",
    "Academic Advisor" : "336-285-4213"
}

total_media_followers = insta_info[2] + twitter_info[2]

print("================================================================")
print("              PERSONAL & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "| Email:", student_email)
print("From:", student_hometown, "| Graduating:", grad_semester)
print("Major:", student_major)

print("\n=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_media_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")