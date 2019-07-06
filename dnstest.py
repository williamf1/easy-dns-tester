from dns import resolver

#dns user input

website1=input("what website=")
dnsserver=input("dns_server_ip=")


res = resolver.Resolver()

res.nameservers = [dnsserver]



answers = res.query(website1)


#-----------------------------------------------

print("    ")
print("    ")


#dns 1.1.1.1



print("    ")
print("    ")


res = resolver.Resolver()

res.nameservers = ["1.1.1.1"]



answers1 = res.query(website1)






#output

print("your chosen dns says that " +  website1 + "'s" +  " ip address is " +  answers[0].address)

print("    ")
print("    ")

print("1.1.1.1 says that " + website1 + "'s" + " ip is "+ answers1[0].address)
print("     ")
print("     ")


# in two lines

print("1.1.1.1\t\t\tyour dns")
print("     ")
print(answers1[0].address + "\t\t" + answers[0].address)


if answers1[0].address == answers[0].address:
    print("pass")
else:
    print("fail")
