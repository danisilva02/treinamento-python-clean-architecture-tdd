output "ecr_image_name" {
  value = aws_ecr_repository.ecr.name
}

output "ecr_image_uri" {
  value = aws_ecr_repository.ecr.repository_url
}