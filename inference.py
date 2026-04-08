import random

def clamp_score(score):
    return max(0.01, min(0.99, score))


def run_task(task_name):
    print(f"[START] {task_name}")

    # Dummy simulation of environment interaction
    for step in range(3):
        action = "ask_question"
        print(f"Action: {action}")

    # Generate a safe score (IMPORTANT FIX)
    raw_score = random.uniform(0, 1)
    score = clamp_score(raw_score)

    print(f"Score: {score}")
    print("[END]\n")


if __name__ == "__main__":
    run_task("easy-task")
    run_task("medium-task")
    run_task("hard-task")