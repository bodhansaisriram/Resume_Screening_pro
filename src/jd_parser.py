
from .skill_extractor import extract_skills
def parse_job_description(text):
    return {'skills':extract_skills(text)}
