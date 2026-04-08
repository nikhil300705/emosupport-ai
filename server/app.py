from fastapi import FastAPI, Request
import random

app = FastAPI()

# 🔥 ADVANCED STATE
state = {
    "emotion": "neutral",
    "step_count": 0,
    "history": [],
    "last_action": None,
    "emotion_trend": [],
    "engagement_score": 0,
    "improvement_score": 0
}

@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
async def reset(request: Request):
    global state
    state = {
        "emotion": "neutral",
        "step_count": 0,
        "history": [],
        "last_action": None,
        "emotion_trend": [],
        "engagement_score": 0,
        "improvement_score": 0
    }
    return {"status": "ok"}


@app.post("/step")
async def step(request: Request):
    global state
    data = await request.json()

    user_input = data.get("input", "").lower()
    state["step_count"] += 1
    state["history"].append(user_input)

    # 🔥 EMOTION SCORING
    sadness_words = ["sad", "depressed", "lonely", "tired", "cry", "worthless"]
    anger_words = ["angry", "mad", "frustrated", "annoyed", "hate"]
    positive_words = ["happy", "good", "great", "excited", "love", "proud"]

    sadness = sum(word in user_input for word in sadness_words)
    anger = sum(word in user_input for word in anger_words)
    positive = sum(word in user_input for word in positive_words)

    # context influence
    if len(state["history"]) >= 2:
        prev = state["history"][-2]
        if any(w in prev for w in sadness_words):
            sadness += 1
        if any(w in prev for w in anger_words):
            anger += 1

    # determine emotion
    if sadness > anger and sadness > positive:
        emotion = "sad"
    elif anger > sadness:
        emotion = "angry"
    elif positive > 0:
        emotion = "happy"
    else:
        emotion = "neutral"

    state["emotion"] = emotion
    state["emotion_trend"].append(emotion)

    # 🔥 ADAPTIVE STRATEGY
    if emotion == "sad":
        action = "comfort" if state["last_action"] != "comfort" else "encourage"
    elif emotion == "angry":
        action = "calm"
    elif emotion == "happy":
        action = "encourage"
    else:
        action = "listen"

    # 🔥 RESPONSE SYSTEM
    responses = {
        "comfort": [
            "I understand this is really tough. I'm here with you.",
            "You're not alone — things will get better step by step.",
            "It's okay to feel this way. I'm here to listen."
        ],
        "calm": [
            "Take a deep breath. Let's slow things down.",
            "I hear your frustration — let's approach this calmly.",
            "Pause for a moment, you're in control."
        ],
        "encourage": [
            "You're doing better than you think. Keep going!",
            "That's a great sign — you're improving!",
            "I'm proud of your progress!"
        ],
        "listen": [
            "I'm here. Tell me more.",
            "I'm listening — go ahead.",
            "Feel free to share anything."
        ]
    }

    response_text = random.choice(responses[action])

    # 🔥 ENGAGEMENT TRACKING
    if len(user_input) > 20:
        state["engagement_score"] += 1

    # 🔥 PROGRESS DETECTION (THIS IS THE WINNING PART)
    if len(state["emotion_trend"]) >= 2:
        prev_emotion = state["emotion_trend"][-2]

        if prev_emotion == "sad" and emotion in ["neutral", "happy"]:
            state["improvement_score"] += 1

        if prev_emotion == "angry" and emotion == "neutral":
            state["improvement_score"] += 1

    # 🔥 ADVANCED REWARD SYSTEM
    reward = 0.2

    # base alignment
    if emotion == "sad" and action == "comfort":
        reward += 0.5
    if emotion == "angry" and action == "calm":
        reward += 0.4
    if emotion == "happy":
        reward += 0.6

    # engagement bonus
    reward += min(state["engagement_score"] * 0.05, 0.3)

    # 🔥 PROGRESS BONUS (KEY DIFFERENTIATOR)
    reward += state["improvement_score"] * 0.3

    # repetition penalty
    if state["last_action"] == action:
        reward -= 0.1

    state["last_action"] = action

    reward = round(max(0, reward), 2)

    # 🔥 ELITE OBSERVATION
    observation = (
        f"[Step {state['step_count']}] "
        f"Emotion: {emotion} | Action: {action} | "
        f"Improvement: {state['improvement_score']} | "
        f"Response: {response_text}"
    )

    done = state["step_count"] >= 6

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": {
            "emotion": emotion,
            "action": action,
            "engagement": state["engagement_score"],
            "improvement": state["improvement_score"]
        }
    }


# REQUIRED
def main():
    return app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)