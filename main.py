import re
#([a-zA-Z]*[\s]*=[\s]*([{])*([\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\\\/\(\)\-]|[{][\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\\\/\(\)\-]+[}])*([}])*[ ]*,)|([a-zA-Z]*[\s]*=[\s]*(["])*[\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:{}&=.,\\;\\\/\(\)\-]+(["])*[ ]*,?)

def findFirst(idlinha):
    for i in idlinha:
        if i == '{':
            return '{'
        elif i == '"':
            return '"'
        else:
            return '='


def addbloco(bloco, info):
    padraoLinhas = '([a-zA-Z]*[\s]*=[\s]*([{])*([\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\\\/\(\)\-]|[{][\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\\\/\(\)\-]+[}])*([}])*[ ]*,)|([a-zA-Z]*[\s]*=[\s]*(["])*[\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:{}&=.,\\;\\\/\(\)\-]+(["])*[ ]*,?)'
    padraoTag = '@[a-zA-Z]+{[a-zA-Z0-9:.-]+'
    tag = re.search(padraoTag, bloco)
    match = str(re.split('{', tag.group())[0]).title()
    chave = str(re.split('{', tag.group())[1])

    if match not in info:
        info[match] = {chave: {}}
    else:
        info[match][chave] = {}

    for linha in re.finditer(padraoLinhas, bloco):
        idlinha = re.split('=', linha.group().title())[0]
        idlinha = str(idlinha).strip()
        char = findFirst(re.split('=', linha.group().title())[1])
        if char == '{':
            infoLinha = re.split('{', linha.group().title(),maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha[:-2]
        elif char == '"':
            infoLinha = re.split('"', linha.group().title(),maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha
        else:
            infoLinha = re.split('=', linha.group().title(),maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha[:-2]


    #print(info)
    return info

def analisa(txt):
    espacogrande = '&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160'
    espaco = '&#160&#160&#160'
    f = open(txt, encoding='utf-8')
    content = f.read()
    info = {}
    conta=0
    detetaBloco = '@[a-zA-Z]+{([\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\"\\\/\(\)\-{}])+'
    for bloco in re.finditer(detetaBloco,content):
        conta+=1
        info = addbloco(bloco.group(),info)



    print(info['@Inproceedings']['RPA99'])

    f.close()
    e = open('converte.html', 'w')
    e.write('<html>\n\t<body>\n\t\t<p>\n')
    for tag in info:
        e.write('\t\t\t'+tag+':'+str(len(info[tag]))+'<br>\n')
        for chave in info[tag]:
            e.write('\t\t\t\t'+espacogrande+chave+'<br>\n')
            try:
                detailinfo = info[tag][chave]['Author']
                e.write('\t\t\t\t\t'+espacogrande+espacogrande+'Author: '+detailinfo+'<br>\n')
            except:
                pass
            try:
                detailinfo = info[tag][chave]['Title']
                e.write('\t\t\t\t\t' + espacogrande + espacogrande+'Title: ' + detailinfo + '<br>\n')
            except:
                pass

    e.write('\t\t</p>\n\t</body>\n</html>')
    e.close()






analisa('C:\\Users\\Bruno\\PycharmProjects\\pythonProject\\exemplo-utf8.bib')
