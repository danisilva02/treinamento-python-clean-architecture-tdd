output "host" {
  value = split(":", aws_db_instance.rds.endpoint)[0]
}

output "port" {
  value = aws_db_instance.rds.port
}

output "user_name" {
  value = var.postgres_username
}

output "password" {
  value = aws_db_instance.rds.password
}

output "database" {
  value = var.postgres_database
}
