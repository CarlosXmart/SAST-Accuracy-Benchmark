resource "aws_iam_policy" "case" {
  name = "xg-benchmark-read-one-bucket"

  # XG-BENCH:TF-TN-005 START
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = ["arn:aws:s3:::example-bucket/*"]
    }]
  })
  # XG-BENCH:TF-TN-005 END
}
