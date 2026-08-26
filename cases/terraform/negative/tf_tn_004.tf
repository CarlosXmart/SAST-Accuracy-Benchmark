variable "service_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "case" {
  identifier          = "xg-benchmark-db-private"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = "benchmark"
  password            = var.service_password
  skip_final_snapshot = true

  # XG-BENCH:TF-TN-004 START
  publicly_accessible = false
  # XG-BENCH:TF-TN-004 END
}
