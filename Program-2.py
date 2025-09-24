class FSA:
    def __init__(self):
        self.start_state = 0
        self.accept_state = 2
        self.current_state = self.start_state
    def transition(self, char):
        if self.current_state == 0:  
            if char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0

        elif self.current_state == 1:  
            if char == 'b':
                self.current_state = 2
            elif char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0

        elif self.current_state == 2:  
            if char == 'a':
                self.current_state = 1
            else:
                self.current_state = 0

    def process(self, string):
        self.current_state = self.start_state
        
        for char in string:
            self.transition(char)
        return self.current_state == self.accept_state


fsa = FSA()
test_strings = ["ab", "cab", "aab", "baba", "xyz", "aaabb"]

for s in test_strings:
    if fsa.process(s):
        print(f"{s} => ACCEPTED (ends with 'ab')")
    else:
        print(f"{s} => REJECTED")
