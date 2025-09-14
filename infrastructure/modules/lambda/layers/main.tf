resource "aws_lambda_layer_version" "custom_layer" {
  s3_bucket                = var.s3_bucket
  s3_key                   = var.s3_key
  layer_name               = var.layer_name
  compatible_runtimes      = ["python3.10", "python3.9", "python3.8", "python3.7"]
  compatible_architectures = ["x86_64"]
}