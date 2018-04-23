# Teste
Como utilizamos sistemas legados feitos em delphi, são poucas as ferramentas no mercado para automatizar testes em aplicações desktop (e as poucas que existem são pagas e fora do nosso orçamento). 

Como não queria ficar repetindo o teste no menu arquivo em toda nova versão, resolvi criar alguns scripts em Python 3 utilizando PyAutoGUI, para testar o menu mais usado do sistema de recursos humanos. Apesar de básico, o teste poupa bastante tempo!

# PyAutoGUI 
É um módulo Python que possibilita simular a utilização da interface, mouse e teclado, além de outras opções que está na documentação e no código fonte, o que já facilita muito o trabalho de qualquer pessoa na automação de tarefas.

Documentação: http://pyautogui.readthedocs.io/en/latest/index.html

Código Fonte: https://github.com/asweigart/pyautogui

# Coordenadas do Mouse
Para pegar as coordenadas do mouse, onde ele deve clicar no sistema e etc, chamei um metódo do próprio PyAutoGUI:

import pyautogui
pyautogui.displayMousePosition()
