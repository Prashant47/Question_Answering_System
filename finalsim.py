#!/usr/bin
import nltk
from nltk.corpus import wordnet as wd

def make_lock(wor , lis):
	for i in range(len(lis)):
		if (wor is lis[i][0]) and (lis[i][1] is 0) :
			lis[i][1] = 1
			return 1
	return 0

def lock_words( total_lis, ip , que_lis ):
	values = 0
	for i in total_lis:
		if i[0] > 0.78:
			make_lock( i[1], ip )
			rvalue = make_lock( i[2] , que_lis )
			if rvalue is 1 and (i[1] not in ['is', 'to','in']):
				print "i[1] ", i[1]
				values = values + i[0]
	return values

def readsynmap(fil):
	f = open(fil,'r')
	lis_syn = []
	lis = f.readlines()
	for i in lis :
		i = i.split('\n')[0].split()
		lis_syn.append(i)
#	print "lis_syn is :\n\n",lis_syn
	return lis_syn
	

def createtag(inpque):
#        print inpque
        tokens  = nltk.word_tokenize(inpque)
#        print tokens
        tagged = nltk.pos_tag(tokens)
        return tagged


def searchin(lis , key , value):
	for i in lis :
		if key in i:
			return i[value]
	print "\n\n value of key is ",key
	return 0

def simm(winip,winq ,iptag , lis_syn , que_tag  , count_ip , count_q ,tech_lis):
	if (winip in tech_lis ) and (winip in winq):
	#	print "\n\n\n   yuppie \n\n"
		return 1.0
	syn_ip = []
	syn_q = []
	syn_all = wd.synsets(winip)
	for p in  syn_all :
		if '.'+ searchin( lis_syn , iptag[ count_ip ] , 0) + '.' in str(p) :
			syn_ip.append(p)

	syn_all = []		
	syn_all = wd.synsets(winq)
	for p in  syn_all :
		if '.'+ searchin( lis_syn , que_tag[ count_q ] , 0) + '.' in str(p) :
			syn_q.append(p)

# here filtering is comleted now find the similarity 

	ls_ws = []
	for  i in syn_ip :
		ls_ss = []
		for j in syn_q:
			res = i.wup_similarity(j)
	#		print i , j , res
			ls_ss.append(res)
		if(ls_ss):
			ls_ws.append(max(ls_ss))
			#print i," ",j," ",ls_ss
	if (ls_ws):
	#	print " ip = ",winip," q = ",winq,"res = ",max(ls_ws)
		return max(ls_ws)

def sen_similarity(ip,que):
#	ip = raw_input('Enter the question :')
	tagged = createtag(ip)
#	print tagged

	#tags for input 

	ip = []
	iptag = []

	lis_syn = readsynmap('synmap')
	for i in tagged :
		ip.append([i[0],0])
		iptag.append(i[1])

#	print "iptag = ", iptag
#	print "ip = " , ip

	#tags from questions 
#	que = raw_input('Enter question from database :  ')
	que_lis = []
	tech_lis = ['gedit','vlc','CD','DVD']
	que_tag = []

	lis = []
	total_lis = []

	tagged = createtag(que)
	for i in tagged :
		que_lis.append([i[0],0])
		que_tag.append(i[1])

	print "que tag = ", que_tag
	print "que lis = " , que_lis
#	print "\n\n\nNow similarity is "
	for i in range(len(ip)):
		for j in range(len(que_lis)):
	#	print "ip ",ip[i],"que ",que_lis[j]
			lis = []
			tmp = simm(ip[i][0], que_lis[j][0] , iptag , lis_syn , que_tag, i,j,tech_lis)
			lis.append(tmp)
			lis.append(ip[i][0])
			lis.append(que_lis[j][0])
			total_lis.append(lis)
	#print total_lis
	total_lis.sort()
	total_lis.reverse()
	print total_lis
	sim_value = lock_words( total_lis , ip , que_lis )
#	print "ip = ", ip
#	print "que_lis = ", que_lis
	print "value of similarity ", sim_value
	return sim_value

#a = raw_input("Enter question from user :")
#b = raw_input("question from database: ")
#sen_similarity(a,b,tech_lis)


