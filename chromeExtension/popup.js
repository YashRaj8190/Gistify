document.getElementById("summarizeBtn").addEventListener("click", async () => {
    // Get current tab URL
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const videoUrl = tab.url;

    // POST to your Flask backend
    const response = await fetch("http://127.0.0.1:5000/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: videoUrl })
    });

    const data = await response.json();
    document.getElementById("output").value = data.summary || "Failed to summarize";
});
