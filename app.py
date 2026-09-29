from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

FRONTEND_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "frontend"
)


@app.route("/")
def home():
    return send_from_directory(
        FRONTEND_FOLDER,
        "index.html"
    )


@app.route("/style.css")
def style():
    return send_from_directory(
        FRONTEND_FOLDER,
        "style.css"
    )


@app.route("/script.js")
def script():
    return send_from_directory(
        FRONTEND_FOLDER,
        "script.js"
    )


@app.route("/analyze", methods=["POST"])
def analyze():

    try:
        data = request.get_json()

        income = float(data.get("income", 0))
        food = float(data.get("food", 0))
        travel = float(data.get("travel", 0))
        shopping = float(data.get("shopping", 0))
        bills = float(data.get("bills", 0))

        total_expense = (
            food
            + travel
            + shopping
            + bills
        )

        balance = income - total_expense

        if income > 0:
            saving_percentage = (
                balance / income
            ) * 100
        else:
            saving_percentage = 0

        # Local smart recommendation
        if balance < 0:

            recommendation = (
                "Your expenses are higher than "
                "your income. Reduce unnecessary "
                "spending."
            )

        elif saving_percentage < 10:

            recommendation = (
                "Your savings are low. Try to "
                "reduce shopping and other "
                "non-essential expenses."
            )

        elif saving_percentage < 20:

            recommendation = (
                "Good start. Try to save at "
                "least 20% of your monthly income."
            )

        else:

            recommendation = (
                "Great! Your budget is healthy. "
                "Continue tracking your expenses "
                "and savings."
            )

        products = []

        if balance <= 0:

            products = [
                "Avoid non-essential purchases",
                "Create a monthly spending limit",
                "Review your expenses"
            ]

        elif balance < 5000:

            products = [
                "Choose budget-friendly products",
                "Compare prices before buying",
                "Prioritize essential purchases"
            ]

        else:

            products = [
                "Maintain an emergency fund",
                "Set a monthly savings goal",
                "Plan large purchases carefully"
            ]

        return jsonify({

            "income": income,

            "totalExpense":
                total_expense,

            "balance":
                balance,

            "savingPercentage":
                round(
                    saving_percentage,
                    2
                ),

            "aiRecommendation":
                recommendation,

            "products":
                products
        })

    except Exception as error:

        print("Error:", error)

        return jsonify({
            "error":
                "Unable to analyze budget"
        }), 500


if __name__ == "__main__":

    print(
        "PocketSmart AI running..."
    )

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )