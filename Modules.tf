module "network" {
  source = "./modules/vpc"
  cidr_block  = "10.0.0.0/16"
  subnet_cidr = "10.0.1.0/24"
  vpc_name    = "prod-vpc"
}

variable "instance_type" {
  description = "my-ec2-instance"
  ami = "ami-123456"
  region = "us-east-1"
  default = "t2.micro"
}


variable "cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability zones" {
  description = List of availability zones
  type = list(string)
}

variable "instances" {
  default = {
    web    = "t3.micro"
    app    = "t3.small"
    db     = "t3.medium"
  }
}


resource "aws_instance" "ec2" {
  for_each      = var.instances
  ami           = "ami-0abcd1234"
  instance_type = each.value

  tags = {
    Name = each.key
  }
}

variable "server_count" {
  description = "Number of EC2 instances"
  type = Number
  default = 2
}

resource "aws_instance" "web" {
  count = var.server_count
  ami = "ami -"
  instance_type = "t2.micro"
}