resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${var.function_name}"
  retention_in_days = var.log_retention_in_days

  # Tags
  tags = var.tags
}

resource "null_resource" "wait_for_lambda_update" {
  provisioner "local-exec" {
    command = "echo 'Waiting for 30 seconds...'; sleep 30"
  }

  triggers = {
    lambda_function_name = var.function_name
    ecr_image_version    = var.ecr_image_version
  }
}

resource "aws_lambda_function" "lambda" {
  function_name    = var.function_name
  timeout          = var.function_timeout
  memory_size      = var.function_memory_size
  image_uri        = "${var.ecr_image_uri}:${var.ecr_image_version}"
  package_type     = "Image"
  architectures    = var.architectures
  role = aws_iam_role.iam_role.arn
  
  environment {
    variables = merge(
      var.environment_variables,
      {
        STAGE = var.environment
      }
    )
  }

  depends_on = [
    aws_cloudwatch_log_group.lambda_log_group,
    null_resource.wait_for_lambda_update
  ]

  # Tags
  tags = var.tags
}