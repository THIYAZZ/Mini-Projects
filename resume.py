# Resume Skill Matcher

def clean_skills(skill_text):
    return set(skill.strip().lower() for skill in skill_text.split(","))

resume_skills = input("Enter your resume skills (comma separated): ")
job_skills = input("Enter job required skills (comma separated): ")

resume_set = clean_skills(resume_skills)
job_set = clean_skills(job_skills)

matched_skills = resume_set.intersection(job_set)
missing_skills = job_set.difference(resume_set)

match_percentage = (len(matched_skills) / len(job_set)) * 100 if job_set else 0

print("\n--- Skill Match Result ---")
print("Matched Skills:", ", ".join(matched_skills) if matched_skills else "None")
print("Missing Skills:", ", ".join(missing_skills) if missing_skills else "None")
print("Match Percentage:", round(match_percentage, 2), "%")
