alphabet = {'a','b'}

def DFA_string_ends_with_a(text):
	final_states = {'q1'}
	state = q0
	if state in final_states:
		return "Accepted"
	else:
		return "Rejected"

def q0(text):
	if (text[0] in alphabet):
		if (text == ""):
			return "Accepted"
		elif (text[0] == 'a'):
			p=1
		else :
			return "Rejected"
	