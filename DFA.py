alphabet = {'a', 'b'}

def DFA_string_ends_with_a(text):
    final_states = {'q1'} 
    state = q0(text) 
    if state in final_states:
        return "Accepted"
    else:
        return "Rejected"

def q0(text):
    if not text: 
        return 'q0'
    
    if text[0] == 'a':
        return q1(text[1:])  
    elif text[0] == 'b':
        return q0(text[1:]) 
    else:
        return 'q0'  

def q1(text):
    if not text:  
        return 'q1'
    
    if text[0] == 'a':
        return q1(text[1:])  
    elif text[0] == 'b':
        return q0(text[1:])  
    else:
        return 'q0' 

print(DFA_string_ends_with_a("b"))  
