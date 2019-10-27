from Aresta import *

class ListaEncadeada:
    def __init__(self):
        self.aresta = None
        self.lista = None
        self.ponteiro = None
        self.ponteiro2 = None

    def vazia(self):
        if self.lista == None:
            return True
        return False


    def insere(self,index,valorAresta):

        aresta = Aresta()
        aresta.index = index
        aresta.valorAresta = valorAresta
        if self.vazia():

            self.lista = aresta

        else:
            self.ponteiro2 = self.lista
            self.ponteiro = self.lista
            while(self.ponteiro !=None):
                self.ponteiro2 = self.ponteiro
                self.ponteiro = self.ponteiro.prox
            self.ponteiro2.prox = aresta
    def printarLista(self):
        self.ponteiro = self.lista

        if self.ponteiro == None:
            pass
        else:
            while(self.ponteiro != None):

                print('[',self.ponteiro.index,',',self.ponteiro.valorAresta ,']',end='->')

                self.ponteiro = self.ponteiro.prox

    def atualizar(self, index):
        ponteiro = self.lista
        while True:
            if(index == ponteiro.index):
                ponteiro.valorAresta +=1
                break
            else:
                ponteiro = ponteiro.prox




