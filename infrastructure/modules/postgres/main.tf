resource "aws_db_subnet_group" "subnet_group" {
  name       = "${var.environment}-${var.company_name}-${var.project_name}"
  subnet_ids = var.aws_subnets_private

  # Tags
  tags = var.tags
}

resource "aws_security_group" "security_group" {
  name   = "${var.environment}-${var.company_name}-${var.project_name}"
  vpc_id = var.aws_vpc_id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Tags
  tags = var.tags
}

resource "random_password" "password" {
  length            = 16 
  special           = false
  override_special  = "!#$%&*()-_=+[]{}<>?"
  upper             = true
  lower             = true
}

resource "aws_db_instance" "rds" {
  identifier             = "${var.environment}-${var.company_name}-${var.project_name}"
  instance_class         = var.instance_class
  allocated_storage      = var.allocated_storage
  engine                 = var.engine
  engine_version         = var.engine_version
  
  # Access control
  username               = var.postgres_username
  password               = random_password.password.result
  db_name                = var.postgres_database

  # VPC
  vpc_security_group_ids = [aws_security_group.security_group.id]
  db_subnet_group_name   = aws_db_subnet_group.subnet_group.name

  publicly_accessible    = true
  skip_final_snapshot    = true

  # Tags
  tags                   = var.tags
}

resource "aws_secretsmanager_secret" "postgres_secret_connection" {
  description = "Postgres superset connect details"
  name        = "${var.environment}/${var.company_name}/${var.project_name}/postgres/credentials_${var.secret_version}"
  
  # Tags
  tags = var.tags
}

resource "aws_secretsmanager_secret_version" "postgres_connection" {
  secret_id = aws_secretsmanager_secret.postgres_secret_connection.id
  secret_string = jsonencode({
    id                  = aws_db_instance.rds.id
    username            = aws_db_instance.rds.username
    password            = aws_db_instance.rds.password
    database            = aws_db_instance.rds.db_name
    engine              = aws_db_instance.rds.engine
    host                = split(":", aws_db_instance.rds.endpoint)[0]
    port                = aws_db_instance.rds.port
  })
}