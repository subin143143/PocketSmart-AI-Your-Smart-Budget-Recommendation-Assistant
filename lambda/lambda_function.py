import json

from gemini_service import get_ai_recommendation
from database_service import save_budget
from external_api import get_product_recommendations


def lambda_handler(event, context):

    try:

        body = event.get("body", {})

        if isinstance(body, str):
            body = json.loads(body)

        income = float(
            body.get("income", 0)
        )

        food = float(
            body.get("food", 0)
        )

        travel = float(
            body.get("travel", 0)
        )

        shopping = float(
            body.get("shopping", 0)
        )

        bills = float(
            body.get("bills", 0)
        )

        total_expense = (
            food
            + travel
            + shopping
            + bills
        )

        balance = (
            income - total_expense
        )

        if income > 0:

            saving_percentage = (
                balance / income
            ) * 100

        else:
            saving_percentage = 0

        recommendation = (
            get_ai_recommendation(
                income,
                total_expense,
                balance,
                saving_percentage
            )
        )

        products = (
            get_product_recommendations(
                balance
            )
        )

        save_budget(
            income,
            food,
            travel,
            shopping,
            bills,
            total_expense,
            balance,
            saving_percentage
        )

        result = {

            "income":
                income,

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
        }

        return {

            "statusCode": 200,

            "headers": {

                "Content-Type":
                    "application/json",

                "Access-Control-Allow-Origin":
                    "*"
            },

            "body":
                json.dumps(result)
        }

    except Exception as error:

        print(
            "PocketSmart Error:",
            str(error)
        )

        return {

            "statusCode": 500,

            "headers": {

                "Content-Type":
                    "application/json",

                "Access-Control-Allow-Origin":
                    "*"
            },

            "body": json.dumps({
                "error":
                    "Budget analysis failed."
            })
        }