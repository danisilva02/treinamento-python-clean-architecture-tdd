resource "aws_iam_role" "iam_role" {
  name = "${var.environment}-${var.project_name}-lambda-iam-role"

  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "lambda.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF

  # Política inline para CloudWatch Logs
  inline_policy {
    name   = "lambda-cloudwatch-policy"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Action = [
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents"
          ],
          Effect   = "Allow",
          Resource = "arn:aws:logs:*:*:*"
        }
      ]
    })
  }

  # Política inline para acesso completo ao S3
  inline_policy {
    name   = "lambda-s3-full-access-policy"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Action = "s3:*",
          Effect = "Allow",
          Resource = "*"
        }
      ]
    })
  }

  # Política inline para acesso ao DynamoDB
  inline_policy {
    name   = "lambda-dynamodb-access-policy"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Action = [
            "dynamodb:PutItem",
            "dynamodb:GetItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
            "dynamodb:Scan",
            "dynamodb:Query"
          ],
          Effect   = "Allow",
          Resource = "arn:aws:dynamodb:*:*:table/*"
        }
      ]
    })
  }

  # Tags
  tags = var.tags
}
