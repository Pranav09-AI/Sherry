const inputBox = document.getElementById("message-input");
const sendButton = document.getElementById("send-btn");
const heroSection = document.querySelector(".container");
const pdfFileInput = document.getElementById("pdf-file");

const API_URL = "http://127.0.0.1:8000/chat";
const UPLOAD_URL = "http://127.0.0.1:8000/upload";

const chatContainer = document.getElementById("chat-container");

let isLoading = false;

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);

    const textDiv = document.createElement("div");
    textDiv.classList.add("message-text");
    textDiv.innerHTML = marked.parse(message);

    messageDiv.appendChild(textDiv);

    if (sender === "bot") {

        const copyButton = document.createElement("button");
        copyButton.classList.add("copy-btn");
        copyButton.textContent = "📋 Copy";

        copyButton.addEventListener("click", async () => {

            try {

                await navigator.clipboard.writeText(
                    textDiv.textContent
                );

                copyButton.textContent = "✓ Copied";

                setTimeout(() => {
                    copyButton.textContent = "📋 Copy";
                }, 2000);

            } catch (err) {

                console.error("Copy failed:", err);

            }

        });

        messageDiv.appendChild(copyButton);
    }

    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;

    return textDiv;
}

async function sendMessage() {

    if (isLoading) {
        return;
    }

    const message = inputBox.value.trim();

    if (message === "") {
        return;
    }

    isLoading = true;

    addMessage(message, "user");

    inputBox.value = "";
    inputBox.focus();

    heroSection.style.display = "none";

    const thinkingMessage = addMessage(
        "Sherry is thinking...",
        "bot"
    );

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
            throw new Error(
                "Failed to connect to backend."
            );
        }

        const data = await response.json();

        thinkingMessage.innerHTML = marked.parse(
            data.response
        );

    } catch (error) {

        console.error(error);

        thinkingMessage.innerHTML =
            "❌ Error: " + error.message;

    } finally {

        isLoading = false;

        sendButton.disabled = false;
        sendButton.textContent = "➜";

    }
}

sendButton.addEventListener(
    "click",
    sendMessage
);

inputBox.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Enter" &&
            !sendButton.disabled
        ) {
            sendMessage();
        }

    }
);

pdfFileInput.addEventListener(
    "change",
    async () => {

        const file = pdfFileInput.files[0];

        if (!file) {
            return;
        }

        heroSection.style.display = "none";

        addMessage(
            `📄 Uploading ${file.name}...`,
            "bot"
        );

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response = await fetch(
                UPLOAD_URL,
                {
                    method: "POST",
                    body: formData
                }
            );

            if (!response.ok) {
                throw new Error(
                    "Upload failed"
                );
            }

            addMessage(
                `✅ ${file.name} uploaded successfully`,
                "bot"
            );

        } catch (error) {

            console.error(error);

            addMessage(
                "❌ PDF upload failed",
                "bot"
            );

        }

    }
);