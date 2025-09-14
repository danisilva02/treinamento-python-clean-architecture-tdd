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
variable "aws_account_id" {
  type        = string
  description = "AWS Account ID"
}

variable "aws_region" {
  type        = string
  description = "AWS region where resources will be deployed."
}

variable "aws_vpc_id" {
  type        = string
  description = "AWS VPC ID Default"
}

variable "aws_subnets_private" {
  type        = list(string)
  description = "Subnets Private CIDR blocks."
}