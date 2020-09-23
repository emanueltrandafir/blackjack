import os


class MenuScreen:

    def __init__(self):
        self.header = "Blackjack Night"
        self.question = "press enter to continue.."
        self.width = 80
        
    def with_header(self, header):
        self.header = header 
        return self
        
    def with_question(self, question):
        self.question = question
        return self
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def build(self):
        print(self.padding_vertical(1))
        print(self.centered_text(self.header))
        print(self.padding_vertical(1)) 
        print(self.horizointal_line())
        print(self.padding_vertical(11)) 
        print(self.question)
        input()
        
    def centered_text(self, text):
        return int((self.width - len(text))/2)*" " + text
    
    def horizointal_line(self):
        return "-"*self.width

    def padding_vertical(self, times):
        return "\n"*times

s = MenuScreen().with_header("test").with_question("press any key").build()
