A modular Python-based chatbot that performs **conversation-level** and **statement-level** sentiment analysis using the VADER sentiment model.

This project is built as part of the **LiaPlus AI assignment**, following all mandatory requirements and implementing Tier-1 and Tier-2 tasks.

---

- Entire conversation history is recorded.
- At the end of the chat, the chatbot computes:
  - Overall sentiment (Positive / Neutral / Negative)
  - Average compound sentiment score
  - Explanation of the emotional direction

- Every user message is analyzed individually.
- Each message is displayed with its sentiment label.
- Chatbot responses adapt slightly to user sentiment.

- Mood Trend Summary → Shows whether the user's mood was overall Positive, Neutral, or Negative.

- Clean and modular code structure
- Separate files for chatbot logic and sentiment engine
- Production-minded design (easy to extend or integrate)

---


| Component       | Technology                           |
| --------------- | ------------------------------------ |
| Language        | Python 3.9+                          |
| Sentiment Model | VADER (via `vaderSentiment` package) |
| Interface       | Command Line (Terminal)              |

---