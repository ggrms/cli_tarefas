import csv, re
from datetime import datetime
from models.tarefa import Tarefa

ARQUIVO = "tarefas.csv"

def carregar_tarefas():
    tarefas = []
    try:
        with open(ARQUIVO, mode="r", newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                tarefas.append(Tarefa.from_list(linha))
    except FileNotFoundError:
        pass
    return tarefas

def salvar_tarefas(tarefas):
    with open(ARQUIVO, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for tarefa in tarefas:
            writer.writerow(tarefa.to_list())

def exportar_pendentes(tarefas):
    with open("relatorio_pendentes.txt", mode="w", encoding="utf-8") as f:
        for t in tarefas:
            if t.status == "pendente":
                f.write(f"{t.id} - {t.titulo} (até {t.data_entrega})\n")

def valida_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False
