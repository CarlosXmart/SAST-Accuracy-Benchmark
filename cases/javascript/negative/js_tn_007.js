const crypto = require('crypto');
function digest(data) {
  // XG-BENCH:JS-TN-007 START
  return crypto.createHash('sha256').update(data).digest('hex');
  // XG-BENCH:JS-TN-007 END
}
module.exports = { digest };
