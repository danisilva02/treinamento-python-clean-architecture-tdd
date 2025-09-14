data "aws_caller_identity" "current" {}

module "s3_bucket_datalake" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket        = var.bucket_name
  force_destroy = false

  # Bucket policies
  attach_deny_insecure_transport_policy = true
  attach_require_latest_tls_policy      = true
  attach_elb_log_delivery_policy        = false
  attach_lb_log_delivery_policy         = false

  # S3 bucket-level Public Access Block configuration
  block_public_acls       = var.block_public_acls
  block_public_policy     = var.block_public_policy
  ignore_public_acls      = var.ignore_public_acls
  restrict_public_buckets = var.restrict_public_buckets

  # S3 Bucket Ownership Controls
  control_object_ownership = true
  object_ownership         = "BucketOwnerPreferred"
  expected_bucket_owner    = data.aws_caller_identity.current.account_id
  acl                      = var.acl

  tags                     = var.tags
}

resource "aws_secretsmanager_secret" "s3_secret_connection" {
  description = "S3 ${var.company_name} ${var.project_name} details"
  name        = "${var.environment}/${var.company_name}/${var.project_name}/s3/credentials_${var.secret_version}"
  tags        = var.tags
}

resource "aws_secretsmanager_secret_version" "bucket" {
  secret_id = aws_secretsmanager_secret.s3_secret_connection.id
  secret_string = jsonencode({
    id   = module.s3_bucket_datalake.s3_bucket_id
    arn  = module.s3_bucket_datalake.s3_bucket_arn
    name = module.s3_bucket_datalake.s3_bucket_bucket_domain_name
  })
}