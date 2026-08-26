function start() {
  // XG-BENCH:JS-TN-006 START
  window.addEventListener('message', (event) => {
    if (event.origin !== 'https://portal.example.test') return;
    document.getElementById('out').textContent = String(event.data);
  });
  // XG-BENCH:JS-TN-006 END
}
