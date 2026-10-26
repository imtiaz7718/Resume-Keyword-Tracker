import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Ensure stop words are ready
stop_words = set(stopwords.words("english"))

def extract_keywords(text: str) -> set:
    """Extracts nouns and key technical phrases using NLTK."""
    tokens = word_tokenize(text.lower())
    
    # POS tagging: identify nouns (NN, NNS, NNP, NNPS)
    pos_tags = nltk.pos_tag(tokens)
    keywords = set()

    for word, tag in pos_tags:
        # Keep alphabetic words that are nouns and not stop words
        if tag.startswith("NN") and word.isalpha() and word not in stop_words and len(word) > 2:
            keywords.add(word)

    # Simple 2-word phrase extraction (bigrams)
    for i in range(len(tokens) - 1):
        w1, w2 = tokens[i], tokens[i + 1]
        if (w1.isalpha() and w2.isalpha() and 
            w1 not in stop_words and w2 not in stop_words and
            len(w1) > 2 and len(w2) > 2):
            keywords.add(f"{w1} {w2}")

    return keywords

def calculate_similarity(resume_text: str, jd_text: str) -> float:
    """Computes TF-IDF Cosine Similarity percentage."""
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

def analyze_match(resume_text: str, jd_text: str):
    resume_kw = extract_keywords(resume_text)
    jd_kw = extract_keywords(jd_text)

    matched = sorted(list(resume_kw.intersection(jd_kw)))
    missing = sorted(list(jd_kw.difference(resume_kw)))

    match_rate = round((len(matched) / len(jd_kw) * 100), 2) if jd_kw else 0.0
    cosine_score = calculate_similarity(resume_text, jd_text)

    return {
        "match_rate": match_rate,
        "cosine_score": cosine_score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "total_jd_keywords": len(jd_kw),
    }