from first_aid import FIRST_AID

def chatbot_response(text):
    text = text.lower()
    for injury in FIRST_AID:
        if injury in text:
            steps = FIRST_AID[injury]
            return "\n".join([f"{i+1}. {s}" for i, s in enumerate(steps)])
    return "Please consult a doctor if symptoms are serious."
