
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

    for tag in info:
        for chave in info[tag]:
            for idx in info[tag][chave]:
                if idx == 'Author':
                    nospace=info[tag][chave][idx]
                    nospace=nospace.lstrip()
                    info[tag][chave][idx]=nospace
                    if info[tag][chave][idx][0] == '"' or info[tag][chave][idx][0]== '{' and not info[tag][chave][idx] == '{Projecto Camila}':
                        nochar=info[tag][chave][idx][1:]
                        nochar= nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if  info[tag][chave][idx][-1] ==',' or info[tag][chave][idx][-1] =='"' :
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if  info[tag][chave][idx][-1] ==',' or info[tag][chave][idx][-1] =='"' :
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
    for tag in info:
        for chave in info[tag]:
            for idx in info[tag][chave]:
                if idx == 'Title':
                    title=info[tag][chave][idx]
                    title=title.lstrip()
                    print(title)
                    if title.count('{')!=title.count('}'):
                        title=title[1:]
                        info[tag][chave][idx] = title
                    if title[0] == '"':
                        title = title[1:]
                        info[tag][chave][idx] = title
                    if  info[tag][chave][idx][-1] ==',' or info[tag][chave][idx][-1] =='"' :
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if  info[tag][chave][idx][-1] ==',' or info[tag][chave][idx][-1] =='"' :
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar




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