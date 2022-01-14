
#################################################################################################################################
#Inteiros
#Definição de Soma    
def parse_Soma(self, p):
    "Expressao : Expressao '+' Expressao"
    p[0] =  p[1] + p[3] + "add\n"

#Definição de Subtração 
def parse_Subtracao(self, p):
    "Expressao : Expressao '-' Expressao"
    p[0] =  p[1] + p[3] + "sub\n"

#Definição de Multiplicaçaõ 
def parse_Multiplicacao(self, p):
    "Expressao : Expressao '*' Expressao"
    p[0] =  p[1] + p[3] + "mul\n"

#Defenição de Divisão 
def parse_Divisao(self, p):
    "Expressao : Expressao '/' Expressao"
    p[0] =  p[1] + p[3] + "div\n"

#Definição de Módulo 
def parser_Modulo(self, p):
    "Expressao : Expressao '%' Expressao"
    p[0] =  p[1] + p[3] + "mod\n"




#Dois Float
#Definição de Soma 
def parse_Soma_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '+' ExpressaoFloat"
    p[0] =  p[1] + p[3] + "fadd\n"

#Definição de Subtração 
def parse_Subtracao_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '-' ExpressaoFloat"
    p[0] =  p[1] + p[3] + "fsub\n"

#Definição de Multiplicaçaõ 
def parse_Multiplicacao_FLoat(self, p):
    "ExpressaoFloat : ExpressaoFloat '*' ExpressaoFloat"
    p[0] =  p[1] + p[3] + "fmul\n"

#Defenição de Divisão 
def parse_Divisao_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '/' ExpressaoFloat"
    p[0] =  p[1] + p[3] + "fdiv\n"








#Um Int e um Float
#Definição de Soma 
def parse_Soma_Float(self, p):
    "ExpressaoFloat : Expressao '+' ExpressaoFloat"
    p[0] =  p[1] + 'itof\n' + p[3] + "fadd\n"

#Definição de Subtração 
def parse_Subtracao_Float(self, p):
    "ExpressaoFloat : Expressao '-' ExpressaoFloat"
    p[0] =  p[1] + 'itof\n' + p[3] + "fsub\n"

#Definição de Multiplicaçaõ 
def parse_Multiplicacao_FLoat(self, p):
    "ExpressaoFloat : Expressao '*' ExpressaoFloat"
    p[0] =  p[1] + 'itof\n' + p[3] + "fmul\n"

#Defenição de Divisão 
def parse_Divisao_Float(self, p):
    "ExpressaoFloat : Expressao '/' ExpressaoFloat"
    p[0] =  p[1] + 'itof\n' + p[3] + "fdiv\n"







#Um Float e um Int
#Definição de Soma 
def parse_Soma_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '+' Expressao"
    p[0] =  p[1] + p[3] + 'itof\n' + "fadd\n"

#Definição de Subtração 
def parse_Subtracao_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '-' Expressao"
    p[0] =  p[1] + p[3] + 'itof\n' + "fsub\n"

#Definição de Multiplicaçaõ 
def parse_Multiplicacao_FLoat(self, p):
    "ExpressaoFloat : ExpressaoFloat '*' Expressao"
    p[0] =  p[1] + p[3] + 'itof\n' + "fmul\n"

#Defenição de Divisão 
def parse_Divisao_Float(self, p):
    "ExpressaoFloat : ExpressaoFloat '/' Expressao"
    p[0] =  p[1] + p[3] + 'itof\n' + "fdiv\n"



#################################################################################################################################


#Definição de visualização de Variável
def parse_Valor_IntID(self, p):
    "Valor : VARINT"
    p[0] = rf"pushg {self.fp[p[1]][0]}\n"

def parse_Valor_FloatID(self, p):
    "ValorFloat : VARFLOAT"
    p[0] = rf"pushg {self.fp[p[1]][0]}\n"

def parse_Valor_ArrayID(self, p):
    "Valor : VARARRAY '[' Expressao ']'"
    p[0] = rf"pushgp\npushi {self.fp[p[1]][0]}\npadd\n{p[3]}loadn\n"

def parse_Valor_2DArrayID(self, p):
    "Valor : VARARRAY '[' Expressao ']' '[' Expressao ']'"
    p[0] = rf"pushgp\npushi {self.fp[p[1]][0]}\npadd\n{p[3]}pushi {self.fp[p[1]][2][1]}\nmul\n{p[6]}add\nloadn\n"



#Definição do Valor da Variável
#Valor de Int
def parse_Valor_Int(self, p):
        "Valor : INT"
        p[0] = rf"pushi {p[1]}\n"

#Valor de Float
def parse_Valor_FLOAT(self, p):
        "ValorFloat : FLOAT"
        p[0] = rf"pushf {p[1]}\n"

#Valor de uma String em Int
def parse_Valor_Str_to_Int(self, p):
    "Valor : INTR '('String')'"
    p[0] = rf"{p[3]}atoi\n"

#Valor de uma String em Float
def parse_Valor_str_to_Float(self, p):
    "ValorFloat : FLOATR '('String')'"
    p[0] = rf"{p[3]}atof\n"

#Valor de um Float em Int
def parse_Valor_float_to_int(self, p):
    "Valor : INTR '('ExpressaoFloat')'"
    p[0] = rf"{p[3]}ftoi\n"

#Valor de um Int em Float
def parse_Valor_int_to_float(self, p):
    "ValorFloat : FLOATR '('Expressao')'"
    p[0] = rf"{p[3]}itof\n"




#################################################################################################################################

#Definição de Expressão
def parse_ValorExpressao(self,p):
    "Expressao : Valor"
    p[0] = p[1]

