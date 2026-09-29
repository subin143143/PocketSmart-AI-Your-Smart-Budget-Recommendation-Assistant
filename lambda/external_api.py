def get_product_recommendations(
    balance
):

    if balance <= 0:

        return [
            "Avoid non-essential purchases",
            "Review monthly expenses",
            "Create a spending limit"
        ]

    elif balance < 5000:

        return [
            "Choose budget-friendly products",
            "Compare prices before purchasing",
            "Prioritize essential purchases"
        ]

    elif balance < 15000:

        return [
            "Look for value-for-money products",
            "Keep part of your balance as savings",
            "Compare offers before purchasing"
        ]

    else:

        return [
            "Maintain an emergency fund",
            "Set a monthly savings goal",
            "Plan large purchases carefully"
        ]