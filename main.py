import re
def analisa(txt):
    f = open(txt, encoding='utf-8')
    content = f.read()
    occ = {}
    padrao = '@[a-zA-Z]+{[a-zA-Z0-9:.-]+'

    for match in re.finditer(padrao, content):
        if re.split('{', match.group().title())[0] not in occ:
            occ[re.split('{', match.group().title())[0]] = 1
        else:
            occ[re.split('{', match.group().title())[0]] += 1
    tags={x:[] for x in occ}
    for match in re.finditer(padrao,content):
        tags[re.split('{', match.group().title())[0]].append(re.split('{', match.group().title())[1])
    print(tags)




    f.close()
    e = open('converte.html', 'w')
    e.write('<html>\n\t<body>\n\t\t<p>\n')
    for tag in occ:
        e.write('\t\t\t'+str(tag)+': '+str(occ[tag])+'<br>'+'\n')
        #e.write('\t\t\t\t'+str(tags[x for x in tags[x]])+'<br>'+)

    e.write('\t\t</p>\n\t</body>\n</html>')
    e.close()

detetaBloco = '@[a-zA-Z]+{[a-zA-Z0-9:.-]+,\n([\s]*[a-zA-Z]*[\s]*=[\s]*([{]|["])*[a-zA-Z0-9\s.:=\-,\'\(\)áãéõ]*([}]|["])+,?\n)+}'


def addbloco(bloco, info):
    padraoLinhas = '[a-zA-Z]*[\s]*=[\s]*([{]|["])*[a-zA-Z0-9\s.:=\-,\'\(\)áãéõ]*([}]|["])+,?'
    padraoTag = '@[a-zA-Z]+{[a-zA-Z0-9:.-]+'
    tag = re.search(padraoTag, bloco)
    match = str(re.split('{', tag.group())[0]).title()
    chave = str(re.split('{', tag.group())[1]).title()

    if match not in info:
        info[match] = {chave: {}}
    else:
        info[match][chave] = {}

    for linha in re.finditer(padraoLinhas, bloco):
        idlinha = re.split('=', linha.group().title())[0]
        idlinha = str(idlinha).strip()
        try:
            infoLinha = re.split('{', linha.group().title())[1]
            infoLinha = re.sub('\n',' ',str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha[:-2]
        except:
            infoLinha = re.split('"', linha.group().title())[1]
            infoLinha = re.sub('\n',' ',str(infoLinha))
            infoLinha = re.sub('[\s]', ' ', str(infoLinha))
            info[match][chave][idlinha] = infoLinha

    print(info)
    return info


bloco = "@inproceedings{oliveira09b,\
   title     = {Applying Program Comprehension Techniques to Karel Robot Programs},\
   author    = {Oliveira, Nuno and and Henriques, Pedro Rangel and\
            da Cruz, Daniela and Pereira, Maria João Varanda and\
            Mernik, Marjan and Kosar, Tomaz and Crepinsek, Matej},\
   booktitle = {Proceedings of the International Multiconference on Computer Science and Information Technology -- 2nd Workshop on Advances in Programming Languages (WAPL'2009)},\
   pages     = {697 --- 704},\
   publisher = {IEEE Computer Society Press},\
   address   = {Mragowo, Poland},\
   year      = {2009},\
   month     = \"October\",\
}',)'"
blocoq = "@inpRoceedings{oliveira09b2,\
   title     = {Applying Program Comprehension Techniques to Karel Robot Programs},\
   author    = {Oliveira, Nuno and and Henriques, Pedro Rangel and da Cruz, Daniela and Pereira, Maria João Varanda and Mernik, Marjan and Kosar, Tomaz and Crepinsek, Matej},\
   booktitle = {Proceedings of the International Multiconference on Computer Science and Information Technology -- 2nd Workshop on Advances in Programming Languages (WAPL'2009)},\
   pages     = {697 --- 704},\
   publisher = {IEEE Computer Society Press},\
   address   = {Mragowo, Poland},\
   year      = {2009},\
   month     = {October},\
}',)'"

example={}
addbloco(bloco,example)
addbloco(blocoq,example)





#analisa('exemplo-utf8.bib')
