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
    def p_Programa(self, p):
        "Programa : Atribuicoes Instrucoes"
        p[0] = p[1] + 'start' + '\n' + p[2] + '\nstop' + '\n'

    # Definição de um progama sem Atribuições
    # Apenas Instruções
    def p_Programa_NOATRIB(self, p):
        "Programa : Instrucoes"
        p[0] = 'start' + '\n' + p[1] + '\nstop' + '\n'

    # Definição de um programa sem Instruções
    # Apenas Atribuições
    def p_Programa_NOINST(self, p):
        "Programa : Atribuicoes"
        print('Não foram encontradas Instruções!')
        raise SyntaxError

    # Definição de um programa com erros
    def p_Programa_ERROR(self, p):
        "Programa : error"
        print('E aprenderes a programar?!')
        raise SystemExit

    # Definição de um conjunto de Atribuições genéricas
    def p_Atribuicoes(self, p):
        "Atribuicoes : Atribuicoes Atribuicao"
        p[0] = p[1] + p[2]

    # Definição de uma Atribuição singular
    def p_Atribuicoes_Singular(self, p):
        "Atribuicoes : Atribuicao"
        p[0] = p[1]



    # Definição de um conjunto de Instrucoes genéricos
    def p_Instrucoes(self, p):
        "Instrucoes : Instrucoes Instrucao"
        p[0] = p[1] + p[2]

    # Definição de uma Instrução singular
    def p_Intrucoes_Singular(self, p):
        "Instrucoes : Instrucao"
        p[0] = p[1]



    #
    #   INTEIROS
    #

    #Atribuicao nao incializada de Inteiros
    def p_Atribuicao_Int_NoInit(self,p):
        "Atribuicao : INTR AtribuicoesINT ';'"
        p[0] = p[2]

    #Atribuicao de Inteiros Singular
    def p_Atribuicao_Int_Singular(self,p):
        "AtribuicoesINT : AtribuicaoINT"
        p[0] = p[1]

    # Atribuicao Multipla de Inteiros
    def p_Atribuicao_Int_Multipla(self, p):
        "AtribuicoesINT : AtribuicoesINT ',' AtribuicaoINT"
        p[0] = p[1] + p[3]

    #Atribuicao inicializada de Inteiros
    def p_Atribuicao_Int_Init(self,p):
        "AtribuicaoINT : ID '=' Expressao"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack,INT)
            self.tamanho_stack += 1

        #Atribuição incializada

        p[0] = p[3]


    def p_Atribuicao_Int_NOINIT(self,p):
        "AtribuicaoINT : ID"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack,INT)
            self.tamanho_stack += 1
        p[0] = 'pushi 0\n'

    #
    #   FLOATS
    #

    # Atribuicao nao incializada de Floats
    def p_Atribuicao_Float_NoInit(self, p):
        "Atribuicao : FLOATR AtribuicoesFLOAT ';'"
        p[0] = p[2]

    # Atribuicao de Floats Singular
    def p_Atribuicao_Float_Singular(self, p):
        "AtribuicoesFLOAT : AtribuicaoFLOAT"
        p[0] = p[1]

    # Atribuicao Multipla de Floats
    def p_Atribuicao_Float_Multipla(self, p):
        "AtribuicoesFLOAT : AtribuicoesFLOAT ',' AtribuicaoFLOAT"
        p[0] = p[1] + p[3]

    # Atribuicao inicializada de Floats
    def p_Atribuicao_Float_Init(self, p):
        "AtribuicaoFLOAT : ID '=' Expressao"
        if p[1] in self.var:
            # Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            # Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack, INT)
            self.tamanho_stack += 1

        # Atribuição incializada

        p[0] = p[3]

    def p_Atribuicao_Float_NOINIT(self,p):
        "AtribuicaoFLOAT : ID"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adiconar variável à Stack
            self.var[p[1]] = (self.tamanho_stack,INT)
            self.tamanho_stack += 1
        'pushi 0.0\n'

    #
    #   STRINGS
    #

    # Atribuicao nao incializada de Strings
    def p_Atribuicao_String_NoInit(self, p):
        "Atribuicao : STRR AtribuicoesSTRING ';'"
        p[0] = p[2]

    # Atribuicao de Strings Singular
    def p_Atribuicaos_String_Singular(self, p):
        "AtribuicoesSTRING : AtribuicaoSTRING"
        p[0] = p[1]

    # Atribuicao Multipla de Strings
    def p_Atribuicao_String_Multipla(self, p):
        "AtribuicoesSTRING : AtribuicoesSTRING ',' AtribuicaoSTRING"
        p[0] = p[1] + p[3]

    # Atribuicao inicializada de Strings
    def p_Atribuicao_String(self, p):
        "AtribuicaoSTRING : ID '=' String ';'"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.lineno} já existe!')
            raise SyntaxError
        else:
            #Adicionar variável à Stack
            self.var[p[1]] = (self.tamanho_stack,STRING)
            self.tamanho_stack += 1

        p[0] = p[3]

    #
    #   ARRAYS
    #

    #Atribuicao nao incializada de um Array
    def p_Atribuicao_Array(self,p):
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
    def p_Atribuicao_Array_Singular(self,p):
        "Arrays : Array"
        p[0] = p[1]

    #Atribuicao Valorada de Arrays
    def p_Atribuicao_Array_Valorada(self,p):
        "Array : '[' Elementos ']'"
        p[0] = p[2]

    #Definicao de Elementos
    def p_Elementos(self,p):
        "Elementos : Elementos ',' INT"
        p[0] = p[1]
        p[0].append(p[3])

    #Definicao Singular de Elementos
    def p_Elementos_Singular(self,p):
        "Elementos : INT"
        p[0] = p[1]

    #Definição de Matriz
    def p_Atribuicao_Matriz(self,p):
        "Atribuicao : INTR ID '[' INT ']' '[' INT ']' ';'"
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack,ARRAY,(p[4],p[7]))
            self.tamanho_stack += p[4] * p[7]
        else:
            print(f"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = f"pushn {p[4]*p[7]}\n"

    #Definição de Matriz por Arrays
    def p_Matriz(self,p):
        "Matriz : '[' Arrays ']'"
        p[0] = p[2]

    #Definição de Arrays
    def p_Arrays(self,p):
        "Arrays : Arrays ',' Array"
        if len(p[3]) != len(p[1][0]):
            print(f"Os arrays têm de ter dimensões iguais! Erro na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = p[1]
        p[0].append(p[3])

    #Definição de Atribuição de Array Valorado
    def p_Atribuicao_Array_Valorado_TamanhoDET(self,p):
        "Atribuicao : INTR ID '[' INT ']' '=' Array ';'"
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack,ARRAY,p[4])
            self.tamanho_stack += p[4]
        else:
            print(f"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        if len(p[7]) != len(p[4]):
            print(f"Os arrays têm de ter dimensões iguais! Erro na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for inteiro in p[7]:
            p[0] += f"pushi {inteiro}\n"
    #Definição de Atribuição de um Array Valorado sem tamanho definido
    def p_Atribuicao_Array_Valorado_TamanhoNDET(self, p):
        "Atribuicao : INTR ID '[' Vazio ']' '=' Array ';'"

        p[4] = len(p[7])
        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack, ARRAY, p[4])
            self.tamanho_stack += p[4]
        else:
            print(f"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for inteiro in p[7]:
            p[0] += f"pushi {inteiro}\n"

    #Definicão de Atribuição de uma Matriz Valorada
    def p_Atribuicao_Matriz_Valorada(self,p):
        "Atribuicao : INTR ID '[' Vazio ']' '=' Matriz ';'"
        p[4] = len(p[10])
        p[7] = len(p[10][0])

        if p[2] not in self.var:
            self.var[p[2]] = (self.tamanho_stack, ARRAY,(p[4],p[7]))
            self.tamanho_stack += p[4]*p[7]
        else:
            print(f"A variável {p[2]} foi já foi declarada na linha {p.lineno(2)}")
            raise SyntaxError
        p[0] = ""
        for linha in p[10]:
            for inteiro in linha:
                p[0] += f"pushi{inteiro}\n"

    #
    #   ERRO NAS ATRIBUIÇÕES
    #

    def p_Atribuicao_ErroINT(self,p):
        "Atribuicao : INTR error ';'"
        p[0] = ""
    def p_Atribuicao_ErroFLOAT(self,p):
        "Atribuicao : FLOATR error ';'"
        p[0] = ""
    def p_Atribuicao_ErroSTRING(self,p):
        "Atribuicao : STRR error ';'"
        p[0] = ""


    #
    #   INSTRUCOES
    #

    #Definição da Instrução Atualiza
    def p_Instrucao_Atualiza(self,p):
        "Instrucao : Atualiza ';'"
        p[0] = p[1]

    #Definicao de Atualizar um Inteiro
    def p_Atualiza(self,p):
        "Atualiza : VARINT '=' Expressao"
        p[0] = f"{p[3]}storeg {self.var[p[1]][0]}\n"

    # Definicao de Atualizar um Float
    def p_Atualiza_FLOAT(self, p):
        "Atualiza : VARFLOAT '=' ExpressaoFloat"
        p[0] = f"{p[3]}storeg {self.var[p[1][0]]}\n"

    # Definicao de Atualizar uma String
    def p_Atualiza_STRING(self, p):
        "Atualiza : VARSTRING '=' String"
        p[0] = f"{p[3]}storeg {self.var[p[1][0]]}\n"

    #Definição Atualizacao ++
    def p_Atualiza_PP(self,p):
        "Atualiza : VARINT PP"
        val = self.var[p[1]][0]
        p[0] = f"pushg {val}\npushi 1\nadd\nstoreg {val}\n"

    # Definição Atualizacao --
    def p_Atualiza_MM(self, p):
        "Atualiza : VARINT MM"
        val = self.var[p[1]][0]
        p[0] = f"pushg {val}\npushi 1\n sub\nstoreg {val}\n"

    # Definição Atualizacao ++
    def p_Atualiza_PP_FLOAT(self, p):
        "Atualiza : VARFLOAT PP"
        val = self.var[p[1]][0]
        p[0] = f"pushg {val}\npushi 1.0\n fadd\nstoreg {val}\n"

    # Definição Atualizacao --
    def p_Atualiza_MM_FLOAT(self, p):
        "Atualiza : VARFLOAT MM"
        val = self.var[p[1]][0]
        p[0] = f"pushg {val}\npushi 1.0\n fsub\nstoreg {val}\n"

    #Definição de Atualizacao de um elemento de um Array
    def p_Atualiza_Elem_Array(self,p):
        "Atualiza : VARARRAY '[' Expressao ']' '=' Expressao"
        p[0] = f"pushgp\npushi {self.var[p[1]][0]}\npadd\n{p[3]}{p[6]}\nstoren\n"

    # Definição de Atualizacao de um elemento de uma Matriz
    def p_Atualiza_Elem_Matriz(self,p):
        "Atualiza : VARARRAY '[' Expressao ']' '[' Expressao ']' '=' Expressao"
        p[0] = f"pushgp\npushi {self.var[p[1]][0]}\npadd\{p[3]}pushi{self.var[p[1]][2][1]}\nmul\n{p[6]}add\n{p[9]}ftoi\nstoreg\n"

    #Conversao de Variaveis
    def p_INT2FLOAT(self,p):
        "Atualiza : VARFLOAT '=' Expressao"
        p[0] = f"{p[3]}ftoi\nstoreg {self.var[p[1]][0]}\n"

    def p_FLOAT2INT(self, p):
        "Atualiza : VARINT '=' ExpressaoFloat"
        p[0] = f"{p[3]}ftoi\nstoreg {self.var[p[1]][0]}\n"

    def p_Instrucao_Print(self,p):
        "Instrucao : PRINT '(' Expressao ')' ';'"
        p[0] = p[3] + "writei\n"

    def p_Instrucao_Print_ExpLogica(self,p):
        "Instrucao : PRINT '(' ExpLogica ')' ';'"
        p[0] = p[3] + "writei\n"
    def p_Instrucao_Print_FLOAT(self,p):
        "Instrucao : PRINT '(' ExpressaoFloat ')' ';'"
        p[0] = p[3] + "writef\n"

    def p_Instrucao_Print_String(self,p):
        "Instrucao : PRINT '(' String ')' ';'"
        p[0] = p[3] + "writes\n"



    def p_Instrucao_PrintLN(self, p):
        "Instrucao : PRINTLN '(' Expressao ')' ';'"
        p[0] = p[3] + "writei\n" + "pushs \"\\n\"\nwrites\n"

    def p_Instrucao_PrintLN_ExpLogica(self, p):
        "Instrucao : PRINTLN '(' ExpLogica ')' ';'"
        p[0] = p[3] + "writei\n" + "pushs \"\\n\"\nwrites\n"

    def p_Instrucao_PrintLN_FLOAT(self, p):
        "Instrucao : PRINTLN '(' ExpressaoFloat ')' ';'"
        p[0] = p[3] + "writef\n" + "pushs \"\\n\"\nwrites\n"

    def p_Instrucao_PrintLN_String(self, p):
        "Instrucao : PRINTLN '(' String ')' ';'"
        p[0] = p[3] + "writes\n" + "pushs \"\\n\"\nwrites\n"

    def p_Instrucao_if(self,p):
        "Instrucao : IF Boolean '{' Instrucoes '}'"
        p[0] = p[2] + f"jz l{self.ifs}\n" + p[4] + f"l{self.ifs}:\n"
        self.ifs += 1

    def p_Instrucao_if_else(self,p):
        "Instrucao : IF Boolean '{' Instrucoes '}' Else"
        p[0] = p[2] + f"jz l{self.ifs}\n" + p[4] + f"jump le{self.if_else}\n" + f"l{self.ifs}:\n" + p[6]
        self.ifs +=1
        self.if_else += 1

    def p_Instrucao_Else(self,p):
        "Else : ELSE '{' Instrucoes '}'"
        p[0] = p[3] + f"le{self.if_else}:\n"

    def p_Instrucao_else_if(self,p):
        "Else : ELSE IF Boolean '{' Instrucoes '}' Else"
        p[0] = p[3] + f"jz l{self.ifs}\n" + p[5] + f"l{self.ifs}\n" + f"le{self.if_else}:\n"
        self.ifs += 1

    def p_Instrucao_For(self,p):
        "Instrucao : FOR '(' Atualiza ';' Boolean ';' Atualiza ')' '{' Instrucoes '}'"
        p[0] = p[3] + f"lc{self.ciclo}:\n" + p[5] + f"jz lb{self.ciclo_fim}\n" + p[10] + p[7] + f"jump lc{self.ciclo}\n" + f"lb{self.ciclo_fim}:\n"
        self.ciclo += 1
        self.ciclo_fim += 1

    def p_Instrucao_For_NOINIT(self,p):
        "Instrucao : FOR '(' Vazio ';' Boolean ';' Atualiza ')' '{' Instrucoes '}'"
        p[0] = "" + f"lc{self.ciclo}:\n" + p[5] + f"jz lb{self.ciclo_fim}\n" + p[10] + p[7] + f"jump lc{self.ciclo}\n" + f"lb{self.ciclo_fim}:\n"

    def  p_Instrucao_While(self,p):
        "Instrucao : WHILE Boolean '{' Instrucoes '}'"
        p[0] = f"lc{self.ciclo}:\n" + p[2] + f"jz lb{self.ciclo_fim}\n" + p[4] + f"jump lc{self.ciclo}\n" + f"lb{self.ciclo_fim}:\n"
        self.ciclo += 1
        self.ciclo_fim += 1


    def p_Boolean(self,p):
        "Boolean : Expressao"
        p[0] = p[1]

    def p_Boolean_ExpLogica(self,p):
        "Boolean : ExpLogica"
        p[0] = p[1]

    def p_String(self,p):
        "String : LINHA"
        p[0] = f"pushs \"" + p[1].strip('"') + "\"\n"

    def p_String_VARSTRING(self,p):
        "String : VARSTRING"
        p[0] = f"pushg {self.var[p[1]][0]}\n"

    def p_String_Input(self,p):
        "String : INPUT '(' ')'"
        p[0] = f"read\n"

    def p_Vazio(self,p):
        "Vazio : "
        pass
    def p_error(self,p):
        print(f"Isto tá mal men, olha a linha -> {p.lineno-1}")

    #################################################################################################################################
    # Inteiros
    # Definição de Soma
    def p_Soma(self, p):
        "Expressao : Expressao '+' Expressao"
        p[0] = p[1] + p[3] + "add\n"

    # Definição de Subtração
    def p_Subtracao(self, p):
        "Expressao : Expressao '-' Expressao"
        p[0] = p[1] + p[3] + "sub\n"

    # Definição de Multiplicaçaõ
    def p_Multiplicacao(self, p):
        "Expressao : Expressao '*' Expressao"
        p[0] = p[1] + p[3] + "mul\n"

    # Defenição de Divisão
    def p_Divisao(self, p):
        "Expressao : Expressao '/' Expressao"
        p[0] = p[1] + p[3] + "div\n"

    # Definição de Módulo
    def p_Modulo(self, p):
        "Expressao : Expressao '%' Expressao"
        p[0] = p[1] + p[3] + "mod\n"

    # Dois Float
    # Definição de Soma
    def p_Soma_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '+' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fadd\n"

    # Definição de Subtração
    def p_Subtracao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '-' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fsub\n"

    # Definição de Multiplicaçaõ
    def p_Multiplicacao_FLoat(self, p):
        "ExpressaoFloat : ExpressaoFloat '*' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fmul\n"

    # Defenição de Divisão
    def p_Divisao_Float(self, p):
        "ExpressaoFloat : ExpressaoFloat '/' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fdiv\n"

    # Um Int e um Float
    # Definição de Soma
    def p_Soma_Int_Float(self, p):
        "ExpressaoFloat : Expressao '+' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fadd\n"

    # Definição de Subtração
    def p_Subtracao_Int_Float(self, p):
        "ExpressaoFloat : Expressao '-' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fsub\n"

    # Definição de Multiplicaçaõ
    def p_Multiplicacao_Int_FLoat(self, p):
        "ExpressaoFloat : Expressao '*' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fmul\n"

    # Defenição de Divisão
    def p_Divisao_Int_Float(self, p):
        "ExpressaoFloat : Expressao '/' ExpressaoFloat"
        p[0] = p[1] + 'itof\n' + p[3] + "fdiv\n"

    # Um Float e um Int
    # Definição de Soma
    def p_Soma_Float_Int(self, p):
        "ExpressaoFloat : ExpressaoFloat '+' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fadd\n"

    # Definição de Subtração
    def p_Subtracao_Float_Int(self, p):
        "ExpressaoFloat : ExpressaoFloat '-' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fsub\n"

    # Definição de Multiplicaçaõ
    def p_Multiplicacao_FLoat_Int(self, p):
        "ExpressaoFloat : ExpressaoFloat '*' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fmul\n"

    # Defenição de Divisão
    def p_Divisao_Float_Int(self, p):
        "ExpressaoFloat : ExpressaoFloat '/' Expressao"
        p[0] = p[1] + p[3] + 'itof\n' + "fdiv\n"

    #################################################################################################################################

    # Definição de visualização de Variável
    def p_Valor_IntID(self, p):
        "Valor : VARINT"
        p[0] = f"pushg {self.var[p[1]][0]}\n"

    def p_Valor_FloatID(self, p):
        "ValorFloat : VARFLOAT"
        p[0] = f"pushg {self.var[p[1]][0]}\n"

    def p_Valor_ArrayID(self, p):
        "Valor : VARARRAY '[' Expressao ']'"
        p[0] = f"pushgp\npushi {self.var[p[1]][0]}\npadd\n{p[3]}loadn\n"

    def p_Valor_2DArrayID(self, p):
        "Valor : VARARRAY '[' Expressao ']' '[' Expressao ']'"
        p[0] = f"pushgp\npushi {self.var[p[1]][0]}\npadd\n{p[3]}pushi {self.var[p[1]][2][1]}\nmul\n{p[6]}add\nloadn\n"

    # Definição do Valor da Variável
    # Valor de Int
    def p_Valor_Int(self, p):
        "Valor : INT"
        p[0] = f"pushi {p[1]}\n"

    # Valor de Float
    def p_Valor_FLOAT(self, p):
        "ValorFloat : FLOAT"
        p[0] = f"pushf {p[1]}\n"

    # Valor de uma String em Int
    def p_Valor_Str_to_Int(self, p):
        "Valor : INTR '(' String ')'"
        p[0] = f"{p[3]}atoi\n"

    # Valor de uma String em Float
    def p_Valor_str_to_Float(self, p):
        "ValorFloat : FLOATR '(' String ')'"
        p[0] = f"{p[3]}atof\n"

    # Valor de um Float em Int
    def p_Valor_float_to_int(self, p):
        "Valor : INTR '(' ExpressaoFloat ')'"
        p[0] = f"{p[3]}ftoi\n"

    # Valor de um Int em Float
    def p_Valor_int_to_float(self, p):
        "ValorFloat : FLOATR '(' Expressao ')'"
        p[0] = f"{p[3]}itof\n"

    #################################################################################################################################

    # Definição de Expressão
    def p_ValorExpressao(self, p):
        "Expressao : Valor"
        p[0] = p[1]

    def p_ValorExpressao_Float(self, p):
        "ExpressaoFloat : ValorFloat"
        p[0] = p[1]

    # Expressão entre parênteses
    def p_Expressao_parenteses(self, p):
        "Expressao : '(' Expressao ')'"
        p[0] = p[2]

    def p_ExpressaoFloat_parenteses(self, p):
        "ExpressaoFloat : '(' ExpressaoFloat ')'"
        p[0] = p[2]

    #################################################################################################################################
    # Expressões Lógicas
    # Expressões com Inteiros
    def p_Comparacoes_Igual(self, p):
        "ExpLogica : Expressao EQUAL Expressao"
        p[0] = p[1] + p[3] + "equal\n"

    def p_Comparacoes_Diferente(self, p):
        "ExpLogica : Expressao DIFF Expressao"
        p[0] = p[1] + p[3] + "equal\nnot\n"

    def p_Comparacoes_Maior(self, p):
        "ExpLogica : Expressao '>' Expressao"
        p[0] = p[1] + p[3] + "sup\n"

    def p_Comparacoes_Menor(self, p):
        "ExpLogica : Expressao '<' Expressao"
        p[0] = p[1] + p[3] + "inf\n"

    def p_Comparacoes_MaiorIgual(self, p):
        "ExpLogica : Expressao GEQUAL Expressao"
        p[0] = p[1] + p[3] + "supeq\n"

    def p_Comparacoes_MenorIgual(self, p):
        "ExpLogica : Expressao LEQUAL Expressao"
        p[0] = p[1] + p[3] + "infeq\n"

    # Expressões com dois Floats
    def p_ComparacoesFloat_Igual(self, p):
        "ExpLogica : ExpressaoFloat EQUAL ExpressaoFloat"
        p[0] = p[1] + p[3] + "equal\n"

    def p_ComparacoesFloat_Diferente(self, p):
        "ExpLogica : ExpressaoFloat DIFF ExpressaoFloat"
        p[0] = p[1] + p[3] + "equal\nnot\n"

    def p_ComparacoesFloat_Maior(self, p):
        "ExpLogica : ExpressaoFloat '>' ExpressaoFloat"
        p[0] = p[1] + p[3] + "fsup\nftoi\n"

    def p_ComparacoesFloat_Menor(self, p):
        "ExpLogica : ExpressaoFloat '<' ExpressaoFloat"
        p[0] = p[1] + p[3] + "finf\nftoi\n"

    def p_ComparacoesFloat_MaiorIgual(self, p):
        "ExpLogica : ExpressaoFloat GEQUAL ExpressaoFloat"
        p[0] = p[1] + p[3] + "fsupeq\nftoi\n"

    def p_ComparacoesFLoat_MenorIgual(self, p):
        "ExpLogica : ExpressaoFloat LEQUAL ExpressaoFloat"
        p[0] = p[1] + p[3] + "finfeq\nftoi\n"

    # Expressões com um Int e um Float
    def p_ComparacoesIntFLoat_Igual(self, p):
        "ExpLogica : Expressao EQUAL ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "equal\n"

    def p_ComparacoesInt_Float_Diferente(self, p):
        "ExpLogica : Expressao DIFF ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "equal\nnot\n"

    def p_ComparacoesInt_Float_Maior(self, p):
        "ExpLogica : Expressao '>' ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "fsup\nftoi\n"

    def p_ComparacoesInt_Float_Menor(self, p):
        "ExpLogica : Expressao '<' ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "finf\nftoi\n"

    def p_ComparacoesInt_Float_MaiorIgual(self, p):
        "ExpLogica : Expressao GEQUAL ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "fsupeq\nftoi\n"

    def p_ComparacoesInt_FLoat_MenorIgual(self, p):
        "ExpLogica : Expressao LEQUAL ExpressaoFloat"
        p[0] = p[1] + "itof\n" + p[3] + "finfeq\nftoi\n"

    # Expressões com um Float e um Int
    def p_ComparacoesFloat_Int_Igual(self, p):
        "ExpLogica : ExpressaoFloat EQUAL Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "equal\n"

    def p_ComparacoesFloat_Int_Diferente(self, p):
        "ExpLogica : ExpressaoFloat DIFF Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "equal\nnot\n"

    def p_ComparacoesFloat_Int_Maior(self, p):
        "ExpLogica : ExpressaoFloat '>' Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "fsup\nftoi\n"

    def p_ComparacoesFloat_Int_Menor(self, p):
        "ExpLogica : ExpressaoFloat '<' Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "finf\nftoi\n"

    def p_ComparacoesFloat_Int_MaiorIgual(self, p):
        "ExpLogica : ExpressaoFloat GEQUAL Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "fsupeq\nftoi\n"

    def p_ComparacoesFLoat_Int_MenorIgual(self, p):
        "ExpLogica : ExpressaoFloat LEQUAL Expressao"
        p[0] = p[1] + p[3] + "itof\n" + "finfeq\nftoi\n"

    #################################################################################################################################

    # Os valores das ExpLogica tomam valores de 0 ou 1
    def p_ExpLogica_Parenteses(self, p):
        "ExpLogica : '(' ExpLogica ')'"
        p[0] = p[2]

    def p_ExpLogica_And(self, p):
        "ExpLogica : ExpLogica AND ExpLogica"
        p[0] = p[1] + p[3] + "mul\n"

    def p_ExpLogica_Or(self, p):
        "ExpLogica : ExpLogica OR ExpLogica"
        p[0] = p[1] + p[3] + "add\n"

    def p_ExpLogica_Not(self, p):
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