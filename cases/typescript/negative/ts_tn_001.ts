export function calculate(input: string): number {
  // XG-BENCH:TS-TN-001 START
  const value = Number(input);
  if (!Number.isFinite(value)) throw new Error('invalid');
  return value * 2;
  // XG-BENCH:TS-TN-001 END
}
