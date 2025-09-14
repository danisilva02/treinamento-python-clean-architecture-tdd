output "arn" {
  value = module.s3_bucket_datalake.s3_bucket_arn
}

output "id" {
  value = module.s3_bucket_datalake.s3_bucket_id
}

output "name" {
  value = var.bucket_name
}