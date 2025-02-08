document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".approve-ad, .reject-ad").forEach(button => {
        button.addEventListener("click", function () {
            const adId = this.dataset.id;
            const action = this.classList.contains("approve-ad") ? "approve" : "reject";

            fetch(`/moderation/${action}/${adId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.parentElement.remove();
                }
            });
        });
    });
});
