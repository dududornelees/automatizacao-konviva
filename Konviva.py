import requests
import os


# Array com os arquivos à serem baixados
arquivos = [
    {"nome": "Maven - 3.6.3", "endereco": "maven.bin.zip", "url": "https://dlcdn.apache.org/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.zip"},
    {"nome": "Tomcat - 10.0.14", "endereco": "tomcat.zip", "url": "https://dlcdn.apache.org/tomcat/tomcat-10/v10.0.14/bin/apache-tomcat-10.0.14-windows-x64.zip"},
    {"nome": "Maria DB - 10.6", "endereco": "maria-db.msi", "url": "https://espejito.fder.edu.uy/mariadb//mariadb-10.6.5/winx64-packages/mariadb-10.6.5-winx64.msi"},
    {"nome": "Mongo DB - 5.0.5", "endereco": "mongo-db.msi", "url": "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.5-signed.msi"},
    {"nome": "Heidi SQL - 11.3", "endereco": "heidi-sql.exe", "url": "https://www.heidisql.com/installers/HeidiSQL_11.3.0.6295_Setup.exe"},
    {"nome": "OpenVPN - 2.5.5", "endereco": "open-vpn.msi", "url": "https://swupdate.openvpn.org/community/releases/OpenVPN-2.5.5-I602-amd64.msi"},
    {"nome": "NodeJS - 14.7.3", "endereco": "node-js.msi", "url": "https://nodejs.org/download/release/v14.17.3/node-v14.17.3-x64.msi"},
    {"nome": "Java - 8", "endereco": "java.exe", "url": "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=245448_4d5417147a92418ea8b615e228bb6935"},
    {"nome": "JDK - 1.8", "endereco": "jdk.exe", "url": "https://javadl.oracle.com/webapps/download/GetFile/1.8.0_202-b08/1961070e4c9b4e26a04e7f5a083f551e/windows-i586/jdk-8u202-windows-x64.exe"}
]

# Função para baixar e abrir os arquivos
def baixar_arquivo(nome_programa, endereco, url):
    resposta = requests.get(url)

    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)            
        print('Download finalizado, salvo como: {}'.format(endereco))
    else:
        resposta.raise_for_status()
        print('Ocorreu erro no download do programa: {}'.format(nome_programa))

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