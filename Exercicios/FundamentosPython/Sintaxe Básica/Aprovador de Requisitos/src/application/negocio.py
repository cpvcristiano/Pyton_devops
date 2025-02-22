class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def verificar_idade(self):
        
        if self.idade >= 18:
            return " Você é maior de idade."
        else:
            return "Você é menor de idade."

    def verificar_altura(self):
        
        altura_minima = 1.50
        if self.altura >= altura_minima:
            return f"Você tem altura suficiente ({self.altura:.2f}m)."
        else:
            return f"Você não atinge a altura mínima de {altura_minima:.2f}m."

    def verificar_aprovacao(self):
        
        altura_minima = 1.50
        if self.idade >= 18 and self.altura >= altura_minima:
            return "**Parabéns! Aprovado**"
        else:
            return "**Infelizmente,você não foi aprovado.**"
