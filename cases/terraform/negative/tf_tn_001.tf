resource "aws_s3_bucket" "case" {
  bucket = "xg-benchmark-private-storage"
}

resource "aws_s3_bucket_public_access_block" "case" {
  bucket = aws_s3_bucket.case.id

  # XG-BENCH:TF-TN-001 START
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
  # XG-BENCH:TF-TN-001 END
}
