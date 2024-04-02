import difflib


def find_similar_question(question_to_search, questions):

    best_match = None
    best_ratio = 0
    
    for question in questions:
        ratio = difflib.SequenceMatcher(None, question.lower(), question_to_search.lower()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = question
    
    return best_match

