export function render(node: { innerHTML: string }, input: string): void {
  // XG-BENCH:TS-TP-002 START
  node.innerHTML = input;
  // XG-BENCH:TS-TP-002 END
}
