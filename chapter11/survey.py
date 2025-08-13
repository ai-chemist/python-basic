class AnonymousSurvey:
    """Anonymous Survey"""

    def __init__(self, question):
        """Constructor"""
        self.question = question
        self.response = []

    def show_question(self):
        """Show question"""
        print(self.question)

    def store_response(self, new_response):
        """Store response"""
        self.response.append(new_response)

    def show_results(self):
        """Show results"""
        print("result\n")
        for response in self.response:
            print(f"\t- {response}")