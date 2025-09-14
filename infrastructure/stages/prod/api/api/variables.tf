# APP
variable "environment" {
  type        = string
  description = "Environment"
}

variable "project_name" {
  type        = string
  description = "A project naming resources."
}

variable "company_name" {
  type        = string
  description = "A company naming resources."
}

# AWS
variable "aws_vpc_id" {
  type        = string
  description = "AWS VPC ID Default"
}

variable "aws_subnets_private" {
  type        = list(string)
  description = "Subnets Private CIDR blocks."
}

# Postgres
variable "database_url" {
  type = string
}


# Tag
variable "tags" {
  type = map(string)
}