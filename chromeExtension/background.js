chrome.action.onClicked.addListener((tab) => {
    const videoUrl = tab.url;
    const videoId = new URLSearchParams(new URL(videoUrl).search).get("v");

    if (videoId) {
        chrome.tabs.create({
            url: `summary.html?v=${videoId}&url=${encodeURIComponent(videoUrl)}`
        });
    } else {
        alert("Not a valid YouTube video");
    }
});
