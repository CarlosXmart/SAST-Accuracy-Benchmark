interface LocationLike { href: string }
export function redirect(loc: LocationLike, next: string): void {
  // XG-BENCH:TS-TN-003 START
  loc.href = next.startsWith('/app/') ? next : '/app/home';
  // XG-BENCH:TS-TN-003 END
}
