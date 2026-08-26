resource "aws_security_group" "case" {
  name = "xg-benchmark-open-ssh"

  # XG-BENCH:TF-TP-002 START
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  # XG-BENCH:TF-TP-002 END
}
