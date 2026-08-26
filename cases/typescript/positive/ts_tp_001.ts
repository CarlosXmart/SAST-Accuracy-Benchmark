function wrap(v: string): string { return v.trim(); }
export function calculate(input: string): unknown {
  // XG-BENCH:TS-TP-001 START
  const code = wrap(input);
  return eval(code);
  // XG-BENCH:TS-TP-001 END
}
