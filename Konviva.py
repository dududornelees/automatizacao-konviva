from clint.textui import progress
import requests
import os


# Array com os arquivos à serem baixados
arquivos = [
    {"nome": "Maven - 3.6.3", "endereco": "maven.bin.zip", "url": "https://dlcdn.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.zip"},
    {"nome": "Tomcat - 9.0.58", "endereco": "tomcat.zip", "url": "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.58/bin/apache-tomcat-9.0.58.zip"},
    {"nome": "Maria DB - 10.6", "endereco": "maria-db.msi", "url": "https://espejito.fder.edu.uy/mariadb//mariadb-10.6.5/winx64-packages/mariadb-10.6.5-winx64.msi"},
    {"nome": "Mongo DB - 5.0.5", "endereco": "mongo-db.msi", "url": "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.5-signed.msi"},
    {"nome": "Heidi SQL - 11.3", "endereco": "heidi-sql.exe", "url": "https://www.heidisql.com/installers/HeidiSQL_11.3.0.6295_Setup.exe"},
    {"nome": "OpenVPN - 2.5.5", "endereco": "open-vpn.msi", "url": "https://swupdate.openvpn.org/community/releases/OpenVPN-2.5.5-I602-amd64.msi"},
    {"nome": "NodeJS - 14.7.3", "endereco": "node-js.msi", "url": "https://nodejs.org/download/release/v14.17.3/node-v14.17.3-x64.msi"},
    {"nome": "Java - 8", "endereco": "java.exe", "url": "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245448_4d5417147a92418ea8b615e228bb6935"},
    {"nome": "JDK - 1.8 301", "endereco": "jdk.exe", "url": "https://download.oracle.com/otn/java/jdk/8u301-b09/d3c52aa6bfa54d3ca74e617f18309292/jdk-8u301-windows-x64.exe?AuthParam=1642430249_35b16b502ea9dd1873d117017ab3c3b0"}
]

# Função para baixar e abrir os arquivos
def baixar_arquivo(nome_programa, endereco, url):
    resposta = requests.get(url)

    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            tamanho_total = int(resposta.headers.get('content-length'))

            for chunk in progress.bar(resposta.iter_content(chunk_size = 1024), expected_size=(tamanho_total / 1024) + 1):
                if chunk:
                    novo_arquivo.write(chunk)
                    novo_arquivo.flush()
            novo_arquivo.write(resposta.content)
        print('Download finalizado, salvo como: {}'.format(endereco))
        print('')
    else:
        resposta.raise_for_status()
        print('Ocorreu erro no download do programa: {}'.format(nome_programa))
        print('')

def abrir_arquivo(endereco):
    os.startfile(os. getcwd() + '/' + endereco)

for arquivo in arquivos:
    print('Baixando: {}...'.format(arquivo["nome"]))
    baixar_arquivo(arquivo["nome"], arquivo["endereco"], arquivo["url"])
    abrir_arquivo(arquivo["endereco"])


# Mensagem final
print("")
print("******************************************")
print("*** Todos os programas foram baixados! ***")
print("******************************************")

print("")
input("Enter para finalizar...")