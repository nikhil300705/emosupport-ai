from fastapi import FastAPI, Request

app = FastAPI()

# simple memory (state)
state = {
    "emotion": "neutral",
    "step_count": 0
}

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/reset")
async def reset(request: Request):
    global state
    state = {
        "emotion": "neutral",
        "step_count": 0
    }
    return {"status": "ok"}


@app.post("/step")
async def step(request: Request):
    global state
    data = await request.json()

    user_input = data.get("input", "").lower()
    state["step_count"] += 1

    # 🔥 emotion detection (basic but effective)
    if any(word in user_input for word in ["sad", "depressed", "unhappy"]):
        state["emotion"] = "sad"
        action = "comfort"
        reward = 1.0

    elif any(word in user_input for word in ["angry", "mad", "frustrated"]):
        state["emotion"] = "angry"
        action = "calm"
        reward = 0.8

    elif any(word in user_input for word in ["happy", "good", "great"]):
        state["emotion"] = "happy"
        action = "encourage"
        reward = 0.9

    else:
        state["emotion"] = "neutral"
        action = "listen"
        reward = 0.5

    # 🔥 better observation
    observation = f"User seems {state['emotion']}, agent will {action}"

    done = state["step_count"] >= 5

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": {
            "emotion": state["emotion"],
            "action": action,
            "steps": state["step_count"]
        }
    }


# REQUIRED for OpenEnv
def main():
    return app