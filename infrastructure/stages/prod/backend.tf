terraform {
  backend "s3" {
    region         = "us-east-1"
    bucket         = "deploy.danieldeveloper.com.br"
    key            = "terraform/danieldeveloper/treinamento-python-clean-architecture-tdd/prod/terraform.state"
  }
}