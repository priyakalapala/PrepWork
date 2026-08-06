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

