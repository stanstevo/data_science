def get_score() -> dict:
    """
    Returns the students score for every subject
    :return: dict
    """
    subject_scores = {}
    scores = []
    subjects = ["Math", "English", "History", "Geography", "Science", "Art"]
    for subject in subjects:
        score = int(input(f"Enter your score for {subject}: "))
        scores.append(score)
    subject_scores = { key : value 
                for key, value in zip(subjects, scores) }
    return subject_scores
#print(get_score())

def grade_calc() -> dict:
    """
    Calculates the students grade
    :param score: dict
    :return: dict
    """
    score = get_score()
    grades = {}
    for key, value in score.items():
        if value >= 90:
            grades[key] = "A"
        elif value >= 80:
            grades[key] = "B"
        elif value >= 70:
            grades[key] = "C"
        elif value >= 60:
            grades[key] = "D"
        else:
            grades[key] = "F"
    return grades

print(grade_calc())

def get_name():
    return ()