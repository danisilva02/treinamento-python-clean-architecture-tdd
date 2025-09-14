locals {
  # App
  project_name = var.project_name
  company_name = var.company_name
  environment  = var.environment

  # AWS
  aws_account_id      = var.aws_account_id
  aws_region          = var.aws_region
  aws_vpc_id          = var.aws_vpc_id
  aws_subnets_private = var.aws_subnets_private

  # Tags
  tags = {
    owner       = var.company_name,
    environment = var.environment,
    purpose     = "Backend",
    project     = var.project_name,
    department  = "Engeenir",
    author      = "Daniel",
    costCenter  = "API-Python-Clean-Architecture-TDD"
  }
}

/*
  @Name: Dynamo TF Lock
  @Resource: Dynamo
  @Description: Centralized Deploy State Lock Platform
*/

/*
  @Name: Platform
  @Resource: ECR
*/
# module "platform_api_ecr" {
#   source = "../../modules/ecr"

#   environment  = var.environment
#   company_name = var.company_name
#   project_name = "platform/api/${var.environment}-${var.company_name}-${var.project_name}"

#   # Tags
#   tags = local.tags
# }

# /*
#   @Name: Platform API
#   @Resource: ECR Deploy Image
# */
# module "platform_api_ecr_build" {
#   source = "../../modules/ecr/push"
  
#   profile  = "danieldeveloper"
#   ecr_image_uri  = module.platform_api_ecr.ecr_image_uri
#   ecr_image_name = module.platform_api_ecr.ecr_image_name
#   code           = "${path.module}/../../.."
# }

# /*
#   @Name: Platform API
#   @Resource: Lambda
# */
# module "platform_api_lambda" {
#   source = "../../modules/lambda/ecr"

#   environment  = var.environment
#   company_name = var.company_name
#   project_name = "${var.project_name}"

#   function_name        = "${var.environment}-${var.project_name}"
#   function_timeout     = 30
#   function_memory_size = 256

#   ecr_image_uri     = module.platform_api_ecr.ecr_image_uri
#   ecr_image_version = module.platform_api_ecr_build.ecr_image_version

#   environment_variables = {
#     REGION            = "us-east-1"
#     STAGE             = var.environment
#     DATABASE_URL      = "postgresql://neondb_owner:npg_UfP8hvby7AQo@ep-crimson-wildflower-ado4sx55-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
#     DATABASE_MIN_CONN = 10
#     DATABASE_MAX_CONN = 20
#   }

#   log_retention_in_days = 7

#   architectures = ["arm64"]

#   tags = local.tags
# }

# /*
#   @Name: Platform API
#   @Resource: Gateway
# */
# module "platform_api_geteway" {
#   source = "../../modules/gateway/rest"

#   apigateway_name = "${var.environment}-${var.company_name}-${var.project_name}"
#   function_name   = module.platform_api_lambda.lambda_name
#   integration_uri = module.platform_api_lambda.invoke_arn

#   # Tags
#   tags = local.tags
# }