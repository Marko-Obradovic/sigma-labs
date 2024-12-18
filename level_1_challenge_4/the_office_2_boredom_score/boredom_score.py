"""Calculate the boredom score for a team based on their departments and return the sentiment.
"""

def calculate_boredom_score(staff: dict[str, str]) -> int:
    department_scores = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25
    }

    score_list = [
        department_scores[department] for department in staff.values()
        ]

    added_values: int = sum(score_list)
    return added_values

CELEBRATION_MESSAGE = "party time!!"
MANAGEABLE_MESSAGE = "i can handle this"
OVERWHELMED_MESSAGE = "kill me now"

def main(added_values: int) -> str:
    if added_values <= 80:
        return OVERWHELMED_MESSAGE
    if added_values < 100:
        return MANAGEABLE_MESSAGE
    else:
        return CELEBRATION_MESSAGE
