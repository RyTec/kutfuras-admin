document.addEventListener("DOMContentLoaded", function () {
    // Oldalsáv kinyitása / becsukása
    let sidebarToggle = document.getElementById("sidebarToggle");
    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", function () {
            document.querySelector(".sidebar").classList.toggle("collapsed");
        });
    }

    // Kártyák frissítése AJAX-al
    async function updateDashboardData() {
        let data = await sendRequest("/api/dashboard_data");
        if (data) {
            document.getElementById("orderCount").innerText = data.orders;
            document.getElementById("quoteCount").innerText = data.quotes;
        }
    }

    updateDashboardData();
});
