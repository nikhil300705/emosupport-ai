class SupportEnv:
    def __init__(self):
        self.step_count = 0
        self.max_steps = 6
        self.state = None

    def reset(self):
        self.step_count = 0

        self.state = {
            "emotion": "neutral",
            "history": [],
            "confidence": 0.5,
            "difficulty": "easy",
            "resolved": False
        }

        return self.state

    def step(self, action):
        self.step_count += 1
        self.state["history"].append(action)

        reward = 0.0
        done = False

        if action == "empathize":
            reward += 0.3
            self.state["confidence"] += 0.2

        elif action == "ask_question":
            reward += 0.2
            self.state["confidence"] += 0.2

        elif action == "give_solution":
            if self.state["confidence"] >= 0.6:
                reward += 1.0
                self.state["resolved"] = True
                done = True
            else:
                reward += 0.1

        elif action == "escalate":
            reward += 0.5
            done = True

        if self.step_count >= self.max_steps:
            done = True

        return self.state, reward, done, {}