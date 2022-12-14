#For this project. This script will list out various AWS services.
#We will populate an empty list, add to the list, print the list length, remove services and print a new list.

#Define and print out an empty list
aws_list = []
print("\nThis prints an empty list:")
print(aws_list)

#Use the append command to add multiple elements to a list
print("\nThis adds AWS services to our list:")
aws_list.append("S3")
aws_list.append("Lambda")
aws_list.append("EC2")
aws_list.append("SNS")
aws_list.append("SQS")
aws_list.append("DynamoDB")
print(aws_list)

#Print the length of the list
print("\nThis prints out the length of our list:")
print(len(aws_list))

#Remove two specific services by name and print new list
aws_list.remove("SNS")
aws_list.remove("SQS")
print("\nThis prints out our new list with SNS and SQS removed:")
print(aws_list)

#Print new list with length

print("\nThis prints out the length of our new list:")
print(len(aws_list))