import os


class ScreenBuilder:

    def __init__(self):
        self.centered_question = False
        self.header = "Blackjack Night"
        self.question = "press enter to continue.."
        self.width = 80

    def width_width(self, width):
        self.width = width
        return self

    def with_centered_question(self):
        self.centered_question = True
        return self

    def with_header(self, header):
        self.header = header 
        return self
        
    def with_question(self, question):
        self.question = question
        return self
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def build_and_get_input(self):
        self.clear()
        # print(self.padding_vertical(1))
        print(self.centered_text(self.header))
        # print(self.padding_vertical(1))
        print(self.horizointal_line())
        print(self.padding_vertical(1))
        question = self.centered_text(self.question) if self.centered_question else self.question
        return input(question).lower() != "n"
        
    def centered_text(self, text):
        return int((self.width - len(text))/2)*" " + text
    
    def horizointal_line(self):
        return "="*self.width

    def padding_vertical(self, times):
        return "\n"*times

# s = MenuScreen().with_header("test").with_question("press any key").build()
