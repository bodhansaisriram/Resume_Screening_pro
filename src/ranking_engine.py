
from .similarity_engine import similarity
from .skill_extractor import extract_skills
from .skill_gap import skill_gap

def rank_candidates(jd,resumes):
    sims=similarity(jd,resumes)
    req=extract_skills(jd)
    out=[]
    for i,r in enumerate(resumes):
        skills=extract_skills(r)
        out.append({
            'candidate':f'Candidate_{i+1}',
            'score':round(float(sims[i])*100,2),
            'skills':skills,
            'missing':skill_gap(req,skills)
        })
    return sorted(out,key=lambda x:x['score'],reverse=True)
