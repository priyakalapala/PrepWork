output "instance_id" {
    value = aws_instance.web.id
}

output "instance_private_ip" {
    value = aws_instance.web.private_ip
}

resource "aws_instance" "web" {
    count = 3

    ami = "ami-"
    instance_type = "t3.micro"

    tags = {
        Name = "web-${count.index}"
    }
}

output "instance_id" {
    value = aws_instance.web.id
}