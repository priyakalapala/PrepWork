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


