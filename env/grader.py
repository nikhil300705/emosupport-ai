def grade_episode(history, success):
    score = 0.0

    if "empathize" in history:
        score += 0.2

    if "ask_question" in history:
        score += 0.2

    if "give_solution" in history:
        score += 0.3

    if success:
        score += 0.3

    return min(score, 1.0)
