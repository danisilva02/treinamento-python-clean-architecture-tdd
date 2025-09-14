# Root
variable "secret_version" {
  type = string
  default = "v1"
}

variable "bucket_name" {
  type = string
}

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

# ACLS
variable "acl" {
  type = string
  default = "private"
}

variable "block_public_acls" {
  type = bool
  default = true
}

variable "block_public_policy" {
  type = bool
  default = true
}

variable "ignore_public_acls" {
  type = bool
  default = true
}

variable "restrict_public_buckets" {
  type = bool
  default = true
}

# Tags
variable "tags" {
  type = map(string)
}