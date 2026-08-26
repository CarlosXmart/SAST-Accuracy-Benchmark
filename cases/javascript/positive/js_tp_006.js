function start() {
  // XG-BENCH:JS-TP-006 START
  window.addEventListener('message', (event) => {
    document.getElementById('out').textContent = String(event.data);
  });
  // XG-BENCH:JS-TP-006 END
}
