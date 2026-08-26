resource "aws_s3_bucket" "case" {
  bucket = "xg-benchmark-public-storage"

  # XG-BENCH:TF-TP-001 START
  acl = "public-read"
  # XG-BENCH:TF-TP-001 END
}
