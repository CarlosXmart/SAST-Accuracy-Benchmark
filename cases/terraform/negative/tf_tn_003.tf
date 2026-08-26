resource "aws_ebs_volume" "case" {
  availability_zone = "sa-east-1a"
  size              = 1

  # XG-BENCH:TF-TN-003 START
  encrypted = true
  # XG-BENCH:TF-TN-003 END
}
