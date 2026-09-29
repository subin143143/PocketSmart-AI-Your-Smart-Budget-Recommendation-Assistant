import boto3
import os
import uuid
from datetime import datetime


REGION = os.getenv(
    "AWS_REGION",
    "ap-south-1"
)

TABLE_NAME = os.getenv(
    "DYNAMODB_TABLE",
    "PocketSmartBudgets"
)


dynamodb = boto3.resource(
    "dynamodb",
    region_name=REGION
)

table = dynamodb.Table(
    TABLE_NAME
)


def save_budget(
    income,
    food,
    travel,
    shopping,
    bills,
    total_expense,
    balance,
    saving_percentage
):

    budget_id = str(
        uuid.uuid4()
    )

    item = {

        "budgetId":
            budget_id,

        "createdAt":
            datetime.utcnow()
            .isoformat(),

        "income":
            str(income),

        "food":
            str(food),

        "travel":
            str(travel),

        "shopping":
            str(shopping),

        "bills":
            str(bills),

        "totalExpense":
            str(total_expense),

        "balance":
            str(balance),

        "savingPercentage":
            str(
                round(
                    saving_percentage,
                    2
                )
            )
    }

    table.put_item(
        Item=item
    )

    return budget_id