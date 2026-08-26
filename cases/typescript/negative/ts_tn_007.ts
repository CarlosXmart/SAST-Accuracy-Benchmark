interface Msg { origin: string; data: string }
export function onMessage(event: Msg): string | null {
  // XG-BENCH:TS-TN-007 START
  if (event.origin !== 'https://portal.example.test') return null;
  return event.data;
  // XG-BENCH:TS-TN-007 END
}
