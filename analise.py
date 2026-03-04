class Equipe:
    def __init__(self, titulo):
        self.nomeEquipe = titulo
        self.time = []

    def add_membros(self, nome, rendimento):
        self.time.append({"nome" : nome,
                          "rendimento" : rendimento})
        self.time.sort(key=lambda x: x["nome"])

    def __str__(self):
        conteudo = (f'Equipe: {self.nomeEquipe} ({len(self.time)}) \nMembros - Rendimento\n')
        for membro in self.time:
            conteudo += f'{membro["nome"]} - {membro["rendimento"]}\n'
        return conteudo.strip()

class Desempenho:
    def __init__(self, equipe):
        self.equipe = equipe

    def rendimento (self):
        total=0
        melhor = max(self.equipe.time, key=lambda x: x["rendimento"])
        menor = min(self.equipe.time, key=lambda x: x["rendimento"])
        for renda in self.equipe.time:
            total += (renda["rendimento"])
        media = total / len(self.equipe.time)
        conteudo = (f'O rendimento total da equipe foi R${total:.2f} \n')
        conteudo += (f'A média de vendas da equipe foi de R${media:.2f} \n')
        conteudo += (f'Quem teve o maior rendimento foi {melhor["nome"]} com R${melhor["rendimento"]} \n')
        conteudo += (f'Quem teve o menor rendimento foi {menor["nome"]} com R${menor["rendimento"]} \n')
        conteudo += ('RANKING \n')
        ranking = sorted(self.equipe.time, key=lambda x: x["rendimento"], reverse=True)
        for i, vendedor in enumerate (ranking, 1):
            conteudo += (f'{i}. {vendedor["nome"]:<5} - R${vendedor["rendimento"]} \n')
            
        return conteudo
    
equipe1 = Equipe('CarlosEquipe')
equipe1.add_membros('Lucas', 1900)
equipe1.add_membros('Ana', 2200)
equipe1.add_membros('João', 4800)
totais = Desempenho(equipe1)
print(equipe1)
print(totais.rendimento())
