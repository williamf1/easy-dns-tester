from dns import resolver
import time

print("""not all websites will work because they
have multiple dns servers to talk to so the program 
will think that it is incorrect because it is talking
to a different dns server every time you run the program
and sometimes it will say it is correct when your dns server
and 1.1.1.1 go to the same google dns server

""")
time.sleep(2)


#dns user input

website1=input("what website=")
print("     ")
print("mind that this is your dns server it will be compaired with 1.1.1.1")
dnsserver=input("your chosen dns server ip=")
 

res = resolver.Resolver()

res.nameservers = [dnsserver]



answers = res.query(website1)


#-----------------------------------------------



#dns 1.1.1.1


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


# output2

print("1.1.1.1\t\t\tyour dns")
print("     ")
print(answers1[0].address + "\t\t" + answers[0].address)





#same or not print
if answers1[0].address == answers[0].address:
    print("dns correct")
else:
    print("dns incorrect")