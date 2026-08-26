variable "service_password" {
  # XG-BENCH:TF-TN-006 START
  type      = string
  sensitive = true
  nullable  = false
  # XG-BENCH:TF-TN-006 END
}
