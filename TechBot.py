from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class TechBot:
    def __init__(self):
        self.naosei = "Não entendi sua pergunta."
        conversa = ['Oi', 'Olá',
                    'Assembly', 'Vc é maluco',
                    'Filmes', 'Que filmes vc gosta?'
                    'Tudo bem?', 'Tudo ótimo',
                    'Você gosta de programar?', 'Sim, eu programo em Python']
        self.chatbot = ChatBot("TechBot")
        self.trainer = ListTrainer(self.chatbot)
        self.trainer.train(conversa)

    def get_response(self, question: str):
        response = self.chatbot.get_response(question)
        print(f'Confidence is {response.confidence}')
        if response.confidence < 0.5:
            return self.naosei
        else:
            return response


