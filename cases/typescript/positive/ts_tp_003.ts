interface LocationLike { href: string }
export function redirect(loc: LocationLike, next: string): void {
  // XG-BENCH:TS-TP-003 START
  loc.href = next;
  // XG-BENCH:TS-TP-003 END
}
