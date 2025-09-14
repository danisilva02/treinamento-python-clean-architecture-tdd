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

# Root
variable "image_tag_mutability" {
  type = string
  default = "MUTABLE"
}

variable "force_delete" {
    type = bool
    default = true
}

variable "scan_on_push" {
    type = bool
    default = true
}

# Tag
variable "tags" {
  type = map(string)
}