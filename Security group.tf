resource "aws_security_group" "main" {
    name = "webserver-1"
    description = "web server SG for EC2 instance"
}

ingress {
    from_port = 80
    protocol = "TCP"
    to_port = 80
    cidr_block = ["0.0.0.0/0"]
}

ingress {
    from_port = 22
    protocol = "TCP"
    to_port = 80
    cidr_block = ["0.0.0.0/0"]
}

egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
   cidr_block = ["0.0.0.0/0"] 
}

output "PublicIPAddress" {
value = "aws_instance.webserver-1"
description = "AWS EC2 instance Public IP"
}

resource "aws_s3_bucket" {
    bucket = "cloud-aws_bucket"
    tags = {
        Name = "my_bucket"
        Environment = "Dev"
    }
}
versioning _configuration {
    status = "Enabled"
}

