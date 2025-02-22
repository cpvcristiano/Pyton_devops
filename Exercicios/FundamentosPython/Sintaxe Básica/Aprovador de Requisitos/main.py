from src.application.output import mostra_boas_vindas, mostra_mensagem
from src.application.input import pega_dados
from src.application.negocio import Pessoa

if __name__ == "__main__":
    mostra_boas_vindas()
    

    nome, idade, altura = pega_dados()
    
    pessoa = Pessoa(nome, idade, altura)
    
    mostra_mensagem(pessoa.verificar_idade())
    mostra_mensagem(pessoa.verificar_altura())
    mostra_mensagem(pessoa.verificar_aprovacao())
