import xml.etree.ElementTree as et 
import shutil
import random
import os

tree = et.parse('apartamento.xml') 
root = tree.getroot()

def pasta(caminho):
    pasta = caminho
    #verificar se a pasta existe se não existir ele ira criar
    if not os.path.exists(pasta):
        os.makedirs(pasta)

pasta(os.path.abspath('edificio1//'))
pasta(os.path.abspath('edificio1//edificio'))
pasta(os.path.abspath('edificio1//apartamentos//'))
pasta(os.path.abspath('moradia1//'))

caminho_origem = os.path.abspath('arquivo.xml')
caminho_destino = 'edificio1//edificio//edificio1.xml'

shutil.copy(caminho_origem,caminho_destino)
        
final = 9
for i in range(1, (final + 1)):
    tree.write(f'edificio1//apartamentos//apartamento{i}.xml')
    xml_inserir = et.parse(f'edificio1//apartamentos//apartamento{i}.xml')
    elemento_pai_inserir = xml_inserir.getroot()
    xml_principal = et.parse(f'edificio1//edificio//edificio{i}.xml')
    elemento_pai_princial = xml_principal.find('.//ucs')
    elemento_pai_princial.append(elemento_pai_inserir)
    fim = final - 1
    xml_principal.write(f'edificio1//edificio//edificio{i+1}.xml')

    caminho_origem = f'edificio1//edificio//edificio{fim}.xml'
    caminho_destino = f'edificio1//edificio.xml'

shutil.move(caminho_origem,caminho_destino)

def modificar_xml():
    # Carregando o arquivo XML 
    tree = et.parse('edificio1//edificio.xml') 
    root = tree.getroot()

    elementos_destinacao = root.findall(".//uc/destinacao")
    elementos_complemento3 = root.findall(".//uc/id_complemento3")
    elementos_argumento = root.findall(".//uc/argumento3")
    elementos_complemento4 = root.findall(".//uc/id_complemento4")
    elementos_logico = root.findall(".//uc/argumento4_logico")
    elementos_real = root.findall(".//uc/argumento4_real")
    
    for elemento in elementos_destinacao:
        # Faz algo com o elemento
        elemento.text = 'RESIDENCIA'

    for elemento in elementos_complemento3:
        # Faz algo com o elemento
        elemento.text = '9'                                     

    for elemento in elementos_argumento:
        # Faz algo com o elemento
        elemento.text = '1009'

    for elemento in elementos_complemento4:
        # Faz algo com o elemento
        elemento.text = '7'

    for elemento in elementos_logico:
        # Faz algo com o elemento
        elemento.text = '10' 

    for elemento in elementos_real:
        # Faz algo com o elemento
        elemento.text = '10'        
                                                                                         
    tree.write('edificio1//edificio1.xml')
    
modificar_xml()
minha_lista = []
for linha in range (6):
                    minha_lista.append(random.randint(1,9))
                    num = int(''.join(map(str,minha_lista)))
                    novo_numero = '20200824091321' + str(num)
                    
for linha in range(0,(final+2)):                    
    caminho_do_arquivo_edificio = os.path.abspath(f'edificio1//edificio//edificio{linha}.xml')
    caminho_do_arquivo_apartamentos = os.path.abspath(f'edificio1//apartamentos//apartamento{linha}.xml')
    
    #deletar arquivo xml
    try:  
        os.remove(caminho_do_arquivo_apartamentos)
    except:
        pass
    try:
        os.remove(caminho_do_arquivo_edificio)
    except:
        pass
        
caminho_do_arquivo_edificio = os.path.abspath(f'edificio1//edificio.xml')
caminho_do_arquivo_edificio1 = os.path.abspath(f'edificio1//edificio1.xml')
try:
    os.remove(caminho_do_arquivo_edificio)
except:
    pass

shutil.make_archive(f'survey//KLAYTON_{novo_numero}','zip','./','edificio1//edificio1.xml',)

try:
    os.remove(caminho_do_arquivo_edificio1)
except:
    pass

