function getApiBase() {
    // If opened directly from file system during local dev, talk to localhost.
    if (window.location.protocol === "file:") {
        return "http://127.0.0.1:8000";
    }
    // Otherwise use same origin as the backend on Render / local uvicorn.
    return window.API_BASE_URL || window.location.origin;
}

async function runAISummarizer() {
    const text = document.getElementById("mail-blob").value;
    const output = document.getElementById("summary-output");

    if (!text) {
        output.innerText = "Please paste an email.";
        return;
    }

    output.innerText = "Nexus AI thinking...";

    try {
        const base = getApiBase();
        const response = await fetch(`${base}/api/summarize`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text })
        });

        const data = await response.json();

        let color = "#64748b";
        if (data.category === "Academic") color = "#2563eb";
        if (data.category === "Urgent") color = "#dc2626";
        if (data.category === "Event") color = "#16a34a";

        output.innerHTML =
            "<strong>Summary:</strong> " + data.summary +
            "<br><br><span style='background:" + color +
            "; padding:6px 12px; border-radius:8px;'>"
            + data.category + "</span>";
    } catch (error) {
        output.innerText = "Could not connect to AI server.";
    }
}
