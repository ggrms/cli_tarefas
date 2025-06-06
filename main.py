from models.tarefa import Tarefa
from utils import carregar_tarefas, salvar_tarefas, exportar_pendentes, valida_data


def gerar_id(tarefas):
    return max([t.id for t in tarefas], default=0) + 1

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n[1] Adicionar")
        print("[2] Listar")
        print("[3] Marcar como concluída")
        print("[4] Deletar")
        print("[5] Exportar pendentes")
        print("[6] Sair")

        opcao = input("Escolha: ")
        
        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data_entrega = input("Data de entrega (YYYY-MM-DD): ")
            while(valida_data(data_entrega) == False):
                print("Data Inválida. Favor inserir uma nova data!")
                data_entrega = input("Data de entrega (YYYY-MM-DD): ")
            nova = Tarefa(gerar_id(tarefas), titulo, descricao, data_entrega)
            tarefas.append(nova)
            salvar_tarefas(tarefas)
            print("Tarefa adicionada!")

        elif opcao == "2":
            if(len(tarefas) == 0):
                print("Não existem tarefas criadas.")
            for t in tarefas:
                print(f"[{t.id}] {t.titulo} - {t.status} (até {t.data_entrega})")

        elif opcao == "3":
            tarefa_inexistente = True
            if(len(tarefas) == 0):
                print("Não existem tarefas a serem concluídas.")
                tarefa_inexistente = False
            else:
                id_alvo = int(input("ID da tarefa: "))
                for t in tarefas:
                    if t.id == id_alvo:
                        t.status = "concluída"
                        tarefa_inexistente = False
                        break
                if(tarefa_inexistente):
                    print("Não existe tarefa com o ID correspondente a ser concluída")
                else:
                    salvar_tarefas(tarefas)

        elif opcao == "4":
            tam_tarefas = len(tarefas)
            if(tam_tarefas == 0):
                print("Não existem tarefas criadas.")
            else:
                id_alvo = int(input("ID da tarefa: "))
                tarefas = [t for t in tarefas if t.id != id_alvo]
                if(tam_tarefas == len(tarefas)):
                    print("Não existe tarefa com o ID correspondente")
                else:
                    salvar_tarefas(tarefas)

        elif opcao == "5":
            exportar_pendentes(tarefas)
            print("Relatório exportado para 'relatorio_pendentes.txt'.")

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
