"""Calculate happiness value from a dictionary of names assigned to happiness values and 
determine if the happiness value meets the accepted threshold.
"""

def calculate_happiness_value(meet: dict[str, int], boss: str) -> float :
    total_happiness: int = sum(meet.values())
    boss_score: int = meet.get(boss, 0)
    number_of_people = len(meet)

    happiness_value: float = (total_happiness + boss_score) / number_of_people
    return happiness_value

ACCEPTED_THRESHOLD = 5

BAD_OUTCOME_MESSAGE = 'Get Out Now!'
GOOD_OUTCOME_MESSAGE = 'Nice Work Champ!'

def main(happiness_value) -> str:
    return BAD_OUTCOME_MESSAGE if happiness_value <= ACCEPTED_THRESHOLD else GOOD_OUTCOME_MESSAGE
