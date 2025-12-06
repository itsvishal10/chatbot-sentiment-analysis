from sentiment_analyzer import SentimentAnalyzer
from chatbot import Chatbot


def run_chat():
    analyzer = SentimentAnalyzer()
    bot = Chatbot(sentiment_analyzer=analyzer)

    print("=" * 60)
    print("   Chatbot with Conversation-Level Sentiment Analysis")
    print("=" * 60)
    print("Type your messages below. Type 'quit' or 'exit' to finish.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting...")
            break

        if user_input.lower() in {"quit", "exit", "bye"}:
            print("\nEnding conversation...")
            break

        if not user_input:
            print("(Empty message ignored. Type something or 'quit' to exit.)")
            continue

        result = bot.process_user_message(user_input)

        print(f"  [Sentiment] {result['sentiment_label']}")
        print(f"Bot: {result['bot_reply']}")
        print("-" * 60)

    user_messages = bot.get_user_messages()
    conversation_result = analyzer.analyze_conversation(user_messages)

    print("\n" + "=" * 60)
    print("FINAL SENTIMENT SUMMARY (Conversation Level)")
    print("=" * 60)
    print(f"Overall conversation sentiment: {conversation_result['label']}")
    print(f"Details: {conversation_result['message']}")
    print(f"Average compound score: {conversation_result['compound']:.3f}")

    print("\n" + bot.summarize_mood_trend())
    print("=" * 60)


if __name__ == "__main__":
    run_chat()
