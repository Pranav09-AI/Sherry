const inputBox = document.querySelector(".search-box input");
const sendButton = document.querySelector(".search-box button");

const API_URL = "http://127.0.0.1:8000/chat";

async function sendMessage() {
    const message = inputBox.value.trim();

    if (message === "") {
        return;
    }

    inputBox.disabled = true;
    sendButton.disabled = true;
    sendButton.textContent = "...";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Failed to connect to backend.");
        }

        const data = await response.json();

        alert("Sherry:\n\n" + data.response);

    } catch (error) {
        alert("Error:\n\n" + error.message);
        console.error(error);
    } finally {
        inputBox.disabled = false;
        sendButton.disabled = false;
        sendButton.textContent = "➜";
        inputBox.value = "";
        inputBox.focus();
    }
}

sendButton.addEventListener("click", sendMessage);

inputBox.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});