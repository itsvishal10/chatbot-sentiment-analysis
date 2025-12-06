from dataclasses import dataclass, field
from typing import List, Dict
from sentiment_analyzer import SentimentAnalyzer


@dataclass
class MessageRecord:
    sender: str
    text: str
    sentiment: str | None = None
    compound: float | None = None


@dataclass
class Chatbot:
    sentiment_analyzer: SentimentAnalyzer
    history: List[MessageRecord] = field(default_factory=list)

    def _generate_response(self, user_message: str, sentiment_label: str) -> str:
        msg_lower = user_message.lower()
        if any(word in msg_lower for word in ["hi", "hello", "hey"]):
            return "Hello! 👋 How can I help you today?"
        if "help" in msg_lower:
            return "I'm here to help. Please tell me a bit more about your issue."
        if any(word in msg_lower for word in ["price", "cost", "charge"]):
            return "Pricing details depend on the plan you choose. Could you specify what you're looking for exactly?"
        if any(word in msg_lower for word in ["not working", "issue", "problem", "error", "disappoint"]):
            return "I'm sorry you're facing trouble. Could you describe what went wrong so we can address it?"
        if sentiment_label == "Negative":
            return "I’m sorry you feel this way. Your feedback is important and I want to understand the problem better."
        if sentiment_label == "Positive":
            return "Glad to hear that! Is there anything else I can assist you with?"
        return "Got it. Please tell me more, or type 'quit' when you’re done."

    def process_user_message(self, text: str) -> Dict[str, str]:
        sentiment_result = self.sentiment_analyzer.analyze_text(text)
        self.history.append(
            MessageRecord(sender="user", text=text, sentiment=sentiment_result["label"], compound=sentiment_result["compound"])
        )
        bot_reply = self._generate_response(text, sentiment_result["label"])
        self.history.append(MessageRecord(sender="bot", text=bot_reply))
        return {"user_text": text, "sentiment_label": sentiment_result["label"], "bot_reply": bot_reply}

    def get_user_messages(self) -> List[str]:
        return [m.text for m in self.history if m.sender == "user"]

    def summarize_mood_trend(self) -> str:
        labels = [m.sentiment for m in self.history if m.sender == "user" and m.sentiment]
        if not labels:
            return "No clear mood trend – no user messages with sentiment."
        pos = labels.count("Positive")
        neg = labels.count("Negative")
        neu = labels.count("Neutral")
        if pos > neg and pos >= neu:
            return "Mood trend: Mostly positive across the conversation."
        if neg > pos and neg >= neu:
            return "Mood trend: Mostly negative across the conversation."
        if neu >= pos and neu >= neg:
            return "Mood trend: Mostly neutral or mixed feelings."
        return "Mood trend: Mixed – user sentiment changed several times."
