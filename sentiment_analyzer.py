from typing import List, Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    """
    Wraps VADER sentiment analysis and provides
    - per-message sentiment
    - overall conversation sentiment
    """

    def __init__(self, pos_threshold: float = 0.05, neg_threshold: float = -0.05):
        self._analyzer = SentimentIntensityAnalyzer()
        self.pos_threshold = pos_threshold
        self.neg_threshold = neg_threshold

    def _label_from_score(self, compound: float) -> str:
        if compound >= self.pos_threshold:
            return "Positive"
        if compound <= self.neg_threshold:
            return "Negative"
        return "Neutral"

    def analyze_text(self, text: str) -> Dict[str, float | str]:
        scores = self._analyzer.polarity_scores(text)
        label = self._label_from_score(scores["compound"])
        return {
            "compound": scores["compound"],
            "neg": scores["neg"],
            "neu": scores["neu"],
            "pos": scores["pos"],
            "label": label,
        }

    def analyze_conversation(self, user_messages: List[str]) -> Dict[str, float | str]:
        if not user_messages:
            return {"compound": 0.0, "label": "Neutral", "message": "No user messages were provided."}
        compounds = [self.analyze_text(m)["compound"] for m in user_messages]
        avg_compound = sum(compounds) / len(compounds)
        label = self._label_from_score(avg_compound)

        if label == "Positive":
            explanation = "Overall conversation sentiment: Positive – user is mostly satisfied or in a good mood."
        elif label == "Negative":
            explanation = "Overall conversation sentiment: Negative – user shows signs of frustration or dissatisfaction."
        else:
            explanation = "Overall conversation sentiment: Neutral – user emotions are mixed or balanced."

        return {"compound": avg_compound, "label": label, "message": explanation}
