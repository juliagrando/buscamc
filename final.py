print('Digite o numero de canibais e missionarios:')
n = input(); #leitura do numero, ele tambem eh usado para padronizar os operadores

#classe Operador que serve tanto para os operadores quanto para o numero de missionarios e canibais em cada margem
class Operador:        
   def __init__(self, m = 0, c = 0):
      self.m = m
      self.c = c

   def __str__(self):
   	return "[%s, %s]" % (self.m, self.c)

   def __eq__(self, other):
    return (self.m == other.m and self.c == other.c)

   def getm(self):
      return self.m
   def getc(self):
      return self.c

#classe Estado representa os estados
class Estado:
   def __init__(self, m_esq = 0, m_dir = 0, barco = 'direita', caminho = []):
      self.m_esq = m_esq
      self.m_dir = m_dir
      self.barco = barco
      self.caminho = caminho

   def __getitem__(self, i):
     return self.caminho[i]

   def __str__(self):
      return "[%s, %s, %s, %s]" % (self.m_esq, self.barco, self.m_dir, self.caminho)

   def __eq__(self, other):
        return (self.m_esq == other.m_esq and self.m_dir == other.m_dir and self.barco == other.barco)

   def getM_esq(self):
      return self.m_esq
   def getM_dir(self):
      return self.m_dir
   def getBarco(self):
      return self.barco
   def getCaminho(self):
      return self.caminho


operadores = [] #lista de operadores que eh gerada no for abaixo

for o in xrange(0,n):
	for p in xrange(0,n):
         if p+o != 0:
            if o >= p and p+o<n or o == 0: #o numero de canibais nunca pode ser maior que missionarios 
               op = Operador(o,p)          #e a quantidade de pessoas no barco deve ser menor que o numero de missionarios e canibais
               operadores.append(op)

m_dir = Operador(n,n) #margem direita comeca com numero maximo de missionarios e canibais
m_esq = Operador()   # margem esquerda comeca vazia
estado_inicial = Estado(m_esq, m_dir, 'direita') #criacao do estado inicial

busca = [estado_inicial] #lista de busca, inicializada com o estado inicial
cam = [] #lista auxiliar que le os caminhos percorridos do estado

for lista in busca: #para cada elemento da lista

    mesq = lista.getM_esq(); #pega os valores da margem direita e esquerda
    mdir = lista.getM_dir();

    if mdir.getm() == 0 and mdir.getc() == 0: #caso os valores de missionarios e canibais da margem direita seja 0, acabou
                    print "TERMINOU"
                    print "CAMINHO FINAL:"
                    for c in lista:
                      print c
                    exit();

    for op in operadores: #realiza operacoes para cada operador da lista de operadores
      if lista.getBarco() == 'direita': #se o barco esta na direita
        barco = 'esquerda'; #vai para esquerda
        dm = mdir.getm() - op.getm(); #diminui valores da margem direita
        dc = mdir.getc() - op.getc();
        em = mesq.getm() + op.getm(); #soma na margem esquerda
        ec = mesq.getc() + op.getc();
      else:                 #se o barco esta na esquerda
        barco = 'direita';  #vai para direita
        dm = mdir.getm() + op.getm(); #soma na margem direita
        dc = mdir.getc() + op.getc();
        em = mesq.getm() - op.getm(); #diminui valores da margem esquerda
        ec = mesq.getc() - op.getc();

      if dm >=0 and dc >=0 and em >=0 and ec >=0:
        if dm >= dc and em >= ec or dm == 0 or em == 0:
          
          cam = lista.getCaminho(); #pega o caminho do no que esta sendo observado
          novo = Estado(Operador(em,ec), Operador(dm,dc), barco, cam + [op]); #cria um novo

          #if (novo in busca) == False: #caso queira fazer uma lista de fechados
          busca.append(novo) #busca em largura, coloca no final da lista               
          #busca.insert(busca.index(lista)+1, novo) #busca por profundidade, coloca no comeco da lista (logo apos o no que esta sendo observado)

