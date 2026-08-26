interface Runner { execFile(file: string, args: string[]): void }
export function run(r: Runner, input: string): void {
  // XG-BENCH:TS-TN-004 START
  r.execFile('printf', ['%s', input]);
  // XG-BENCH:TS-TN-004 END
}
