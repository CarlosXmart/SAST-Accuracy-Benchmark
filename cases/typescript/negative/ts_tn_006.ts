interface Fs { read(path: string): string }
export function read(fs: Fs, name: string): string {
  // XG-BENCH:TS-TN-006 START
  if (!/^[a-zA-Z0-9._-]+$/.test(name)) throw new Error('invalid name');
  return fs.read('/srv/data/' + name);
  // XG-BENCH:TS-TN-006 END
}
