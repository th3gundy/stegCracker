import os
import sys
import time
    
def stegCracker(wlistlocation,stegFile):
	wlist=open(wlistlocation,"r")
    	print "Going to password crack "+stegFile+" with wordlist "+wlistlocation
	tries=0
    	start=time.time()
	try:
	    	for word in wlist:
			word = word.strip()
			print "Trying "+word
			a=os.popen("steghide extract -p '"+word+"' -sf "+stegFile+" 2>&1 | grep 'wrote extracted'")
			tries+=1
  			for i in a.readlines():
    				if i.find('wrote') != -1:
    					print " [+] Found password : "+repr(word)
    					print " [+] Passwords tried : "+str(tries)
	    				print " [+] Time : %.2f seconds" %(time.time()-start)
    					sys.exit(1)
	except KeyboardInterrupt:
		print "\n[-]Keyboard Interruption"
if(len(sys.argv)==3):
	stegCracker(sys.argv[1],sys.argv[2])
else:
	print sys.argv[0]+" wordList imageFile"
	print "Example: "+sys.argv[0]+" pass.list test.jpg"
	
