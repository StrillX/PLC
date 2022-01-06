import ply.yacc as yacc
from lexer import Lexer

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
        "Atribuicoes : Atribuicao Atribuicoes"
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
        "Instrucoes : Instrucao Instrucoes"
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
    def parse_ATribuicao_Int_Singular(self,p):
        "AtribuicaoINT : AtribuicaoINT"
        p[0] = p[1]

    # Atribuicao Multipla de Inteiros
    def parse_ATribuicao_Int_Multipla(self, p):
        "AtribuicaoINT : AtribuicaoINT ',' AtribuicaoINT"
        p[0] = p[1] + p[3]

    #Atribuicao inicializada de Inteiros
    def parse_Atribuicao_Int_Init(self,p):
        "AtribuicaoINT : ID '=' Expressao | ID"
        if p[1] in self.var:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.numline} já existe!')
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
            print(rf'A variável {p[1]} declarada na linha {p.numline} já existe!')
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
        if p[1] in self.fp:
            #Já existe uma variável com o ID p[1]
            print(rf'A variável {p[1]} declarada na linha {p.numLine} já existe!')
            raise SyntaxError
        else:
            #Adicionar variável à Stack
            self.fp[p[1]] = (self.stack_size,STRING)
            self.stack_size += 1

        p[0] = p[3]

    #
    #   ARRAYS
    #

    #Atribuicao nao incializada de um Array
    def parse_Atribuicao_Array(self,p):
        "Atribuicao : INTR ID '[' INT ']' ';'"
        if p[2] in self.fp:
            #Já existe uma variável com o ID p[2]
            print(rf'A variável {p[1]} declarada na linha {p.numLine} já existe!')
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

    #Definicao Singuar de Elementos
    def parse_Elementos_Singular(self,p):
        "Elementos : INT"
        p[0] = p[1]
    