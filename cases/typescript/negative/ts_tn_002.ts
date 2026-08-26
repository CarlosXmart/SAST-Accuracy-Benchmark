interface TextNode { textContent: string | null }
export function render(node: TextNode, input: string): void {
  // XG-BENCH:TS-TN-002 START
  node.textContent = input;
  // XG-BENCH:TS-TN-002 END
}
