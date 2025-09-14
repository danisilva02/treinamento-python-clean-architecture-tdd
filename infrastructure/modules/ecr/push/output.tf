output "ecr_image_version" {
  value = data.aws_ecr_image.latest.image_tag
}