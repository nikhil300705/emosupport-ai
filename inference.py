import time
import random


def run_task():
    task_name = "emotion_support"

    print(f"[START] task={task_name}", flush=True)

    # Simulated emotional states improving
    emotional_states = [
        "sad",
        "anxious",
        "neutral",
        "hopeful",
        "confident"
    ]

    base_reward = 0.2
    total_reward = 0.0
    steps = len(emotional_states)

    for i in range(steps):
        # simulate improvement
        improvement_factor = (i + 1) * 0.6
        reward = round(base_reward + improvement_factor + random.uniform(0.05, 0.15), 2)

        total_reward += reward

        print(f"[STEP] step={i+1} reward={reward}", flush=True)
        time.sleep(0.1)

    # bonus for consistency
    consistency_bonus = 0.5
    final_score = round(total_reward + consistency_bonus, 2)

    print(f"[END] task={task_name} score={final_score} steps={steps}", flush=True)


if __name__ == "__main__":
    run_task()