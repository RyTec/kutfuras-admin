document.addEventListener("DOMContentLoaded", function () {
    let searchInput = document.getElementById("quoteSearch");

    if (searchInput) {
        searchInput.addEventListener("input", function () {
            let filter = searchInput.value.toLowerCase();
            let rows = document.querySelectorAll(".quotes-table tbody tr");

            rows.forEach(row => {
                let companyName = row.children[1].innerText.toLowerCase();
                let status = row.children[3].innerText.toLowerCase();

                if (companyName.includes(filter) || status.includes(filter)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        });
    }

    // Árajánlat törlése
    document.querySelectorAll(".delete-quote").forEach(button => {
        button.addEventListener("click", async function () {
            let quoteId = this.dataset.id;
            if (confirm("Biztosan törölni szeretnéd ezt az árajánlatot?")) {
                let result = await sendRequest(`/delete_quote/${quoteId}`, "DELETE");

                if (result.success) {
                    showPopup("Árajánlat törölve!");
                    this.closest("tr").remove();
                } else {
                    showPopup("Hiba történt!", "error");
                }
            }
        });
    });
});
