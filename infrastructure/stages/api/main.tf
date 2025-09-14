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
  @Name: API
  @Resource: Multiples Services
  @Description: Resources For API
*/
module "api" {
  source = "./api"

  # Main
  environment  = local.environment
  project_name = local.project_name
  company_name = local.company_name

  # AWS
  aws_vpc_id          = local.aws_vpc_id
  aws_subnets_private = local.aws_subnets_private

  # Postgres
  database_url = "postgresql://neondb_owner:npg_UfP8hvby7AQo@ep-crimson-wildflower-ado4sx55-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

  # Tags
  tags = local.tags
}