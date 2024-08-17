terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

# provision security group
resource "aws_security_group" "my_security_group" {
  
  ingress {# da bta3 l SSH ht7ot l port aly anta 3amlo fl application
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = [ "0.0.0.0/0" ]
  }
  egress{ #De l ports
    from_port = 0
    to_port = 0
    protocol = "-1" #minus one 3l4an t2dr t3ml access l kol l ports
    cidr_blocks = [ "0.0.0.0/0" ]
  }
  tags = {
    Name="My-Security-Group"
  }
}


resource "aws_instance" "deleteme" {
  ami           = "ami-04a81a99f5ec58529" # Ubuntu 24.04 LTS (us-east-1)
  instance_type = "t2.micro"
  key_name = "mykey"
  # sg
 # Reference the security group by its ID
  vpc_security_group_ids = [
    aws_security_group.my_security_group.id,
  ]
  tags = {
    Name = "deleteme"
  }
}


#resource, data, provider, variable, output
