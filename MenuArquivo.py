# Testes de Validacao das Telas do menu Arquivo, para a Release 5.0.0.0 do Sistema ARH

import pyautogui 

# Funcao para sumular clique do mouse
def clique():
	pyautogui.click(interval=1)

# Funcao para percorrer o Menu Arquivo 
def menuArquivo():
	pyautogui.moveTo(35, 25); clique()

# Funcao para fechar a tela pelo botão Esc
def fecharTela():
	pyautogui.hotkey('esc')

# Funcao para percorrer a opcao Competencia
def opcaoCompetencia():
	menuArquivo()
	pyautogui.moveTo(100, 55); clique()

def opcaoCompetenciaFolha():
	opcaoCompetencia()
	pyautogui.moveTo(400, 125); clique()
	pyautogui.moveTo(400, 125); clique()

# Selecionar Competencia
opcaoCompetencia()
pyautogui.moveTo(400, 55); clique()
fecharTela()

# Criar Competencia
opcaoCompetencia()
pyautogui.moveTo(375, 80); clique()
fecharTela()

# Reabrir Competencia
opcaoCompetencia()
pyautogui.moveTo(400, 95); clique()
fecharTela()

# Folha Complementar
# Criar Folha
opcaoCompetenciaFolha()
pyautogui.moveTo(665, 125); clique()
fecharTela()

# Folha Complementar
# Manutencao Folha
opcaoCompetenciaFolha()
pyautogui.moveTo(665, 145); pyautogui.click()
pyautogui.moveTo(585, 500); pyautogui.click()

def opcaoUsuarios():
	menuArquivo()
	pyautogui.moveTo(100, 85); pyautogui.click()

# Grupo de Usuarios
opcaoUsuarios()
pyautogui.moveTo(380, 85); pyautogui.click(interval=2)
fecharTela()

# Habilitar Usuario
opcaoUsuarios()
pyautogui.moveTo(380, 105); clique()
fecharTela()

# Reiniciar Senha do Usuario
opcaoUsuarios()
pyautogui.moveTo(380, 125); clique()
fecharTela()

def opcaoConfiguracoes():
	menuArquivo()
	pyautogui.moveTo(100, 105); clique()

# Percorre as telas da opcao ATS
opcaoConfiguracoes()
pyautogui.moveTo(360, 115); clique()
pyautogui.moveTo(230, 130); clique()
pyautogui.moveTo(285, 130); clique()
pyautogui.moveTo(370, 130); clique()
pyautogui.moveTo(440, 130); clique()
fecharTela()

# Ferias e Decimo Terceiro
opcaoConfiguracoes()
pyautogui.moveTo(360, 135); clique()
fecharTela()

# Percorre as telas da opcao Operacoes Internas
opcaoConfiguracoes()
pyautogui.moveTo(360, 155); clique()
pyautogui.moveTo(230, 130); clique()
pyautogui.moveTo(285, 130); clique()
pyautogui.moveTo(345, 130); clique()
pyautogui.moveTo(415, 130); clique()
pyautogui.moveTo(500, 130); clique()
pyautogui.moveTo(555, 130); clique()
fecharTela()

# Percore as telas da opcao Mensal
opcaoConfiguracoes()
pyautogui.moveTo(360, 175); clique()
pyautogui.moveTo(235, 130); clique()
pyautogui.moveTo(325, 130); clique()
fecharTela()

# Percore as telas da opcao Gerador de Arquivos
opcaoConfiguracoes()
pyautogui.moveTo(360, 200); clique()
pyautogui.moveTo(285, 130); clique()
fecharTela()

# Percore as telas da opcao Calculo
opcaoConfiguracoes()
pyautogui.moveTo(360, 225); clique()
pyautogui.moveTo(260, 130); clique()
pyautogui.moveTo(390, 130); clique()
pyautogui.moveTo(485, 130); clique()
fecharTela()

