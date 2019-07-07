from dns import resolver


def compareresults(cloudflare,results):

    cloudFlareIPList = []
    resultsIPList = []

    for res in cloudflare:
        cloudFlareIPList.append( res.address)
    
    for res in results:
        resultsIPList.append( res.address)
    
    cloudFlareIPList.sort()
    resultsIPList.sort()
    
    #print(cloudFlareIPList)
    #print(resultsIPList)


    if len(cloudFlareIPList) != len(resultsIPList) :
        return "_____fail1"

    for x in range( len( cloudFlareIPList)) :
        if cloudFlareIPList[x] != resultsIPList[x] :
            return "_____fail2"


    return "pass"




#dns user input
dnsserver=input("your chosen dns server ip=")
res = resolver.Resolver()
res.nameservers = [dnsserver]
#dns 1.1.1.1
res2 = resolver.Resolver()
res2.nameservers = ["1.1.1.1"]
a = open("testurls","r")

print("website\t\t\t\t1.1.1.1           chosen dns server         result")

while True:
    line = a.readline()
    if not line: 
        break
    # the "strip" function removes any spaces/newlines before/after the text
    website=line.strip()
    answeruser = res.query(website)
    answer2 = res2.query(website)    
    #print header
    result = compareresults(answer2,answeruser)
    print('{0:<30} {1:<20} {2:<20} {3:>8}'.format(website, answer2[0].address, answeruser[0].address, result))






