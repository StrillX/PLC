import ply.yacc as yacc
from lexerPLC import Lexer

INT = 1
FLOAT = 2
ARRAY = 3
STRING = 4


class Parser:
    tokens = Lexer.tokens

    # Definição de um programa
    # Todas as Atribuições sempre no inicio do programa
    # Seguidas das Instruções
    def parse_Programa(self, p):
        "Programa : Atribuicoes Instrucoes"
        p[0] = p[1] + 'start' + '\n' + p[2] + 'stop' + '\n'

    # Definição de um progama sem Atribuições
    # Apenas Instruções
    def parse_Programa_NOATRIB(self, p):
        "Programa : Instrucoes"
        p[0] = 'start' + '\n' + p[1] + 'stop' + '\n'

    # Definição de um programa sem Instruções
    # Apenas Atribuições
    def parse_Programa_NOINST(self, p):
        "Programa : Atribuicoes"
        print('Não foram encontradas Instruções!')
        raise SyntaxError

    # Definição de um programa com erros
    def parse_Programa_ERROR(self, p):
        "Programa : ERROR"
        print('Erro!')
        raise SystemExit

    # Definição de um conjunto de Atribuições genéricas
    def parse_Atribuicoes(self, p):
        "Atribuicoes : Atribuicoes Atribuicao"
        p[0] = p[1] + p[2]

    # Definição de uma Atribuição singular
    def parse_Atribuicoes_Singular(self, p):
        "Atribuicoes : Atribuicao"
        p[0] = p[1]

    # Definição de uma atribuição vazia
    def parse_Atribuicoes_Vazia(self, p):
        "Atribuicoes : "
        p[0] = ''

    # Definição de um conjunto de Instrucoes genéricos
    def parse_Instrucoes(self, p):
        "Instrucoes : Instrucoes Instrucao"
        p[0] = p[1] + p[2]

    # Definição de uma Instrução singular
    def parse_Intrucoes_Singular(self, p):
        "Instrucoes : Instrucao"
        p[0] = p[1]

    # Definição de uma atribuição vazia
    def parse_Instrucoes_Vazia(self, p):
            "Instrucoes : "
            p[0] = ''

    #
    #   INTEIROS
    #

    #Atribuicao nao incializada de Inteiros
    def parse_Atribuicao_Int_NoInit(self,p):
        "Atribuicao : INTR AtribuicaoINT ';'"
        p[0] = p[2]

    #Atribuicao de Inteiros Singular
    def parse_Atribuicao_Int_Singular(self,p):
        "AtribuicaoINT : AtribuicaoINT"
        p[0] = p[1]

    # Atribuicao Multipla de Inteiros
    def parse_Atribuicao_Int_Multipla(self, p):
        "AtribuicaoINT : AtribuicaoINT ',' AtribuicaoINT"
        p[0] = p[1] + p[3]

    #Atribuicao inicializada de Inteiros
    def parse_Atribuicao_Int_Init(self,p):
        "AtribuicaoINT : ID '=' Expressao | ID"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack,INT)
            self.tamanho_stack += 1
        #Atribuição não incializada
        if len(p)<=2:
            'pushi 0\n'
        #Atribuição incializada
        else:
            p[0] = p[3]

    #
    #   FLOATS
    #

    # Atribuicao nao incializada de Floats
    def parse_Atribuicao_Float_NoInit(self, p):
        "Atribuicao : FLOATR AtribuicaoFLOAT ';'"
        p[0] = p[2]

    # Atribuicao de Floats Singular
    def parse_ATribuicao_Float_Singular(self, p):
        "AtribuicaoFLOAT : AtribuicaoFLOAT"
        p[0] = p[1]

    # Atribuicao Multipla de Floats
    def parse_ATribuicao_Float_Multipla(self, p):
        "AtribuicaoFLOAT : AtribuicaoFLOAT ',' AtribuicaoFLOAT"
        p[0] = p[1] + p[3]

    # Atribuicao inicializada de Floats
    def parse_Atribuicao_Float_Init(self, p):
        "AtribuicaoFLOAT : ID '=' Expressao | ID"
        if p[1] in self.var:
            # Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            # Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack, INT)
            self.tamanho_stack += 1
        # Atribuição não incializada
        if len(p) <= 2:
            'pushi 0.0\n'
        # Atribuição incializada
        else:
            p[0] = p[3]

    #
    #   STRINGS
    #

    # Atribuicao nao incializada de Strings
    def parse_Atribuicao_String_NoInit(self, p):
        "Atribuicao : STRR AtribuicaoSTRING ';'"
        p[0] = p[2]

    # Atribuicao de Strings Singular
    def parse_Atribuicaos_String_Singular(self, p):
        "AtribuicaoSTRING : AtribuicaoSTRING"
        p[0] = p[1]

    # Atribuicao Multipla de Strings
    def parse_Atribuicao_String_Multipla(self, p):
        "AtribuicaoSTRING : AtribuicaoSTRING ',' AtribuicaoSTRING"
        p[0] = p[1] + p[3]

    # Atribuicao inicializada de Strings
    def parse_Atribuicao_String(self, p):
        "AtribuicaoString : ID '=' String ';'"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adicionar variável à Stack
            self.fp[p[1]] = (self.tamanho_stack,STRING)
            self.tamanho_stack += 1

        p[0] = p[3]

    #
    #   ARRAYS
    #

    #Atribuicao nao incializada de um Array
    def parse_Atribuicao_Array(self,p):
        "Atribuicao : INTR ID '[' INT ']' ';'"
        if p[2] in self.var:
            #Já existe uma variável com o ID p[2]
            print(rf'A variável {p[2]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            self.var[p[2]] = (self.tamanho_stack,ARRAY,p[4])
            self.tamanho_stack += p[4]
        p[0] = f"pushn {p[4]}\n"

    #Atribuicao de Arrays Singular
    def parse_Atribuicao_Array_Singular(self,p):
        "Array : Array"
        p[0] = p[1]

    #Atribuicao Valorada de Arrays
    def parse_Atribuicao_Array_Valorada(self,p):
        "Array : '[' Elementos ']'"
        p[0] = p[2]

    #Definicao de Elementos
    def parse_Elementos(self,p):
        "Elementos : Elementos ',' INT"
        p[0] = p[1]
        p[0].append(p[3])

    #Definicao Singular de Elementos
    def parse_Elementos_Singular(self,p):
        "Elementos : INT"
        p[0] = p[1]

    #Definição de Matriz
    def parse_Atribuicao_Matriz(self,p):
        "Atribuicao : INTR ID '[' INT ']' '[' INT ']' ';'"
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack,ARRAY,(p[4],p[7]))
            self.tamanho_stack += p[4] * p[7]
        else:
            print(rf"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = rf"pushn {p[4]*p[7]}\n"

    #Definição de Matriz por Arrays
    def parse_Matriz(self,p):
        "Matriz : '[' Arrays ']'"
        p[0] = p[2]

    #Definição de Arrays
    def parse_Arrays(self,p):
        "Arrays : Arrays ',' Array"
        if len(p[3]) != len(p[1][0]):
            print(rf"Os arrays têm de ter dimensões iguais! Erro na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = p[1]
        p[0].append(p[3])

    #Definição de Atribuição de Array Valorado
    def parse_Atribuicao_Array_Valorado_TamanhoDET(self,p):
        "Atribuicao : INTR ID '[' INT ']' '=' Array ';'"
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack,ARRAY,p[4])
            self.tamanho_stack += p[4]
        else:
            print(rf"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        if len(p[7]) != len(p[4]):
            print(rf"Os arrays têm de ter dimensões iguais! Erro na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for inteiro in p[7]:
            p[0] += rf"pushi {inteiro}\n"
    #Definição de Atribuição de um Array Valorado sem tamanho definido
    def parse_Atribuicao_Array_Valorado_TamanhoNDET(self, p):
        "Atribuicao : INTR ID '[' Vazio ']' '=' Array ';'"

        p[4] = len(p[7])
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack, ARRAY, p[4])
            self.tamanho_stack += p[4]
        else:
            print(rf"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for inteiro in p[7]:
            p[0] += rf"pushi {inteiro}\n"

    #Definicão de Atribuição de uma Matriz Valorada
    def parse_Atribuiçao_Matriz_Valorada(self,p):
        "Atribuicao : INTR ID '[' Vazio ']' '=' Matriz ';'"
        p[4] = len(p[10])
        p[7] = len(p[10][0])

        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack, ARRAY,(p[4],p[7]))
            self.tamanho_stack += p[4]*p[7]
        else:
            print(rf"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for linha in p[10]:
            for inteiro in linha:
                p[0] += rf"pushi{inteiro}\n"

    #
    #   ERRO NAS ATRIBUIÇÕES
    #

    def parse_Atribuicao_ErroINT(self,p):
        "Atribuicao : INTR ERROR ';'"
        p[0] = ""
    def parse_Atribuicao_ErroFLOAT(self,p):
        "Atribuicao : FLOATR ERROR ';'"
        p[0] = ""
    def parse_Atribuicao_ErroSTRING(self,p):
        "Atribuicao : STRR ERROR ';'"
        p[0] = ""


    #
    #   INSTRUCOES
    #

    #Definição da Instrução Atualiza
    def parse_Instrucao_Atualiza(self,p):
        "Instrucao :Atualiza ';'"
        p[0] = p[1]

    #Definicao de Atualizar um Inteiro
    def parse_Atualiza(self,p):
        "Atualiza : VARINT '=' Expressao"
        p[0] = rf"{p[3]}storeg {self.var[p[1][0]]}\n"

    # Definicao de Atualizar um Float
    def parse_Atualiza_FLOAT(self, p):
        "Atualiza : VARFLOAT '=' ExpressaoFloat"
        p[0] = rf"{p[3]}storeg {self.var[p[1][0]]}\n"

    # Definicao de Atualizar uma String
    def parse_Atualiza_STRING(self, p):
        "Atualiza : VARSTRING '=' String"
        p[0] = rf"{p[3]}storeg {self.var[p[1][0]]}\n"

    #Definição Atualizacao ++
    def parse_Atualiza_PP(self,p):
        "Atualiza : VARINT PP"
        val = self.var[p[1]][0]
        p[0] = rf"pushg {val}\npushi 1\n add\nstoren {val}\n"

    # Definição Atualizacao --
    def parse_Atualiza_MM(self, p):
        "Atualiza : VARINT MM"
        val = self.var[p[1]][0]
        p[0] = rf"pushg {val}\npushi 1\n sub\nstoren {val}\n"

    # Definição Atualizacao ++
    def parse_Atualiza_PP_FLOAT(self, p):
        "Atualiza : VARFLOAT PP"
        val = self.var[p[1]][0]
        p[0] = rf"pushg {val}\npushi 1.0\n fadd\nstoreg {val}\n"

    # Definição Atualizacao --
    def parse_Atualiza_MM_FLOAT(self, p):
        "Atualiza : VARFLOAT MM"
        val = self.var[p[1]][0]
        p[0] = rf"pushg {val}\npushi 1.0\n fsub\nstoreg {val}\n"

    #Definição de Atualizacao de um elemento de um Array
    def parse_Atualiza_Elem_Array(self,p):
        "Atualiza : VARARRAY '[' Expressao ']' '=' Expressao"
        p[0] = rf"pushgp\npushi {self.var[p[1]][0]}\npadd\n{p[3]}{p[6]}\nstoren\n"

    # Definição de Atualizacao de um elemento de uma Matriz
    def parse_Atualiza_Elem_Matriz(self,p):
        "Atualiza : VARARRAY '[' Expressao ']' '[' Expressao ']' '=' Expressao"
        p[0] = rf"pushgp\npushi {self.var[p[1]][0]}\npadd\{p[3]}pushi{self.var[p[1]][2][1]}\nmul\n{p[6]}add\n{p[9]}ftoi\nstoren\n"

    #Conversao de Variaveis
    def parse_INT2FLOAT(self,p):
        "Atualiza : VARFLOAT '=' Expressao"
        p[0] = rf"{p[3]}ftoi\nstoreg {self.var[p[1]][0]}\n"

    def parse_FLOAT2INT(self, p):
        "Atualiza : VARINT '=' ExpressaoFloat"
        p[0] = rf"{p[3]}ftoi\nstoreg {self.var[p[1]][0]}\n"

    def parse_Instrucao_Print(self,p):
        "Instrucao : PRINT '(' Expressao ')' ';'"
        p[0] = p[3] + "writei\n"

    def parse_Instrucao_Print_ExpLogica(self,p):
        "Instrucao : PRINT '(' ExpLogica ')' ';'"
        p[0] = p[3] + "writei\n"
    def parse_Instrucao_Print_FLOAT(self,p):
        "Instrucao : PRINT '(' ExpressaoFloat ')' ';'"
        p[0] = p[3] + "writef\n"

    def parse_Instrucao_Print_String(self,p):
        "Instrucao : PRINT '(' String ')' ';'"
        p[0] = p[3] + "writes\n"

    def parse_Instrucao_PrintLN(self, p):
        "Instrucao : PRINTLN '(' Expressao ')' ';'"
        p[0] = p[3] + "writei\n" + "pushs \"\\n\"\nwrites\n"

    def parse_Instrucao_PrintLN_ExpLogica(self, p):
        "Instrucao : PRINT '(' ExpLogica ')' ';'"
        p[0] = p[3] + "writei\n" + "pushs \"\\n\"\nwrites\n"

    def parse_Instrucao_PrintLN_FLOAT(self, p):
        "Instrucao : PRINT '(' ExpressaoFloat ')' ';'"
        p[0] = p[3] + "writef\n" + "pushs \"\\n\"\nwrites\n"

    def parse_Instrucao_PrintLN_String(self, p):
        "Instrucao : PRINT '(' String ')' ';'"
        p[0] = p[3] + "writes\n" + "pushs \"\\n\"\nwrites\n"

    def parse_Instrucao_if(self,p):
        "Instrucao : IF Boolean '{' Instrucoes '}'"
        p[0] = p[2] + rf"jz l{self.ifs}\n" + p[4] + rf"l{self.ifs}:\n"
        self.ifs += 1

    def parse_Instrucao_if_else(self,p):
        "Instrucao : IF Boolean '{' Instrucoes '}' Else"
        p[0] = p[2] + rf"jz l{self.ifs}\n" + p[4] + rf"jump le{self.if_else}\n" + rf"l{self.ifs}:\n" + p[6]
        self.ifs +=1
        self.if_else += 1

    def parse_Instrucao_Else(self,p):
        "Else : ELSE '{' Intrucoes '}'"
        p[0] = p[3] + rf"le{self.if_else}"

    def parse_Instrucao_else_if(self,p):
        "Else : ELSE IF Boolean '{' Instrucoes '}' Else"
        p[0] = p[3] + rf"jz l {self.ifs}\n" + p[5] + rf"jump le{self.if_else}\n" + rf"l{self.ifs}:\n" + p[7]
        self.ifs += 1

    def parse_Instrucao_For(self,p):
        "Instrucao : FOR '(' Atualiza ';' Boolean ';' Atualiza ')' '{' Instrucoes '}'"
        p[0] = p[3] + rf"lc{self.ciclo}:\n" + p[5] + rf"jz lb{self.ciclo_fim}\n" + p[10] + p[7] + rf"jump lc{self.ciclo}\n" + rf"lb{self.ciclo_fim}:\n"
        self.ciclo += 1
        self.ciclo_fim += 1

    def parse_Instrucao_For_NOINIT(self,p):
        "Instrucao : FOR '(' Vazio ';' Boolean ';' Atualiza ')' '{' Instrucoes '}'"
        p[0] = "" + rf"lc{self.ciclo}:\n" + p[5] + rf"jz lb{self.ciclo_fim}\n" + p[10] + p[7] + rf"jump lc{self.ciclo}\n" + rf"lb{self.ciclo_fim}:\n"

    def  parse_Instrucao_While(self,p):
        "Instrucao : WHILE Boolean '{' Instrucoes '}'"
        p[0] = rf"lc{self.ciclo}:\n" + p[2] + rf"jz lb{self.ciclo_fim}\n" + p[4] + rf"jump lc{self.ciclo}" + rf"lb{self.ciclo_fim}:\n"
        self.ciclo += 1
        self.ciclo_fim += 1


    def parse_Boolean(self,p):
        "Boolean : Expressao"
        p[0] = p[1]

    def parse_Boolean_ExpLogica(self,p):
        "Boolean : ExpLogica"
        p[0] = p[1]

    def parse_String(self,p):
        "String : Texto"
        p[0] = rf"pushs \"" + p[1].strip('"') + "\"\n"

    def parse_String_VARSTRING(self,p):
        "String : VARSTRING"
        p[0] = rf"pushg {self.var[p[1]][0]}\n"

    def parse_String_Input(self,p):
        "String : INPUT '(' ')'"
        p[0] = rf"read\n"

    def parse_Vazio(self,p):
        "Vazio : "
        pass
    def parse_ERROR(self,p):
        print(rf"Erro de sintaxe na linha - {p.lineno}")

    #################################################################################################################################
    # Inteiros
    # Definição de Soma
    def parse_Soma(self, p):
        "Expressao : Expressao '+' Expressao"
        p[0] = p[1] + p[3] + "add\n"

    # Definição de Subtração
    def parse_Subtracao(self, p):
        "Expressao : Expressao '-' Expressao"
        p[0] = p[1] + p[3] + "sub\n"

    # Definição de Multiplicaçaõ
    def parse_Multiplicacao(self, p):
        "Expressao : Expressao '*' Expressao"
        p[0] = p[1] + p[3] + "mul\n"

    # Defenição de Divisão
    def parse_Divisao(self, p):
        "Expressao : Expressao '/' Expressao"
        p[0] = p[1] + p[3] + "div\n"

    # Definição de Módulo
    def parser_Modulo(self, p):
        "Expressao : Expressao '%' Expressao"
        p[0] = p[1] + p[3] + "mod\n"

    # Dois Float
    # Definição de Soma
    def parse_Soma_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '+' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fadd\n"

    # Definição de Subtração
    def parse_Subtracao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '-' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fsub\n"

    # Definição de Multiplicaçaõ
    def parse_Multiplicacao_FLoat(self, p):
        "ExpressaoFloat : ExpressaoFloat '*' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fmul\n"

    # Defenição de Divisão
    def parse_Divisao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '/' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fdiv\n"

    # Um Int e um Float
    # Definição de Soma
    def parse_Soma_Float(self, p):
        "ExpressaoFloat : Expressao '+' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fadd\n"

    # Definição de Subtração
    def parse_Subtracao_Float(self, p):
        "ExpressaoFloat : Expressao '-' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fsub\n"

    # Definição de Multiplicaçaõ
    def parse_Multiplicacao_FLoat(self, p):
        "ExpressaoFloat : Expressao '*' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fmul\n"

    # Defenição de Divisão
    def parse_Divisao_Float(self, p):
        "ExpressaoFloat : Expressao '/' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fdiv\n"

    # Um Float e um Int
    # Definição de Soma
    def parse_Soma_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '+' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fadd\n"

    # Definição de Subtração
    def parse_Subtracao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '-' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fsub\n"

    # Definição de Multiplicaçaõ
    def parse_Multiplicacao_FLoat(self, p):
        "ExpressaoFloat : ExpressaoFloat '*' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fmul\n"

    # Defenição de Divisão
    def parse_Divisao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '/' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fdiv\n"

    #################################################################################################################################

    # Definição de visualização de Variável
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

    # Definição do Valor da Variável
    # Valor de Int
    def parse_Valor_Int(self, p):
        "Valor : INT"
        p[0] = rf"pushi {p[1]}\n"

    # Valor de Float
    def parse_Valor_FLOAT(self, p):
        "ValorFloat : FLOAT"
        p[0] = rf"pushf {p[1]}\n"

    # Valor de uma String em Int
    def parse_Valor_Str_to_Int(self, p):
        "Valor : INTR '('String')'"
        p[0] = rf"{p[3]}atoi\n"

    # Valor de uma String em Float
    def parse_Valor_str_to_Float(self, p):
        "ValorFloat : FLOATR '('String')'"
        p[0] = rf"{p[3]}atof\n"

    # Valor de um Float em Int
    def parse_Valor_float_to_int(self, p):
        "Valor : INTR '('ExpressaoFloat')'"
        p[0] = rf"{p[3]}ftoi\n"

    # Valor de um Int em Float
    def parse_Valor_int_to_float(self, p):
        "ValorFloat : FLOATR '('Expressao')'"
        p[0] = rf"{p[3]}itof\n"

    #################################################################################################################################

    # Definição de Expressão
    def parse_ValorExpressao(self, p):
        "Expressao : Valor"
        p[0] = p[1]

    def parse_ValorExpressao_Float(self, p):
        "ExpressaoFloat : ValorFloat"
        p[0] = p[1]

    # Expressão entre parênteses
    def parse_Expressao_parenteses(self, p):
        "Expressao : '('Expressao')'"
        p[0] = p[2]

    def parse_ExpressaoFloat_parenteses(self, p):
        "ExpressaoFloat : '('ExpressaoFloat')'"
        p[0] = p[2]

    #################################################################################################################################
    # Expressões Lógicas
    # Expressões com Inteiros
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

    # Expressões com dois Floats
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

    # Expressões com um Int e um Float
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

    # Expressões com um Float e um Int
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

    # Os valores das ExpLogica tomam valores de 0 ou 1
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

    def build(self, **kwargs):
        self.var = dict()
        self.tamanho_stack = 0
        self.lexer = Lexer(self.var)
        self.lexer.build()
        self.parser = yacc.yacc(module=self, **kwargs)
        self.ifs = 0
        self.if_else = 0
        self.ciclo = 0
        self.ciclo_fim = 0