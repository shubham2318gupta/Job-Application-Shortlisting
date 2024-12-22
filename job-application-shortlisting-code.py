applications = [
    {"name": "Shubham ", "skills": ["Python", "SQL", "Machine Learning"], "experience": 3},
    {"name": "Amit ", "skills": ["Java", "SQL", "React"], "experience": 5},
    {"name": "Sohel ", "skills": ["Python", "Data Analysis"], "experience": 2},
    {"name": "Somesh", "skills": ["Python", "Machine Learning", "Data Science"], "experience": 4},
]

required_skills = {"Python", "Machine Learning"}
minimum_experience = 3

def filter_applications(applications, required_skills, minimum_experience):
    shortlisted = []
    for application in applications:
        if (required_skills.issubset(application["skills"]) and
                application["experience"] >= minimum_experience):
            shortlisted.append(application)
    return shortlisted

shortlisted_candidates = filter_applications(applications, required_skills, minimum_experience)

print("Shortlisted Candidates:")
for candidate in shortlisted_candidates:
    print(f"Name: {candidate['name']}, Experience: {candidate['experience']} years")
