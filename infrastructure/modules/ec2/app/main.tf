resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "ec2_instance_profile"
  role = aws_iam_role.ec2_role.name
}

locals {
  env_vars_string = join(" ", [for key, value in var.env_vars : "-e ${key}=${value}"])
}

resource "aws_instance" "instance" {
  ami           = var.instance_ami
  instance_type = var.instance_type

  key_name = var.instance_key_name

  user_data = "${templatefile("${path.module}/setup.sh.tpl", {
      ecr_image_uri  = "${var.ecr_image_uri}"
      env_vars       = "${local.env_vars_string}"
      app_port       = "${var.app_port}"
    })
  }"

  iam_instance_profile = aws_iam_instance_profile.ec2_instance_profile.name
  
  vpc_security_group_ids = [aws_security_group.sg.id]
  subnet_id = element(var.aws_subnets_private, 0)

  tags = var.tags
}

resource "aws_security_group" "sg" {
  name        = "${var.environment}-${var.company_name}-${var.project_name}-sg"
  description = "Allow HTTP, HTTPS, and SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  vpc_id = var.aws_vpc_id

  # Tags
  tags = var.tags
}
