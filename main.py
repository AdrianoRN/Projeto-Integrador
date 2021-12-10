import Funcoes 
import Apuracao 
import Lista

opcao = Funcoes.criarMenu()
while opcao != 4:
    if opcao == 1:
        print("\n")
        Lista.lista_votacao()
    elif opcao == 2:
        
#votação a Governador
        Funcoes.votacao_governador()
        print("\n")
       
# Votação a presidente

        Funcoes.votacao_presidente() 
            
#Apuração dos votos 

    elif opcao == 3:
        print("Apuração dos Votos\n")
        Apuracao.apuracao_votos()          
 
    else: 
        print("Opção inválida.")
    print("\n")
    opcao = Funcoes.criarMenu()
    

print("Obrigado por utilizar a Urna Eletrônica!")






