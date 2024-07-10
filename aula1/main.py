import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # configurar pausa entre comandos

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Abrir link do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Fazer login no sistema
pyautogui.click(x=1027, y=369)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("teste@gmail.com")

pyautogui.press("tab")

pyautogui.write("teste1234")
pyautogui.press("tab")
pyautogui.press("enter")

# Tela de cadastro
time.sleep(2)
pyautogui.click(x=1460, y=360)

# Importar base de dados para cadastro
tabela = pandas.read_csv("produtos.csv")

# Cadastrar
for linha in tabela.index: # .index - tdas as linhas da tabela
    pyautogui.click(x=1203, y=262)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")

    # pyautogui.scroll(2000)