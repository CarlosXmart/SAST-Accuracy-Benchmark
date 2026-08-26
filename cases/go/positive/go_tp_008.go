package cases
import "database/sql"
func GoTp008(db *sql.DB, user string) (*sql.Rows,error) {
    // XG-BENCH:GO-TP-008 START
    return db.Query("SELECT * FROM users WHERE name='"+user+"'")
    // XG-BENCH:GO-TP-008 END
}
