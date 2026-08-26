package cases
import "database/sql"
func GoTn008(db *sql.DB, user string) (*sql.Rows,error) {
    // XG-BENCH:GO-TN-008 START
    return db.Query("SELECT * FROM users WHERE name = ?", user)
    // XG-BENCH:GO-TN-008 END
}
