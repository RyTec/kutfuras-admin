// Popup üzenet megjelenítése
function showPopup(message, type = "success") {
    let popup = document.createElement("div");
    popup.classList.add("popup", type);
    popup.innerText = message;
    document.body.appendChild(popup);

    setTimeout(() => {
        popup.remove();
    }, 3000);
}

// AJAX kérés küldése
async function sendRequest(url, method = "GET", data = null) {
    let options = {
        method: method,
        headers: { "Content-Type": "application/json" }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        let response = await fetch(url, options);
        let result = await response.json();
        return result;
    } catch (error) {
        console.error("Hiba történt:", error);
        showPopup("Hálózati hiba!", "error");
    }
}
