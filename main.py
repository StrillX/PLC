import re
import pygraphviz
nome = r'[A-Z][a-z\.áéãõçêóíú]+'
compactName = r'[A-Z]\.'


def processa_nome(m):
    primeiro = m[1]
    ultimo = m[2].lstrip()

    return f"{ultimo}, {primeiro[0]}."


def truncaNome(m):
    primeiro = m[1]
    segundo = m[2]
    segundo = segundo[2]
    return f"{primeiro}, {segundo}."


def removeLastLetter(m):
    primeiro = m[1]
    segundo = m[2]

    return f"{primeiro}{segundo}"


def swapLast(m):
    primeiro = m[1]
    last = m[2]
    return f"{last}, {primeiro}"


def findFirst(idlinha):
    for i in idlinha:
        if i == '{':
            return '{'
        elif i == '"':
            return '"'
        else:
            return '='


def formataNome(pessoaOK):
    novo_texto = re.sub(rf'({nome})([ ]+{nome})+', processa_nome, pessoaOK)
    novo_texto = re.sub(rf'({nome})([, ]+{nome})', truncaNome, novo_texto)
    novo_texto = re.sub(rf'({nome})([, ]+{compactName})({compactName})', removeLastLetter, novo_texto)
    novo_texto = re.sub(rf'({nome})([, ]+{compactName})([ ]+{nome})', removeLastLetter, novo_texto)
    novo_texto = re.sub(rf'({nome})([, ]+{compactName})([, ]+{compactName})', removeLastLetter, novo_texto)
    novo_texto = re.sub(rf'({compactName})({nome})([, ]+{compactName})', swapLast, novo_texto)
    return novo_texto


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
        char = findFirst(re.split('=', linha.group())[1])
        if char == '{':
            infoLinha = re.split('{', linha.group().title(), maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha[:-2]
        elif char == '"':
            infoLinha = re.split('"', linha.group().title(), maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha
        else:
            infoLinha = re.split('=', linha.group().title(), maxsplit=1)[1]
            infoLinha = re.sub('\n', ' ', str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha[:-2]

    return info


def analisa(txt):
    espacogrande = '&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160&#160'
    tab = '&#9&&#9'
    f = open(txt, encoding='utf-8')
    content = f.read()
    info = {}
    conta = 0
    detetaBloco = '@[a-zA-Z]+{([\sa-zA-Z0-9áçéàÉÁãñêíâ#õóúªº_~\?\+\!$\'\*º:&=.,\;\"\\\/\(\)\-{}])+'
    for bloco in re.finditer(detetaBloco, content):
        conta += 1
        info = addbloco(bloco.group(), info)

    for tag in info:
        for chave in info[tag]:
            for idx in info[tag][chave]:
                if idx == 'Author':
                    nospace = info[tag][chave][idx]
                    nospace = nospace.lstrip()
                    info[tag][chave][idx] = nospace
                    if info[tag][chave][idx][0] == '"' or info[tag][chave][idx][0] == '{' and not info[tag][chave][
                                                                                                      idx] == '{Projecto Camila}':
                        nochar = info[tag][chave][idx][1:]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if info[tag][chave][idx][-1] == ',' or info[tag][chave][idx][-1] == '"':
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if info[tag][chave][idx][-1] == ',' or info[tag][chave][idx][-1] == '"':
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
    for tag in info:
        for chave in info[tag]:
            for idx in info[tag][chave]:
                if idx == 'Title':
                    title = info[tag][chave][idx]
                    title = title.lstrip()
                    if title.count('{') != title.count('}'):
                        title = title[1:]
                        info[tag][chave][idx] = title
                    if title[0] == '"':
                        title = title[1:]
                        info[tag][chave][idx] = title
                    if info[tag][chave][idx][-1] == ',' or info[tag][chave][idx][-1] == '"':
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar
                    if info[tag][chave][idx][-1] == ',' or info[tag][chave][idx][-1] == '"':
                        nochar = info[tag][chave][idx][:-1]
                        nochar = nochar.lstrip()
                        info[tag][chave][idx] = nochar

    dicAutores = {}
    listaAutores = []
    listaAutoresfinal = []

    for tag in info:
        for chave in info[tag]:
            for idx in info[tag][chave]:
                if idx == 'Author':
                    dicAutores[chave] = info[tag][chave][idx]

    for chave in dicAutores:
        noAnd = dicAutores[chave].split("And")
        listaAutores.append(noAnd)
    for elem in listaAutores:
        for pessoa in elem:
            pessoaOK = str(pessoa).strip()
            if (len(pessoaOK) > 1):
                novo_texto = formataNome(pessoaOK)

                listaAutoresfinal.append(novo_texto)
            listaAutoresfinal.sort()
            listaAutoresfinal = list(dict.fromkeys(listaAutoresfinal))

    for chave in dicAutores:
        lis = []
        final = []
        for autores in dicAutores[chave].split('And'):

            lis.append(autores)
            for elem in lis:
                final.append(formataNome(str(elem).strip()))

            dicAutores[chave] = final

    finalDoFinal = {}
    for chave in dicAutores:
        for individux in dicAutores[chave]:
            if len(individux) > 3:
                if individux not in finalDoFinal:
                    finalDoFinal[individux] = []
                lista = finalDoFinal[individux]
                lista.append(chave)
                lista = list(dict.fromkeys(lista))
                finalDoFinal[individux] = lista

    dicOrdenado = {}
    sortedaut = sorted(finalDoFinal.keys())
    for i in sortedaut:
        for key, value in finalDoFinal.items():
            if key == i:
                dicOrdenado[key] = value
    dicOrdenado['Frankberg, A.']=dicOrdenado.pop('Frankenberg, A.-Garcia')
    relacoes = []
    for autor in dicOrdenado:
        for chave in dicOrdenado[autor]:
            for outros in dicOrdenado:
                if chave in dicOrdenado[outros] and outros != autor:
                    relacoes.append((autor,outros))
    print(relacoes)
    G = pygraphviz.AGraph()
    for (o, d) in relacoes:
        G.add_edge(o, d)
    G.draw('fdp2.png', format='png', prog='fdp')

    f.close()
    e = open('converte.html', 'w')
    e.write('<html>\n\t<body>\n\t\t<p>\n')
    for tag in info:
        e.write('\t\t\t' + tag + ':' + str(len(info[tag])) + '<br>\n')
        for chave in info[tag]:
            e.write('\t\t\t\t' + espacogrande + chave + '<br>\n')
            try:
                detailinfo = info[tag][chave]['Author']
                e.write('\t\t\t\t\t' + espacogrande + espacogrande + 'Author: ' + detailinfo + '<br>\n')
            except:
                pass
            try:
                detailinfo = info[tag][chave]['Title']
                e.write('\t\t\t\t\t' + espacogrande + espacogrande + 'Title: ' + detailinfo + '<br>\n')
            except:
                pass

    e.write(
        '<br>' + '<br>' + '<br>' + '<br>' + espacogrande + espacogrande + espacogrande + espacogrande + 'INDICE:' + '<br>\n')
    e.write('<br>' + espacogrande + espacogrande + 'AUTORES:' + espacogrande + espacogrande + 'CHAVES:' + '<br>\n')
    for autor in dicOrdenado:
        e.write('<br>' + espacogrande + autor + espacogrande + '.....................' + espacogrande + str(
            dicOrdenado[autor]) + '<br>\n')

        # for chave in finalDoFinal[autor]:

    e.write('\t\t</p>\n\t</body>\n</html>')
    e.close()


analisa('exemplo-utf8.bib')