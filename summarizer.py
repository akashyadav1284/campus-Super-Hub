def summarize_email(email_text: str):
    sentences = email_text.split(".")
    summary = sentences[0].strip() + "." if sentences[0] else email_text[:60]

    category = detect_category(email_text)

    return {
        "summary": summary,
        "category": category
    }


def detect_category(text: str):
    text = text.lower()

    if any(word in text for word in ["assignment", "exam", "class", "lecture", "submit"]):
        return "Academic"

    if any(word in text for word in ["event", "fest", "workshop", "seminar"]):
        return "Event"

    if any(word in text for word in ["urgent", "immediately", "asap", "important"]):
        return "Urgent"

    return "General"
