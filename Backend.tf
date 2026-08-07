terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "env/dev/terraform.tfstate"
    region = "us-east-1"
  }
}


module "ec2_web" {
  source         = "./modules/ec2"
  instance_type  = "t2.micro"
  ami_id         = "ami-0c55b159cbfafe1f0"
  key_name       = "my-keypair"
  subnet_id      = "subnet-0abcd1234"
}

variable "ports" {
    type = list(number)
    default = [22, 80, 443]
}

#To create 3 EC2 instances
resource "aws_instance" "server" {
    count = 3
    ami = "ami_"
    instance_type = "t2.micro"

    tags = {
        Name = "Server-${count.index}"
    }
}

variable "ports" {
    default = [22, 80, 443]
}
resource "aws_security_group_rule" "allow" {
    count = length(var.ports)

    type = "ingress"
    from_port = var.ports[count.index]
    to_port = var.ports[count.index]
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = "sg-12345678"
}

variable "ports" {
    default = [80, 22]
}

dynamic "ingress" {
    for_each = var.ports
}
content {
    from_port = ingress.value
    to_port =   ingress.value
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
}

variable "instance count" {
    type = number
    default = 2
}
resource "aws_instance" web {
    count = var.instance_count
    ami = "ami-"
    intsnce_type = "t2.micro"
}
