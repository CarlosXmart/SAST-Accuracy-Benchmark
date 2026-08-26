interface Fs { read(path: string): string }
export function read(fs: Fs, name: string): string {
  // XG-BENCH:TS-TP-006 START
  return fs.read('/srv/data/' + name);
  // XG-BENCH:TS-TP-006 END
}
