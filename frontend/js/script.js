const BASE_API_URL = "http://127.0.0.1:5000";

const app = {

    router(viewName, event) {
        if (event) event.preventDefault();

        document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));

        document.getElementById(`view-${viewName}`).classList.add('active');
        document.querySelector(`[data-target="${viewName}"]`).classList.add('active');
    },

    async handlePredict(event) {
        event.preventDefault();

        const submitBtn = document.getElementById("submitBtn");
        const resultBox = document.getElementById("result-container");
        const resultValue = document.getElementById("result-value");
        const resultMsg = document.getElementById("result-message");

        submitBtn.disabled = true;
        submitBtn.innerText = "Processing...";

        const payload = {
            product_category: document.getElementById("product_category").value,
            target_geography: document.getElementById("target_geography").value,
            brand_awareness: document.getElementById("brand_awareness").value,
            age: Number(document.getElementById("age").value),
            price: Number(document.getElementById("price").value),
            budget: Number(document.getElementById("budget").value)
        };

        try {
            const res = await fetch(`${BASE_API_URL}/predict`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await res.json();
            resultValue.innerText = data.recommended_platform;
            resultMsg.innerText = "Prediction successful.";
            resultBox.classList.add("show");

        } catch (err) {
            resultValue.innerText = "Error";
            resultMsg.innerText = "Backend not reachable.";
            resultBox.classList.add("show");
        }

        submitBtn.disabled = false;
        submitBtn.innerText = "Get Recommendation";
    }
};
