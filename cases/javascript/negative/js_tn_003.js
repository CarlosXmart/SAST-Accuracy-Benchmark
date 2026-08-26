const path = require('path'); const fs = require('fs');
function read(name) {
  // XG-BENCH:JS-TN-003 START
  const base = path.resolve('/srv/data');
  const target = path.resolve(base, name);
  if (target !== base && !target.startsWith(base + path.sep)) throw new Error('outside base');
  return fs.readFileSync(target, 'utf8');
  // XG-BENCH:JS-TN-003 END
}
module.exports = { read };
