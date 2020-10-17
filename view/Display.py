import os


def header_with_message_content(msg):
    return """
              _____                              
             |A .  | _____                  
             | /.\ ||A ^  | _____            
             |(_._)|| / \ ||A _  | _____     
             |  |  || \ / || ( ) ||A_ _ |    
             |____V||  .  ||(_'_)||( v )|           {{message}}
                    |____V||  .  ||     |     
                           |____V||  .  |      
                                  |____V|     
    """.replace("{{message}}", msg)


def padding_vertical(times):
    return "\n" * times


class ScreenBuilder:

    def __init__(self):
        self.centered_question = False
        self.header = header_with_message_content("Blackjack Night")
        self.question = "press enter to continue.."
        self.width = 95
        self.body = ""

    def width_width(self, width):
        self.width = width
        return self

    def with_body(self, body):
        self.body = body
        return self

    def with_centered_question(self):
        self.centered_question = True
        return self

    def with_header(self, header):
        self.header = header_with_message_content(header)
        return self

    def with_question(self, question):
        self.question = question
        return self

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def build(self):
        self.clear()
        print(self.header)
        print(self.horizointal_line())
        print(padding_vertical(1))
        print(self.body)
        print(padding_vertical(1))

    def build_and_get_input(self):
        self.build()
        question = self.centered_text(self.question) if self.centered_question else self.question
        return input(question)

    def centered_text(self, text):
        return int((self.width - len(text)) / 2) * " " + text

    def horizointal_line(self):
        return "=" * self.width

# s = MenuScreen().with_header("test").with_question("press any key").build()
