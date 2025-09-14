variable "aws_vpc_id" {
  type = string
}

variable "aws_subnets_private" {
  type        = list(string)
  description = "Subnets Private CIDR blocks."
}

variable "environment" {
  type = string
}

variable "company_name" {
  type = string
}

variable "project_name" {
  type = string
}

variable "secret_version" {
  type = string
  default = "v1"
}

# Postgres
variable "instance_class" {
  type = string
  default = "db.t4g.small"
}

variable "allocated_storage" {
  type = number
  default = 20
}

variable "engine" {
  type = string
  default = "postgres"
}

variable "engine_version" {
  type = string
  default = "14"
}

variable "postgres_database" {
  type = string
  default = "stokado"
}

variable "postgres_username" {
  type = string
  default = "stokado"
}

# Tags
variable "tags" {
  type = map(string)
}