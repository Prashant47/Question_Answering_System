#!/usr/bin/python

""" What does this program do?
	input --> what is vim
	oputput --> you get three list
			1] tech_flag = which tech word it has
			2] wh_flag = which wh question does it have
			3] ques = get all questions that of technical word

			4] set the weightage on basis of wh questions (to be done)

"""

def test(in_que):
#	input = raw_input("Enter the sentence: ")
	input = in_que
	input = input.lower()
	input = input.replace('?','') # this is to remove ? from sentence need to add forther
	sen = input.split(' ')
#	print sen

	tech = ['vim','gedit','vlc']
	wh = ['what','how','where','when']
	tech_flag = []
	wh_flag = []
	for i in sen:
		for j in  tech:
			if i == j:
				tech_flag.append(i)
#	print tech_flag
	for i in sen:
		for j in wh:
			if i == j:
				wh_flag.append(i)			
#	print wh_flag


	def vim():
		fd = open("vim_questions")
		questions = fd.readlines()
		return questions
	def gedit():
		fd = open("gedit_questions")
		questions = fd.readlines()
		return questions

	def vlc():
		fd =open("vlc_questions")
		questions = fd.readlines()
		return questions

	def default():  # need to write a logic here for default case
		print "default value"
	mycase = {
	'vim': vim,
	'gedit':gedit,
	'vlc':vlc,
	'':default
	}
	try:
		myfunc = mycase[tech_flag[0]] # considering only one tech word in question. For two we need implement
	except IndexError:
	   myfunc = default

	ques = myfunc()
	print tech_flag[0]
	return ques,wh_flag,tech_flag
