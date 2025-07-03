const params = new URLSearchParams(window.location.search);
const videoId = params.get("v");
const videoUrl = params.get("url");

const output = document.getElementById("output");
const summarizeBtn = document.getElementById("summarizeBtn");
const downloadBtn = document.getElementById("downloadBtn");
const spinner = document.getElementById("spinner");

chrome.storage.local.get(videoId, async (data) => {
    if (data[videoId]) {
        output.textContent = data[videoId];
        downloadBtn.disabled = false;
    }
});

summarizeBtn.addEventListener("click", async () => {
    output.textContent = "Summarizing...";
    // output.textContent = "";
    spinner.classList.remove("hidden");
    try {
        const res = await fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: videoUrl })
        });

        const data = await res.json();
        const summary = data.summary || "Failed to summarize.";

        output.textContent = summary;
        downloadBtn.disabled = false;

        // Save to chrome storage
        chrome.storage.local.set({ [videoId]: summary });
    } catch (err) {
        output.textContent = "Error occurred while summarizing.";
        console.error(err);
    } finally {
        spinner.classList.add("hidden");
    }
});

downloadBtn.addEventListener("click", () => {
    const blob = new Blob([output.textContent], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${videoId}-summary.txt`;
    a.click();
});
