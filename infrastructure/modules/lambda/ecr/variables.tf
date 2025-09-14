# APP
variable "environment" {
  type = string
}

variable "project_name" {
  type = string
}

variable "company_name" {
  type = string
}

# Lambda
variable "function_name" {
  type = string
}

variable "function_timeout" {
  type = number
  default = 10
}

variable "function_memory_size" {
  type = number
  default = 128
}

variable "environment_variables" {
  type = map(string)
}

variable "layers_external" {
  type = list(string)
  default = []
}

variable "architectures" {
  type = list(string)
  default = ["x86_64"]
}

variable "ecr_image_uri" {
  type = string
}

variable "ecr_image_version" {
  type = string
}

# logs
variable "log_retention_in_days" {
  type = number
  default = 7
}

# Tag
variable "tags" {
  type = map(string)
}