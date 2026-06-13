
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def similarity(jd,resumes):
    tfidf=TfidfVectorizer().fit_transform([jd]+resumes)
    return cosine_similarity(tfidf[0:1],tfidf[1:]).flatten()
