resource "aws_s3_object" "upload_object" {
  for_each      = fileset(var.source_path, "**/*")
  bucket        = var.bucket_name
  key           = each.value
  etag          = filemd5("${var.source_path}/${each.value}")
  source        = "${var.source_path}/${each.value}"
  content_type = ( 
    can(regex(".*\\.html$", each.value)) ? "text/html" :
    can(regex(".*\\.css$", each.value)) ? "text/css" :
    can(regex(".*\\.js$", each.value)) ? "application/javascript" :
    can(regex(".*\\.json$", each.value)) ? "application/json" :
    can(regex(".*\\.png$", each.value)) ? "image/png" :
    can(regex(".*\\.(jpg|jpeg)$", each.value)) ? "image/jpeg" :
    can(regex(".*\\.svg$", each.value)) ? "image/svg+xml" :
    can(regex(".*\\.woff$", each.value)) ? "font/woff" :
    can(regex(".*\\.woff2$", each.value)) ? "font/woff2" :
    can(regex(".*\\.ico$", each.value)) ? "image/x-icon" :
    "application/octet-stream"
  )
}

resource "aws_s3_bucket_policy" "upload_policy" {
  bucket = var.bucket_name
  policy = jsonencode({
    "Version": "2012-10-17",
    "Id": "Policy1234567890123",
    "Statement": [
      {
        "Sid": "Stmt1234567890123",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::${var.bucket_name}/*"
      }
    ]
  })
}
