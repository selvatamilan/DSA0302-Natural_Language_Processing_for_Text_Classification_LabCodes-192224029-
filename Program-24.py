import re
dialog = [
    "Hello! How are you?",
    "I'm fine, thank you. How about you?",
    "I'm doing well.",
    "Can you help me with my homework?",
    "Sure, what subject is it?",
    "It's mathematics.",
    "Thanks a lot!"
]
def recognize_dialog_act(utterance):
    utterance_lower = utterance.lower()
    if re.search(r'\b(hi|hello|hey|good morning|good evening)\b', utterance_lower):
        return "Greeting"
    elif utterance.endswith("?"):
        return "Question"
    elif re.search(r'\b(can|could|please|would you)\b', utterance_lower):
        return "Request"
    elif re.search(r'\b(thank|thanks|thank you)\b', utterance_lower):
        return "Thanking"
    else:
        return "Statement"
print("Dialog Act Recognition:\n")
for utterance in dialog:
    act = recognize_dialog_act(utterance)
    print(f"Utterance: \"{utterance}\" -> Dialog Act: {act}")
