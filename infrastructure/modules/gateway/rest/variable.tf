variable "apigateway_name" {
  type = string
}

variable "integration_uri" {
  type = string
}

variable "function_name" {
  type = string
}

# Tag
variable "tags" {
  type = map(string)
}