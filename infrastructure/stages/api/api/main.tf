/*
  @Name: Platform
  @Resource: ECR
*/
module "platform_api_ecr" {
  source = "../../../modules/ecr"

  environment  = var.environment
  company_name = var.company_name
  project_name = "${var.environment}-${var.company_name}-${var.project_name}"

  # Tags
  tags = var.tags
}

/*
  @Name: Platform API
  @Resource: ECR Deploy Image
*/
module "platform_api_ecr_build" {
  source = "../../../modules/ecr/push"
  
  profile  = "danieldeveloper"
  ecr_image_uri  = module.platform_api_ecr.ecr_image_uri
  ecr_image_name = module.platform_api_ecr.ecr_image_name
  code           = "${path.module}/../../.."
}

/*
  @Name: Platform API
  @Resource: Lambda
*/
module "platform_api_lambda" {
  source = "../../../modules/lambda/ecr"

  environment  = var.environment
  company_name = var.company_name
  project_name = "${var.project_name}"

  function_name        = "${var.environment}-${var.project_name}"
  function_timeout     = 30
  function_memory_size = 256

  ecr_image_uri     = module.platform_api_ecr.ecr_image_uri
  ecr_image_version = module.platform_api_ecr_build.ecr_image_version

  environment_variables = {
    REGION                = "us-east-1"
    STAGE                 = var.environment
    DATABASE_URL          = var.database_url
  }

  log_retention_in_days = 1

  architectures = ["arm64"]

  tags = var.tags
}

/*
  @Name: Platform API
  @Resource: Gateway
*/
module "platform_api_geteway" {
  source = "../../../modules/gateway/rest"

  apigateway_name = "${var.environment}-${var.company_name}-${var.project_name}-api"
  function_name   = module.platform_api_lambda.lambda_name
  integration_uri = module.platform_api_lambda.invoke_arn

  # Tags
  tags = var.tags
}