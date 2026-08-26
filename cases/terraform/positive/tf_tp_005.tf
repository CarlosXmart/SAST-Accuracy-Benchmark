resource "aws_iam_policy" "case" {
  name = "xg-benchmark-wildcard"

  # XG-BENCH:TF-TP-005 START
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
  # XG-BENCH:TF-TP-005 END
}
