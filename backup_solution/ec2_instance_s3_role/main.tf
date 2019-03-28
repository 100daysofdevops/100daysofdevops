resource "aws_instance" "my-test-instance" {
  ami                     = "${var.test_ami}"
  instance_type           = "${var.instance_type}"
  iam_instance_profile    = "${aws_iam_instance_profile.my-test-profile.name}"
  key_name                = "vpcflowlogs"
  disable_api_termination = false

  tags {
    Name = "my-test-instance"
  }
}

resource "aws_iam_role" "my-test-instance-role" {
  name = "my-testnew-instance-role"

  assume_role_policy = <<EOF
{
"Version": "2012-10-17",
"Statement": [
{
"Action": "sts:AssumeRole",
"Principal": {
 "Service": "ec2.amazonaws.com"
},
"Effect": "Allow"
}
]
}
EOF

  tags = {
    tag-key = "my-test-instance-role"
  }
}

resource "aws_iam_instance_profile" "my-test-profile" {
  name = "my-testnew-profile"
  role = "${aws_iam_role.my-test-instance-role.name}"
}

resource "aws_iam_role_policy" "my-test-policy" {
  name = "my-testnew-policy"
  role = "${aws_iam_role.my-test-instance-role.id}"

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutAccountPublicAccessBlock",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "cloudwatch:*",
                "s3:HeadBucket"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}
EOF
}
