# Data Engineering

[![Terraform](https://img.shields.io/badge/Terraform-7B42BC?logo=terraform&logoColor=white)](https://www.terraform.io)

## Install Terraform

```bash
$ brew install terraform
```

## Deploy Datalake

Para fazer deploy deste projeto acesse a pasta `stages` e o ambiente que deseja deployar: `staging` ou `prod`. Após isso execute os seguintes comandos:

```bash
$ terraform init -var-file=variables.tfvars
$ terraform fmt
$ terraform plan -var-file=variables.tfvars
$ terraform apply -var-file=variables.tfvars
```