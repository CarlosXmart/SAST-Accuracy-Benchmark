const crypto = require('crypto');
function digest(data) {
  // XG-BENCH:JS-TP-007 START
  return crypto.createHash('md5').update(data).digest('hex');
  // XG-BENCH:JS-TP-007 END
}
module.exports = { digest };
