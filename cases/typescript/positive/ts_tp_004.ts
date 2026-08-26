interface Runner { exec(command: string): void }
export function run(r: Runner, input: string): void {
  // XG-BENCH:TS-TP-004 START
  r.exec('sh -c "echo ' + input + '"');
  // XG-BENCH:TS-TP-004 END
}
