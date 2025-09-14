# APP
variable "environment" {
  type = string
}

variable "company_name" {
  type = string
}

variable "project_name" {
  type = string
}

# AWS
variable "aws_vpc_id" {
  type = string
}

variable "aws_subnets_private" {
  type        = list(string)
  description = "Subnets Private CIDR blocks."
}

# Instance
variable "instance_ami" {
  type = string
  default = "ami-096ea6a12ea24a797"
}

variable "instance_type" {
  type = string
  default = "t4g.small"
}

variable "instance_key_name" {
  type = string
  default = "prodStokadoPlatform"
}

# ECRS
variable "ecr_image_uri" {
  type = string
}

variable "env_vars" {
  type = map(string)
  default = {}
}

variable "app_port" {
  type = string
  default = "80:5000"
}

# Tag
variable "tags" {
  type = map(string)
}