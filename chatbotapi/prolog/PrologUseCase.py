from pyswip import Prolog


class PrologUseCase:

    def __init__(self, database="./bot.pl"):

        self.prolog = Prolog()
        self.prolog.consult(database)

    def make_question(self, question):

        for response in self.prolog.query(f"saludo('{question}', Response)"):
            return response
        
        for response in self.prolog.query(f"responder('{question}', Response)"):
            return response


if __name__ == "__main__":
    prolog = PrologUseCase().make_question("python")
    print(prolog)
