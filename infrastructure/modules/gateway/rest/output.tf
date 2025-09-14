output "api_id" {
  value = aws_apigatewayv2_api.this.id
}

output "stage" {
  value = aws_apigatewayv2_stage.this.id
}