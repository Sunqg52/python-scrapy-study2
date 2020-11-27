import re
url = 'ippr_z2C$qAzdH3FAzdH3Fv-ffs_z&e3B17tpwg2_z&e3Bv54AzdH3F7rs5w1fAzdH3Ftpj4AzdH3Fda8l8aAzdH3FamAzdH3Fda8l8aam8d9b8m_ystqs_z&e3Bpi74k_z&e3B9aa_a_z&e3B3r2'
res = ''
c = ['_z2C$q', '_z&e3B', 'AzdH3F']
decode = {
	'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', 
	'2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', 
	'4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 
	'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 
	'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 
	'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.',
	 'AzdH3F':'/',
	}
if(url==None or 'http' in url):
    print(url)
else:
    j= url
    for m in c:
        j=j.replace(m,decode[m])
    for char in j:
        if re.match('^[a-w\d]+$',char):
            char = decode[char]
        res= res+char
    print(res) 