import pyautogui 

# Testes de Validação das Telas do menu Arquivo, para a Release 5.0.0.0 do Sistema ARH

# Função para percorrer o Menu Arquivo 
def menuArquivo():
	pyautogui.moveTo(60, 30); pyautogui.click()

def opcaoCompetencia():
	pyautogui.moveTo(100, 55); pyautogui.click()

def opcaoUsuarios():
	pyautogui.moveTo(100, 85); pyautogui.click()

def opcaoConfiguracoes():
	pyautogui.moveTo(100, 105); pyautogui.click()

# Competencia
menuArquivo()
pyautogui.moveTo(100, 55); pyautogui.click()
# Selecionar Competencia
#pyautogui.moveTo(400, 55)#; pyautogui.click()
#pyautogui.moveTo(765, 100, 0.50); pyautogui.click()

# Relatório de Inconsistencia de Abertura
#pyautogui.moveTo(400, 55)#; pyautogui.click()

# Reabrir Competencia
#pyautogui.moveTo(400, 75)#; pyautogui.click()

# Folha Complementar
#pyautogui.moveTo(400, 125)#; pyautogui.click()

# Usuarios do Sistema
pyautogui.moveTo(100, 85); pyautogui.click()

# Configuracoes
pyautogui.moveTo(100, 105); pyautogui.click()

# Cancelamento
pyautogui.moveTo(100, 135); pyautogui.click() 

# Manutenção de Cadastros
pyautogui.moveTo(100, 155); pyautogui.click() 

# Utilitarios
pyautogui.moveTo(100, 180); pyautogui.click()

# Logoff
#pyautogui.moveTo(100, 200); pyautogui.click()

# Bloqueio de Estacao
#pyautogui.moveTo(100, 235); pyautogui.click()

# Desenvolvimento
pyautogui.moveTo(100, 245); pyautogui.click() 

# Sair do Sistema
#pyautogui.moveTo(100, 290); pyautogui.click()
pyautogui.alert('O teste acabou!')