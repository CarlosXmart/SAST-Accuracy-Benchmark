function go(next) {
  // XG-BENCH:JS-TN-005 START
  const target = typeof next === 'string' && next.startsWith('/app/') ? next : '/app/home';
  window.location.href = target;
  // XG-BENCH:JS-TN-005 END
}
