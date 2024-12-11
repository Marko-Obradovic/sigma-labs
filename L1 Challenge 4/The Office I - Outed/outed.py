def outed(meet: dict, boss: str):
    added_happiness_scores = sum(meet.values())
    boss_score = meet[boss]
    number_of_people = len(meet)

    happiness_value = (added_happiness_scores + boss_score) / number_of_people

    accepted_threshold = 5

    bad_outcome_message = 'Get Out Now!'
    good_outcome_message = 'Nice Work Champ!'

    return bad_outcome_message if happiness_value <= accepted_threshold else good_outcome_message
