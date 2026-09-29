import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def get_ai_recommendation(
    income,
    expense,
    balance,
    saving_percentage
):
    prompt = f"""
You are PocketSmart AI, a smart budget assistant.

Monthly Income: ₹{income}
Monthly Expenses: ₹{expense}
Remaining Balance: ₹{balance}
Savings Percentage: {saving_percentage:.2f}%

Give a short and practical budget recommendation.
Explain how the user can manage expenses and improve savings.
Avoid risky financial recommendations.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:
        print("Gemini Error:", error)

        return "AI recommendation is currently unavailable."