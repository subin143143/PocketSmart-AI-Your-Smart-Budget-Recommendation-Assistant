const API_URL = "/analyze";

async function analyzeBudget() {

    const income =
        Number(document.getElementById("income").value);

    const food =
        Number(document.getElementById("food").value);

    const travel =
        Number(document.getElementById("travel").value);

    const shopping =
        Number(document.getElementById("shopping").value);

    const bills =
        Number(document.getElementById("bills").value);

    if (income <= 0) {
        alert("Please enter a valid income.");
        return;
    }

    const data = {
        income: income,
        food: food,
        travel: travel,
        shopping: shopping,
        bills: bills
    };

    try {

        const response = await fetch(
            API_URL,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(data)
            }
        );

        if (!response.ok) {
            throw new Error(
                "Server error: " +
                response.status
            );
        }

        const result =
            await response.json();

        document
            .getElementById("result")
            .classList.remove("hidden");

        document.getElementById(
            "resultIncome"
        ).innerText =
            "₹" + result.income;

        document.getElementById(
            "resultExpense"
        ).innerText =
            "₹" + result.totalExpense;

        document.getElementById(
            "resultBalance"
        ).innerText =
            "₹" + result.balance;

        document.getElementById(
            "resultSaving"
        ).innerText =
            result.savingPercentage + "%";

        document.getElementById(
            "aiRecommendation"
        ).innerText =
            result.aiRecommendation;

        const productBox =
            document.getElementById(
                "products"
            );

        productBox.innerHTML = "";

        if (result.products) {

            result.products.forEach(
                function(product) {

                    const p =
                        document.createElement("p");

                    p.innerText =
                        "• " + product;

                    productBox.appendChild(p);
                }
            );
        }

    } catch (error) {

        console.error(error);

        alert(
            "Unable to connect to PocketSmart AI."
        );
    }
}