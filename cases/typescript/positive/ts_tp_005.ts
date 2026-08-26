interface Db { query(sql: string, params?: unknown[]): unknown }
export function lookup(db: Db, user: string): unknown {
  // XG-BENCH:TS-TP-005 START
  return db.query("SELECT * FROM users WHERE name='" + user + "'");
  // XG-BENCH:TS-TP-005 END
}
