const cp = require('child_process');
function run(input) {
  // XG-BENCH:JS-TN-002 START
  return cp.execFile('printf', ['%s', input]);
  // XG-BENCH:JS-TN-002 END
}
module.exports = { run };