def parse_ValorExpressao_Float(self,p):
    "ExpressaoFloat : ValorFloat"
    p[0] = p[1]

#Expressão entre parênteses 
def parse_Expressao_parenteses(self, p):
    "Expressao : '('Expressao')'"
    p[0] = p[2]

def parse_ExpressaoFloat_parenteses(self, p):
    "ExpressaoFloat : '('ExpressaoFloat')'"
    p[0] = p[2]





#################################################################################################################################
#Expressões Lógicas
#Expressões com Inteiros
def parse_Comparacoes_Igual(self, p):
    "ExpLogica : Expressao EQUAL Expressao"
    p[0] = p[1] + p[3] + "equal\n"

def parse_Comparacoes_Diferente(self, p):
    "ExpLogica : Expressao DIFF Expressao"
    p[0] = p[1] + p[3] + "equal\nnot\n"

def parse_Comparacoes_Maior(self, p):
    "ExpLogica : Expressao '>' Expressao"
    p[0] = p[1] + p[3] + "sup\n"

def parse_Comparacoes_Menor(self, p):
    "ExpLogica : Expressao '<' Expressao"
    p[0] = p[1] + p[3] + "inf\n"

def parse_Comparacoes_MaiorIgual(self, p):
    "ExpLogica : Expressao GEQUAL Expressao"
    p[0] = p[1] + p[3] + "supeq\n"

def parse_Comparacoes_MenorIgual(self, p):
    "ExpLogica : Expressao LEQUAL Expressao"
    p[0] = p[1] + p[3] + "infeq\n"




#Expressões com dois Floats
def parse_ComparacoesFloat_Igual(self, p):
    "ExpLogica : ExpressaoFloat EQUAL ExpressaoFloat"
    p[0] = p[1] + p[3] + "equal\n"

def parse_ComparacoesFloat_Diferente(self, p):
    "ExpLogica : ExpressaoFloat DIFF ExpressaoFloat"
    p[0] = p[1] + p[3] + "equal\nnot\n"

def parse_ComparacoesFloat_Maior(self, p):
    "ExpLogica : ExpressaoFloat '>' ExpressaoFloat"
    p[0] = p[1] + p[3] + "fsup\nftoi\n"

def parse_ComparacoesFloat_Menor(self, p):
    "ExpLogica : ExpressaoFloat '<' ExpressaoFloat"
    p[0] = p[1] + p[3] + "finf\nftoi\n"

def parse_ComparacoesFloat_MaiorIgual(self, p):
    "ExpLogica : ExpressaoFloat GEQUAL ExpressaoFloat"
    p[0] = p[1] + p[3] + "fsupeq\nftoi\n"

def parse_ComparacoesFLoat_MenorIgual(self, p):
    "ExpLogica : ExpressaoFloat LEQUAL ExpressaoFloat"
    p[0] = p[1] + p[3] + "finfeq\nftoi\n"



#Expressões com um Int e um Float
def parse_ComparacoesIntFLoat_Igual(self, p):
    "ExpLogica : Expressao EQUAL ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "equal\n"

def parse_ComparacoesFloat_Diferente(self, p):
    "ExpLogica : Expressao DIFF ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "equal\nnot\n"

def parse_ComparacoesFloat_Maior(self, p):
    "ExpLogica : Expressao '>' ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "fsup\nftoi\n"

def parse_ComparacoesFloat_Menor(self, p):
    "ExpLogica : Expressao '<' ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "finf\nftoi\n"

def parse_ComparacoesFloat_MaiorIgual(self, p):
    "ExpLogica : Expressao GEQUAL ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "fsupeq\nftoi\n"

def parse_ComparacoesFLoat_MenorIgual(self, p):
    "ExpLogica : Expressao LEQUAL ExpressaoFloat"
    p[0] = p[1] + "itof\n" + p[3] + "finfeq\nftoi\n"




#Expressões com um Float e um Int
def parse_ComparacoesFloat_Igual(self, p):
    "ExpLogica : ExpressaoFloat EQUAL Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "equal\n"

def parse_ComparacoesFloat_Diferente(self, p):
    "ExpLogica : ExpressaoFloat DIFF Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "equal\nnot\n"

def parse_ComparacoesFloat_Maior(self, p):
    "ExpLogica : ExpressaoFloat '>' Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "fsup\nftoi\n"

def parse_ComparacoesFloat_Menor(self, p):
    "ExpLogica : ExpressaoFloat '<' Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "finf\nftoi\n"

def parse_ComparacoesFloat_MaiorIgual(self, p):
    "ExpLogica : ExpressaoFloat GEQUAL Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "fsupeq\nftoi\n"

def parse_ComparacoesFLoat_MenorIgual(self, p):
    "ExpLogica : ExpressaoFloat LEQUAL Expressao"
    p[0] = p[1] + p[3] + "itof\n" + "finfeq\nftoi\n"

#################################################################################################################################

#Os valores das ExpLogica tomam valores de 0 ou 1
def parse_ExpLogica_Parenteses(self, p):
    "ExpLogica : '('ExpLogica')'"
    p[0] = p[2]

def parse_ExpLogica_And(self, p):
    "ExpLogica : ExpLogica AND ExpLogica"
    p[0] = p[1] + p[3] + "mul\n"

def parse_ExpLogica_Or(self, p):
    "ExpLogica : ExpLogica OR ExpLogica"
    p[0] = p[1] + p[3] + "add\n"

def parse_ExpLogica_Not(self, p):
    "ExpLogica : NOT ExpLogica"
    p[0] = p[2] + "not\n"