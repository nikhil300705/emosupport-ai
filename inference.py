class SupportEnv:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return {
            "observation": "start",
            "info": {}
        }

    def step(self, action):
        self.step_count += 1

        return {
            "observation": "ok",
            "reward": 0.5,
            "done": self.step_count >= 3,
            "info": {}
        }