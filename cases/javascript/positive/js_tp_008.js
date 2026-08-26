function lookup(db, user) {
  // XG-BENCH:JS-TP-008 START
  return db.query("SELECT * FROM users WHERE name='" + user + "'");
  // XG-BENCH:JS-TP-008 END
}
module.exports = { lookup };
