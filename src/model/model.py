import shutil, os, datetime
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(emailDestinatario, assunto, mensagem):
    try:
        smtpObj = smtp.SMTP('smtp.gmail.com', 587)
        conexao = smtpObj.ehlo()

        smtpObj.starttls()

        emailRemetente = 'pythonemail08@gmail.com'

        smtpObj.login(emailRemetente, 'nwwe ossa loxf shlp')

        msg = MIMEMultipart()
        msg['From'] = emailRemetente
        msg['To'] = emailDestinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain', 'utf-8'))

        caminhoRelatorioTxt = 'C:\\Users\\paulo.welton\\relatorio.txt'
        attachment = open(caminhoRelatorioTxt, 'rb')

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', f'attachment; filename=relatorio.txt')
        attachment.close()
        msg.attach(att)

        smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())

        print('email enivado com sucesso')

        smtpObj.quit()
    except Exception as e:
        print(f"ocorreu um erro: {e}")

def backup_arquivos(caminho):
    try:
        caminhoBackupPrincipal = 'C:\\backup_python'
        nomeBackup = 'Backup ' + str(datetime.date.today())
        caminhoBackup = os.path.join(caminhoBackupPrincipal, nomeBackup)

        if not os.path.exists(caminhoBackup):
            os.makedirs(caminhoBackup)
        else:
            raise Exception('arquivo existente')
        
        relatorioTxt = open('C:\\Users\\paulo.welton\\relatorio.txt', 'a')
        caminhoRelatorioTxt = 'C:\\Users\\paulo.welton\\relatorio.txt'
        
        for filename in os.listdir(caminho):
            relatorioTxt.write(filename + '\n')    
            caminhoArquivo = os.path.join(caminho, filename)

            if os.path.isfile(caminhoArquivo):
                shutil.copy2(caminhoArquivo, caminhoBackup)
            elif os.path.isdir(caminhoArquivo):
                shutil.copytree(caminhoArquivo, os.path.join(caminhoBackup, filename))

        relatorioTxt.close()

        print("arquivos salvos com sucesso")

        destinatario = 'paulinho.welton08@gmail.com'
        assunto = 'Subject:BACKUP MENSAL DE ARQUIVOS\n'
        mensagem = 'Ola o backup mensal de arquivos do seu computador foi gerado\n os seguintes arquivos foram salvos: '                

        #* envia um email com um assunto, mensagem e um relatorio anexado
        enviar_email(destinatario, assunto, mensagem)
        
        #* apaga o arquivo gerado que foi enviado para o email
        os.unlink(caminhoRelatorioTxt)
    except Exception as e:
        print(f"ocorreu um erro: {e}")


def organizar_arquivos(caminho):
    Documentos = 'C:\\Users\\paulo.welton\\Documents'
    Imagens = 'C:\\Users\\paulo.welton\\Pictures'
    Musica = 'C:\\Users\\paulo.welton\\Music'
    Videos = 'C:\\Users\\paulo.welton\\Videos'

    extensaoDocumentos = ['.pdf', '.txt']
    extensaoImagens = ['.png', '.jpg', '.jpeg', '.svg']
    extensaoMusica = ['.mp3']
    extensaoVideos = ['.mp4']

    listaArquivos = os.listdir(caminho)

    for filename in listaArquivos:
        caminhoArquivo = caminho + '\\' + filename
        
        if os.path.isfile(caminhoArquivo):
            if any(filename.endswith(ext) for ext in extensaoDocumentos):
                shutil.move(caminhoArquivo, Documentos)
            if any(filename.endswith(ext) for ext in extensaoImagens):
                shutil.move(caminhoArquivo, Imagens)
            if any(filename.endswith(ext) for ext in extensaoMusica):
                shutil.move(caminhoArquivo, Musica)
            if any(filename.endswith(ext) for ext in extensaoVideos):
                shutil.move(caminhoArquivo, Videos)

    print('arquivo: ' + filename + ' inserido')