import streamlit as st
import ollama

st.title("TOURMATE AI")
st.caption("Your Smart Travel Guide & Itinerary Planner")

question = st.text_area(
    "Describe your trip",
    placeholder="Example: Plan a 3-day trip to Ooty for a family of 4 under ₹15,000"
)


def ask_ai(question):
        response = ollama.chat(
            model="mistral",
            messages=[
                {
                    "role": "system",
                    "content": """
You are TOURMATE AI, an experienced and professional travel guide and itinerary planner.

Rules:
- Be polite and friendly
- Keep responses concise and easy to understand
- Act like an experienced local guide
- Recommend attractions based on user interests
- Suggest local food, shopping, and cultural experiences
- Create day-wise travel plans when requested
- Consider budget, duration, and travel style
- Suggest efficient transportation options
- Mention safety precautions and travel tips
- Warn users about common scams and tourist traps
- Highlight must-visit places and hidden gems
- Focus on practical and realistic recommendations
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]


if st.button("Generate Travel Plan"):
        with st.spinner("Planning your trip..."):
            answer = ask_ai(question)

        st.subheader("Travel Plan")
        st.write(answer)