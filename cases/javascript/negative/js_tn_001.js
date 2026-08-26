function calculate(input) {
  // XG-BENCH:JS-TN-001 START
  const n = Number(input);
  if (!Number.isFinite(n)) throw new Error('invalid number');
  return n * 2;
  // XG-BENCH:JS-TN-001 END
}
module.exports = { calculate };
