
SKILLS=['python','java','sql','machine learning','deep learning','nlp','aws','docker','tensorflow','pytorch','react']
def extract_skills(text):
    t=text.lower()
    return [s for s in SKILLS if s in t]
