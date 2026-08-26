interface Msg { origin: string; data: string }
export function onMessage(event: Msg): string {
  // XG-BENCH:TS-TP-007 START
  return event.data;
  // XG-BENCH:TS-TP-007 END
}
