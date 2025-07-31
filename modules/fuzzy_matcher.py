from fuzzywuzzy import process

def get_best_matches(query, choices, limit=5):
    return [match[0] for match in process.extract(query, choices, limit=limit) if match[1] > 60]


