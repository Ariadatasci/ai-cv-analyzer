def calculate_match(cv_keywords, job_keywords):
    matched = set(cv_keywords) & set(job_keywords)
    missing = set(job_keywords) - set(cv_keywords)

    if len(job_keywords) == 0:
        return 0, matched, missing

    score = len(matched) / len(job_keywords) * 100

    return score, matched, missing