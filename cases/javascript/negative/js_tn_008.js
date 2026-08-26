function lookup(db, user) {
  // XG-BENCH:JS-TN-008 START
  return db.query('SELECT * FROM users WHERE name=?', [user]);
  // XG-BENCH:JS-TN-008 END
}
module.exports = { lookup };
