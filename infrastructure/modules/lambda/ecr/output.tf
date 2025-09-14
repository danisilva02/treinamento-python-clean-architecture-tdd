output "lambda_arn" {
  value = aws_lambda_function.lambda.arn
}

output "lambda_name" {
  value = aws_lambda_function.lambda.function_name
}

output "invoke_arn" {
  value = aws_lambda_function.lambda.invoke_arn
}