variable "service_password" {
  type = string

  # XG-BENCH:TF-TP-006 START
  default = "benchmark-hardcoded-password"
  # XG-BENCH:TF-TP-006 END
}
