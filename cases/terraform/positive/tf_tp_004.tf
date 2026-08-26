resource "aws_db_instance" "case" {
  identifier          = "xg-benchmark-db"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = "benchmark"
  password            = "benchmark-only-not-a-secret"
  skip_final_snapshot = true

  # XG-BENCH:TF-TP-004 START
  publicly_accessible = true
  # XG-BENCH:TF-TP-004 END
}
