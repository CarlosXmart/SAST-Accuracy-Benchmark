const fs = require('fs');
function read(name) {
  // XG-BENCH:JS-TP-003 START
  return fs.readFileSync('/srv/data/' + name, 'utf8');
  // XG-BENCH:JS-TP-003 END
}
module.exports = { read };
