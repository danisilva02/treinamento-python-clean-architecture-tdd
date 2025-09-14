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
variable "function_folder" {
  type = string
}

variable "function_name" {
  type = string
}

variable "function_runtime" {
  type = string
  default = "python3.9"
}

variable "function_timeout" {
  type = number
  default = 10
}

variable "function_memory_size" {
  type = number
  default = 128
}

variable "function_handler" {
  type = string
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

# Tag
variable "tags" {
  type = map(string)
}