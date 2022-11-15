#importando as bibliotecas
import smtplib #utilizado para fazer conexão com o servidor SMTP
from email.mime.multipart import MIMEMultipart #criado para carregar os valores corretos de headers
from email.mime.text import MIMEText #criado para inserir o texto do e-mail
import getpass #utilizado para pedir a senha do e-mail

#fazendo a configuração do e-mail de envio via outlook
host = 'smtp.office365.com'
port = 587

#vamos configurar o e-mail que será usado, bem como sua senha
print('Seus dados para envio')
user = input('Insira seu e-mail como nome@outlook.com:' )

print('Obrigado! Agora sua senha')
password = getpass.getpass()

#Criando o objeto servidor
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

#Fazendo login no servidor do objeto criado
print('Fazendo login no servidor...')
server.ehlo()
server.starttls()
server.login(user, password)

#Criando mensagem
message = '''Olá, tudo bem?
             Mensagem enviada via código em Python :)
             Abraços
        '''
print('Criando a mensagem...')

email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = input('Adicione o e-mail para quem deseja enviar: ')
email_msg['Subject'] = 'Enviando meu primeiro e-mail com Python!'

print('Adicionando o texto e seus headers...')
email_msg.attach(MIMEText(message, 'plain'))

#Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

#Mensagem enviada e saindo do servidor
print('Mensagem enviada com sucesso!')
server.quit()