def boredom(staff):
    department_scores = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    
    score_list = [
        department_scores[department] for department in staff.values()
    ]
    added_values = sum(score_list)
    
    celebration_message = 'party time!!'
    manageable_message = 'i can handle this'
    overwhelmed_message = 'kill me now'
    
    if added_values > 100:
        return celebration_message
    elif added_values < 100 and added_values > 80:
        return manageable_message
    elif added_values <= 80:
        return overwhelmed_message