def opcaoCancelamento():
	menuArquivo()
	pyautogui.moveTo(100, 135); clique()

# Competencia
opcaoCancelamento()
pyautogui.moveTo(350, 145); clique()
fecharTela()

# Contrato
opcaoCancelamento()
pyautogui.moveTo(350, 165); clique()
fecharTela()

def opcaoMntCadastros():
	menuArquivo()
	pyautogui.moveTo(100, 155); clique()

# Altera data de Admissao
opcaoMntCadastros()
pyautogui.moveTo(400, 155); clique()
fecharTela()

# Corrigir 1a Data de Transferencia
#opcaoMntCadastros()
#pyautogui.moveTo(400, 185); pyautogui.click()
#fecharTela()

# Reimportacao de Cadastro Mensais
#opcaoMntCadastros()
#pyautogui.moveTo(400, 205); pyautogui.click()
#fecharTela()

# Transfere Classe Nivel Automático
#opcaoMntCadastros()
#pyautogui.moveTo(400, 230); pyautogui.click()
#fecharTela()

# Exclui Movimentacao – Contrato
#opcaoMntCadastros()
#pyautogui.moveTo(400, 255); pyautogui.click()
#fecharTela()

# Lancamento Automatico de Rescisao
#opcaoMntCadastros()
#pyautogui.moveTo(400, 275); pyautogui.click()
#fecharTela()

# Diarias e Funcoes (Carga Inicial)
opcaoMntCadastros()
pyautogui.moveTo(400, 295); clique()
fecharTela()

# Diarias e Funcoes (Revogacoes)
opcaoMntCadastros()
pyautogui.moveTo(400, 310); clique()
fecharTela()

# Manutencao de Classes Niveis (APLIC)
#opcaoMntCadastros()
#pyautogui.moveTo(400, 340); pyautogui.click()
#fecharTela()

def dadosSiope():
	opcaoMntCadastros()
	pyautogui.moveTo(400, 365); pyautogui.click()

# Dados SIOPE - Escolas
#dadosSiope()
#pyautogui.moveTo(600, 365); pyautogui.click()
#pyautogui.moveTo(805, 200); pyautogui.click()
#pyautogui.moveTo(780, 175); pyautogui.click()


def opcaoUtilitarios():
	menuArquivo()
	pyautogui.moveTo(100, 180); pyautogui.click()

# Senha de Liberacao
opcaoUtilitarios()
pyautogui.moveTo(380, 180); clique()
pyautogui.moveTo(750, 525); pyautogui.click()

# Ajuste do Relogio Interno
opcaoUtilitarios()
pyautogui.moveTo(380, 200); clique()
pyautogui.moveTo(655, 115); pyautogui.click()

# Agenda de Atividades
opcaoUtilitarios()
pyautogui.moveTo(380, 225); clique()
fecharTela()

# Calculadora
opcaoUtilitarios()
pyautogui.moveTo(380, 245); clique()
pyautogui.moveTo(655, 290); pyautogui.click()

# Visualizador de Avisos e Notificacoes
opcaoUtilitarios()
pyautogui.moveTo(380, 265); clique()
fecharTela()

# Liberacao de Usuario
opcaoUtilitarios()
pyautogui.moveTo(380, 290); clique()
pyautogui.moveTo(540, 100); pyautogui.click()

# LogOff do Sistema
def opcaoLogoff():
	menuArquivo()
	pyautogui.moveTo(100, 200); pyautogui.click()

# Bloqueio da Estacao
def opcaoBloqEstacao():
	menuArquivo()
	pyautogui.moveTo(100, 235); pyautogui.click()

# Sair do Sistema
def opcaoSairSistema():
	menuArquivo()
	pyautogui.moveTo(100, 290); pyautogui.click()

pyautogui.alert(text='O TESTE ACABOU!!!', title='Quality Sistemas - Sistema ARH', button='OK')