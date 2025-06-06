from datetime import datetime

class Tarefa:
    def __init__(self, id, titulo, descricao, data_entrega, status="pendente"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = data_entrega  # string no formato "YYYY-MM-DD"
        self.status = status

    def to_list(self):
        return [str(self.id), self.titulo, self.descricao, self.data_entrega, self.status]

    @staticmethod
    def from_list(data):
        return Tarefa(int(data[0]), data[1], data[2], data[3], data[4])
