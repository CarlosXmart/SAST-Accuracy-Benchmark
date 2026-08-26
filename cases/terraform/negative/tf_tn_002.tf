resource "aws_security_group" "case" {
  name = "xg-benchmark-private-ssh"

  # XG-BENCH:TF-TN-002 START
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/24"]
  }
  # XG-BENCH:TF-TN-002 END
}
