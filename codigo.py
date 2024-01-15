#programa de Chat ao vivo
#sempre control s para salvar antes de executar


import flet as ft

def main(pagina):
    texto = ft.Text("Chat AO VIVO")

    chat = ft.Column()
    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        #adicionar mensagem no chat
        chat.controls.append(ft.Text(mensagem))
        #limpar campo de mensagem
        pagina.update()

        #PUBLISH SUBSCRIBE = PUBSUB
    pagina.pubsub.subscribe(enviar_mensagem_tunel)    
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all(campo_mensagem.value)
        #limpar campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        #adicionar chat
        pagina.add(chat)
        #fechar chat e remover botao de iniciar chat#
        popup.open = False
        #remover
        pagina.remove(botao_iniciar)
        #criar campo para digitaçao e botao de enviar chat
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title= ft.Text("Bem vindo ao Chat AO VIVO"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click = entrar_popup)], 
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("iniciar chat", on_click=entrar_chat)
    
  
  
  
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main)
