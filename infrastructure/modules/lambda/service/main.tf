resource "random_id" "number" {
  keepers = {
    first = "${timestamp()}"
  }
  byte_length = 10
}

resource "null_resource" "clean" {
  triggers = {
    shell_hash = sha256(random_id.number.hex)
  }

  provisioner "local-exec" {
    command = "rm -rf ${path.module}/build/layer && rm -rf ${path.module}/build/code.zip && rm -rf ${path.module}/build/layer.zip"
  }
}

resource "null_resource" "pip_install" {
  triggers = {
    shell_hash = sha256(random_id.number.hex)
  }

  provisioner "local-exec" {
    command = "python3 -m pip install -r ${var.function_folder}/requirements.txt -t ${path.module}/build/layer/python"
  }

  depends_on = [ null_resource.clean ]
}

data "archive_file" "layer" {
  type        = "zip"
  source_dir  = "${path.module}/build/layer"
  output_path = "${path.module}/build/layer.zip"
  depends_on  = [null_resource.clean, null_resource.pip_install]
}

resource "aws_lambda_layer_version" "layer" {
  layer_name               = "${var.environment}-${var.project_name}-layer"
  filename                 = data.archive_file.layer.output_path
  source_code_hash         = data.archive_file.layer.output_base64sha256
  compatible_runtimes      = ["python3.11", "python3.10", "python3.9"]
  compatible_architectures = var.architectures
  depends_on = [null_resource.clean]
}

data "archive_file" "code" {
  type        = "zip"
  source_dir  = var.function_folder
  output_path = "${path.module}/build/code.zip"
  depends_on = [null_resource.clean]
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${var.function_name}"
  retention_in_days = 7
  tags              = var.tags
}

resource "aws_lambda_function" "lambda" {
  function_name    = var.function_name
  handler          = var.function_handler
  runtime          = var.function_runtime
  timeout          = var.function_timeout
  memory_size      = var.function_memory_size
  filename         = data.archive_file.code.output_path
  source_code_hash = data.archive_file.code.output_base64sha256
  architectures    = var.architectures
  
  role             = aws_iam_role.iam_role.arn
  
  layers           = concat(
    [aws_lambda_layer_version.layer.arn],
    var.layers_external
  )
  
  environment {
    variables = merge(
      var.environment_variables,
      {
        STAGE = var.environment
      }
    )
  }

  depends_on = [aws_cloudwatch_log_group.lambda_log_group]

  # Tags
  tags = var.tags
}