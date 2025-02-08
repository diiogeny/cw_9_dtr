document.addEventListener("DOMContentLoaded", function () {
    const commentForm = document.getElementById("comment-form");
    const commentList = document.getElementById("comments-list");

    if (commentForm) {
        commentForm.addEventListener("submit", function (event) {
            event.preventDefault();
            const formData = new FormData(commentForm);

            fetch(commentForm.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const newComment = document.createElement("li");
                    newComment.innerHTML = `<strong>${data.author}</strong>: ${data.text} <button class="delete-comment" data-id="${data.id}">Удалить</button>`;
                    commentList.prepend(newComment);
                    commentForm.reset();
                }
            });
        });
    }

    if (commentList) {
        commentList.addEventListener("click", function (event) {
            if (event.target.classList.contains("delete-comment")) {
                const commentId = event.target.dataset.id;
                fetch(`/comments/delete/${commentId}/`, {
                    method: "DELETE",
                    headers: {
                        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        event.target.parentElement.remove();
                    }
                });
            }
        });
    }
});
