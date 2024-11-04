let comments = [];

// Function to display comments
function displayComments() {
  const commentsList = document.getElementById('comments-list');
  commentsList.innerHTML = '';

  comments.forEach((comment, index) => {
    const commentDiv = document.createElement('div');
    commentDiv.classList.add('comment');
    commentDiv.innerHTML = `<strong>Comment ${index + 1}:</strong><p>${comment}</p>`;
    commentsList.appendChild(commentDiv);
  });
}

// Function to handle form submission and add comments
document.getElementById('comment-form').addEventListener('submit', function (e) {
  e.preventDefault();
  const commentText = document.getElementById('comment-text').value;

  if (commentText.trim() !== '') {
    comments.push(commentText);
    displayComments();
    document.getElementById('comment-text').value = '';
  }
});

// Initial display of comments when the page loads
displayComments();