window.addEventListener('DOMContentLoaded', (event) => {
  console.log('DOMContentLoaded');
  setTimeout(function () {
    let messages = document.getElementById('msg');
    messages.close();
  }, 3000);
});
