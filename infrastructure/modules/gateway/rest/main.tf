resource "aws_apigatewayv2_api" "this" {
  name          = var.apigateway_name
  protocol_type = "HTTP"
  cors_configuration {
    allow_origins = ["*"]
    allow_methods= ["*"]
    allow_headers = ["*"]
    max_age = 300
    # allow_credentials = ["*"]
    # expose_headers = ["*"]
  }
  
  # Tag
  tags = var.tags
}

resource "aws_apigatewayv2_stage" "this" {
  api_id      = aws_apigatewayv2_api.this.id
  name        = "$default"
  auto_deploy = true
  
  # Tag
  tags = var.tags
}

resource "aws_apigatewayv2_integration" "api_integration" {
  api_id                 = aws_apigatewayv2_api.this.id
  integration_type       = "AWS_PROXY"
  integration_method     = "POST"  # POST para AWS_PROXY
  payload_format_version = "2.0"   # Garantir que é 2.0
  integration_uri        = var.integration_uri
}

resource "aws_apigatewayv2_route" "options_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "OPTIONS /{proxy+}" # Defina a rota OPTIONS
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_apigatewayv2_route" "post_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "POST /{proxy+}"   # Defina a rota POST
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_apigatewayv2_route" "get_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "GET /{proxy+}"    # Defina a rota GET
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_apigatewayv2_route" "put_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "PUT /{proxy+}"    # Defina a rota PUT
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_apigatewayv2_route" "patch_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "PATCH /{proxy+}"    # Defina a rota PATCH
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_apigatewayv2_route" "delete_route" {
  api_id    = aws_apigatewayv2_api.this.id
  route_key = "DELETE /{proxy+}"    # Defina a rota DELETE
  target    = "integrations/${aws_apigatewayv2_integration.api_integration.id}"
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = var.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.this.execution_arn}/*/*"
}