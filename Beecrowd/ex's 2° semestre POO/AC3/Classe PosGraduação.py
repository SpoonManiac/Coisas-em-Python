class PosGraduacao:
    def __init__(self, instituição, curso):
        self.instituição = instituição
        self.curso = curso

    def get_curso(self):
        ... # na subclasse retornará a string 'Doutorado em' + nome do curso

class Doutorado(PosGraduacao):
    def __init__(self, instituição, curso, tese):
        super().__init__(instituição, curso)
        self.__tese = tese

    def get_curso(self):
        return f'Doutorado em {self.curso}'

    def get_tese(self):
        return self.__tese
    
    def set_tese(self, titulo):
        self.titulo = titulo


leleco= Doutorado('Instituto do GraU',
                  'Tutorial de como dar um grau bonito', 
                  'Lalau pra quem quer dar grau')
print(leleco._Doutorado__tese)