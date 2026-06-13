
import streamlit as st
from src.ranking_engine import rank_candidates
from src.report_generator import explain

st.title('Resume Screening Pro')
jd=st.text_area('Job Description')
res=st.text_area('Resumes separated by ---')

if st.button('Analyze'):
    results=rank_candidates(jd,[x.strip() for x in res.split('---') if x.strip()])
    for r in results:
        st.subheader(r['candidate'])
        st.write('Score',r['score'])
        st.write('Skills',r['skills'])
        st.write('Missing',r['missing'])
        st.info(explain(r))
