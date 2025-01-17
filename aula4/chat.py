import flet as ft

def main(pagina): # definindo uma funcao
    titulo = ft.Text("Chat", size=30) # criando elemento título

    tituloPopup = ft.Text("Bem-vindo(a)")
    nomeUsuario = ft.TextField(label="Digite seu nome")

    def enviarMensagemTunel(msg):
        chat.controls.append(ft.Text(msg))
        pagina.update()

    pagina.pubsub.subscribe(enviarMensagemTunel) # cria a comunicacao entre tds os usuarios

    def enviarMensagem(evento):
        texto = f"{nomeUsuario.value}: {mensagem.value}"

        pagina.pubsub.send_all(texto) # enviar msg no tunel

        mensagem.value = ""

        pagina.update()

    mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviarMensagem) # quando apertar enter tmb enviar msg
    botaoEnviar = ft.ElevatedButton("Enviar", on_click=enviarMensagem)

    linhaMensagem = ft.Row([mensagem, botaoEnviar]) # aparecer na mesma linha
    chat = ft.Column() # add mensagem dentro deste campo/coluna

    def entrarChat(evento):
        # fechar elementos que estao abertos
        pagina.remove(titulo)
        pagina.remove(botaoIniciar)
        popup.open = False

        # criar tela do chat
        pagina.add(chat)
        pagina.add(linhaMensagem)

        # notificar que entrou um usuario
        notificacao = f"{nomeUsuario.value} entrou no chat" #valor dinamico = f"{valorDinamico} awdaowhd texto"
        pagina.pubsub.send_all(notificacao)

        pagina.update()

    botaoEntrar = ft.ElevatedButton("Entrar no chat", on_click=entrarChat)

    popup = ft.AlertDialog(
        title= tituloPopup,
        content= nomeUsuario,
        actions= [botaoEntrar] # lista com tds os botoes
        )    

    def abrirPopup(evento): # funcao que esta dentro de um botao deve receber evento como parametro
        # pagina.dialog = popup # antes este comando funcionava
        pagina.overlay.append(popup) # dps da atualizacao precisa usar esse
        popup.open = True

        pagina.update() # atualizar tela para aparecer os novos elementos

    botaoIniciar = ft.ElevatedButton("Iniciar chat", on_click=abrirPopup)

    pagina.add(titulo)
    pagina.add(botaoIniciar)

ft.app(main, view=ft.WEB_BROWSER) # executar sistema