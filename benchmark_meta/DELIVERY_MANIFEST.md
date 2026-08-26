# Delivery manifest

- Benchmark: XGuardian SAST Accuracy Benchmark v1.0
- Scored cases: 164
- Vulnerable: 82
- Benign/hard-negative: 82
- Validation baseline: 96 PASS / 2 SKIP / 0 FAIL
- Evaluator self-test baseline: PASS (5 scenarios)
- Ground truth source: `ground_truth.full.json.gz` (gzip-compressed JSON, semantically identical to the reviewed v1 ground truth)
- Integrity CI: `.github/workflows/benchmark-validation.yml`
- XGuardian SAST pipeline: `.github/workflows/xguardian-sast.yml`

The two baseline SKIPs are compiler/formatter availability for C# and Terraform in the original validation environment. Both tracks received structural/manual review; all available language toolchains passed.
