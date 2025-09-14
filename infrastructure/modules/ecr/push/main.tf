locals {
  repo_url = var.ecr_image_uri
}

resource "random_id" "number" {
  keepers = {
    first = "${md5(join("-", [for x in fileset("", "${var.code}/**/*") : filemd5(x)]))}"
  }
  byte_length = 5
}

resource "null_resource" "image" {
  triggers = {
    hash = md5(join("-", [for x in fileset("", "${var.code}/**/*") : filemd5(x)]))
  }

  provisioner "local-exec" {
    command = <<EOF
      aws ecr get-login-password --region us-east-1 ${var.profile != null ? "--profile ${var.profile}" : ""}  | docker login --username AWS --password-stdin ${local.repo_url}

      export ECR_REPO_URL=${local.repo_url}
      export IMAGE_TAG=${random_id.number.hex}

      docker-compose -f ${var.code}/docker-compose.prod.yml build
      docker-compose -f ${var.code}/docker-compose.prod.yml push
    EOF
  }
}

data "aws_ecr_image" "latest" {
  repository_name = var.ecr_image_name
  image_tag       = "${random_id.number.hex}"
  depends_on      = [null_resource.image]
}