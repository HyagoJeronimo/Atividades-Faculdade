# Armazenar tarefas (por enquanto em memória)
tarefas = []

# Loop infinito até o usuário escolher sair
while True:
        # Exibir menu
        print("\n=== TASK MANAGER v1.0 ===")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")
        print("4 - Deletar tarefa")

        opcao = input("\nEscolha uma opção: ")

        # Validar entrada
        if opcao not in ["1", "2", "3", "4"]:
            print("❌ Opção inválida! Digite 1, 2, 3 ou 4")
            continue
        
        #Processar opção
        if opcao == "1":
            # Subfunção: criar tarefa
            nome = input("nome da tarefa: ")
            if nome.strip():  # Validar que não esta vazio
                 tarefas.append(nome)
                 print(f"✅ Tarefa '{nome}' criada com sucesso")
            else:
                 print("❌ NOme da tarefa não pode ser vazio!")
        
        elif opcao == "2":
            # Subfunção: listar tarefas
            if len(tarefas) == 0:
                 print("➰ Nenhuma tarefa registrada ainda")
            else:
                 print("\n📋 Suas tarefas")
                 for i, tarefa in enumerate(tarefas, 1):
                    print(f"  {i}. {tarefa}")
          
        elif opcao  == "3":
             # Subfunção: sair
             print("🖐️ Até logo!")
             break 
        
        # Ao listar, mostar o total de tarefas
        if opcao == "2":
             print(f"\n🔢 Total de tarefas: {len(tarefas)}")

        # Adicionar opção 4: deletar tarefa
        elif opcao == "4":
             if len(tarefas) == 0:
                  print("➰ Nenhuma tarefa para deletar")
             else:
                  print("\n📋 Tarefas disponíveis para deletar")
                  for i, tarefa in enumerate(tarefas, 1):
                     print(f"  {i}. {tarefa}")
                  try:
                       escolha = int(input("Digite o número da tarefa para deletar: "))
                       if 1 <= escolha <= len(tarefas):
                            deletada = tarefas.pop(escolha - 1)
                            print(f"✅ Tarefa '{deletada}' deletada com sucesso")
                       else:
                            print("❌ Número inválido!")
                  except ValueError:
                       print("❌ Entrada inválida! Digite um número.")
