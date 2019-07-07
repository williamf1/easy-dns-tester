from dns import resolver
#dns user input
dnsserver=input("your chosen dns server ip=")
res = resolver.Resolver()
res.nameservers = [dnsserver]
#dns 1.1.1.1
res2 = resolver.Resolver()
res2.nameservers = ["1.1.1.1"]
a = open("testurls","r")
while True:
    line = a.readline()
    if not line: 
        break
    # the "strip" function removes any spaces/newlines before/after the text
    website=line.strip()
    answeruser = res.query(website)
    answer2 = res2.query(website)    
    #print header
    print("website\t\t\t1.1.1.1\t\t\t\tchosen dns server\t\tresult")
    #same or not print 
    if answer2[0].address == answeruser[0].address:
        result="pass"
    else:
        result="fail"
    #print answers
    print(website + "\t\t"+answer2[0].address+"\t\t\t"+answeruser[0].address+"\t\t\t"+result)






