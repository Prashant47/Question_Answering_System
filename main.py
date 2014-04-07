#!/usr/bin/python
import switch_case
import finalsim as fs
def get_answer(input_que):
	input_que= input_que.lower()
	wh = []
	ques = []
	q_no = []
	tech_flg = []
	ques,wh,tech_flg = switch_case.test(input_que)
	print ques
	if tech_flg == []:
		ans = "Please enter relevent question."
		return ans		
#	print wh
#print ques,wh
	i = 0
	ques_ip = []
	for i in range(len(ques)):
#		print ques[i]
		ques_ip = ques[i].split('\t')
		p = fs.sen_similarity(input_que, ques_ip[0]) 
		print p
		q_no.append(p)
	print q_no
	j = 0.0
	k = 0
	l = 0
	for k in range(len(q_no)):
		if(j < q_no[k]):
			j = q_no[k]
			l = k
			print l
		k = k + 1
	print "value ", ques[l].split()
	if float(q_no[l]) <= 1:
		ques_1 = ques[l].split('\t')
		print ques_1
		ques_1[0] = ques_1[0].lower()
		qq = ques_1[0].split()		
		print "qq: ", qq , "i/p :", len(input_que.split())
		tmp = [['what','is','gedit'], ['what','is','vim'], ['what','is','vlc']]
		if ( qq in tmp ) and (len(input_que.split()) is 3):
			print "Condition satisfied"
		else:
			ans = "Sorry we do not know answer of this question "
			return ans
	que = []
# fetching answer
	que = ques[l].split('\t')
	spec_ans = []
	print tech_flg[0]
	if tech_flg[0] == 'vim':
		fd = open("vim_answers")
		a = "vim_answers"
	elif tech_flg[0] == 'gedit':
		fd = open("gedit_answers")
		a = "gedit_answers"
	elif tech_flg[0] == 'vlc':
		fd = open("vlc_answers")
		a = "vlc_answers"		
	answers = fd.readlines()
	spec_ans = answers[int(que[1]) - 1]
	spec_ans = spec_ans.replace('\n','')
	spec_ans = spec_ans.split('\t')
	print spec_ans
	print int(spec_ans[1])
	print int(spec_ans[2])
	import get_ans
	ans = []
	ans = get_ans.print_ans(a, int(spec_ans[1]), int(spec_ans[2]))
	print ans
	ans = ' '.join(ans)	
	return ans	
#a = raw_input("Enter the que:")
#get_answer(a)	
""" taking one by one question form ques[] passing to simlilarity [by gondya]  """
