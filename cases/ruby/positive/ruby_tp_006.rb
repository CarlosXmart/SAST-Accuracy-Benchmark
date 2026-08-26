def ruby_tp_006(db, user)
  # XG-BENCH:RUBY-TP-006 START
  db.execute("SELECT * FROM users WHERE name='#{user}'")
  # XG-BENCH:RUBY-TP-006 END
end
