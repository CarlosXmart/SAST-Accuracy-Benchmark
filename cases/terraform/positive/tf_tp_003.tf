resource "aws_ebs_volume" "case" {
  availability_zone = "sa-east-1a"
  size              = 1

  # XG-BENCH:TF-TP-003 START
  encrypted = false
  # XG-BENCH:TF-TP-003 END
}
