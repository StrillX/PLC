import re
def analisa(txt):
    f = open(txt, encoding='utf-8')
    content = f.read()
    occ = {}
    padrao = '@[a-zA-Z]+{[a-zA-Z0-9:.-]+'

    for match in re.finditer(padrao, content):
        if re.split('{', match.group())[0] not in occ:
            occ[re.split('{', match.group())[0]] = 1
        else:
            occ[re.split('{', match.group())[0]] += 1
    tags={x:[] for x in occ}
    for match in re.finditer(padrao,content):
        tags[re.split('{', match.group())[0]].append(re.split('{', match.group())[1])

    print(tags)




    f.close()
    e = open('converte.html', 'w')
    e.write('<html>\n\t<body>\n\t\t<p>\n')
    for tag in occ:
        e.write('\t\t\t'+str(tag)+': '+str(occ[tag])+'<br>'+'\n')

    e.write('\t\t</p>\n\t</body>\n</html>')
    e.close()

analisa('exemplo-utf8.bib')
