import time


def run_task():
    task_name = "emotion_support"

    print(f"[START] task={task_name}", flush=True)

    # normalized emotional progression (0 → 1 range)
    rewards = [0.2, 0.35, 0.5, 0.7, 0.85, 1.0]

    total_reward = 0.0

    for i, reward in enumerate(rewards):
        total_reward += reward

        print(f"[STEP] step={i+1} reward={reward}", flush=True)
        time.sleep(0.05)

    # normalized final score
    final_score = round(total_reward / len(rewards), 2)

    print(
        f"[END] task={task_name} score={final_score} steps={len(rewards)}",
        flush=True
    )


if __name__ == "__main__":
    run_task()