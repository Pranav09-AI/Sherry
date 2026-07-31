const inputBox = document.querySelector(".search-box input");
const sendButton = document.querySelector(".search-box button");
const heroSection = document.querySelector(".container");

const API_URL = "http://127.0.0.1:8000/chat";
const chatContainer = document.getElementById("chat-container");
let isLoading = false;

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (sender === "user") {
        messageDiv.classList.add("user");
    } else {
        messageDiv.classList.add("bot");
    }

    messageDiv.innerHTML = marked.parse(message);;

    chatContainer.appendChild(messageDiv);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    return messageDiv;
}

async function sendMessage() {

    if (isLoading) {
        return;
    }

    isLoading = true;

    const message = inputBox.value.trim();

    if (message === "") {
        return;
    }

    // Show user message immediately
    addMessage(message, "user");

    inputBox.value = "";
    inputBox.focus();

    const thinkingMessage = addMessage("Sherry is thinking...", "bot");
    heroSection.style.display = "none";
    inputBox.disabled = false;
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

        // Show Sherry's response
        thinkingMessage.textContent = data.response;

    } catch (error) {

        addMessage("Error: " + error.message, "bot");
        console.error(error);

    } finally {

        isLoading = false;
        sendButton.disabled = false;
        sendButton.textContent = "➜";
    }
}

sendButton.addEventListener("click", sendMessage);

inputBox.addEventListener("keydown", function (event) {

    if (event.key === "Enter" && !sendButton.disabled) {
        sendMessage();
    }

});