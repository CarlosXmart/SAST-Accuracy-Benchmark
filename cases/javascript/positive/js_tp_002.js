const cp = require('child_process');
function run(input) {
  // XG-BENCH:JS-TP-002 START
  cp.exec('echo ' + input);
  // XG-BENCH:JS-TP-002 END
}
module.exports = { run };
