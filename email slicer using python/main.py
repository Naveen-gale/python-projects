email = input("enter your email").strip()#removi extra space
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("your user name is ",username)
print("your domain is ", domain)