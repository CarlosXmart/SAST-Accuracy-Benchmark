def ruby_tn_006(db, user)
  # XG-BENCH:RUBY-TN-006 START
  db.execute('SELECT * FROM users WHERE name = ?', user)
  # XG-BENCH:RUBY-TN-006 END
end
