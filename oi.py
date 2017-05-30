print('Digite o numero de canibais e missionarios:')
n = input(); #leitura do numero


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


operadores = []

for o in xrange(0,n):
	for p in xrange(0,n):
         if p+o != 0:
            if o >= p and p+o<n or o == 0:
               op = Operador(o,p)
               operadores.append(op)

m_dir = Operador(n,n) 
m_esq = Operador()   
estado_inicial = Estado(m_esq, m_dir, 'direita')

busca = [estado_inicial]
fechados = [Estado(m_esq, m_dir, 'direita', [])]

for lista in busca:
    #print lista

    mesq = lista.getM_esq();
    mdir = lista.getM_dir();

    if mdir.getm() == 0 and mdir.getc() == 0:
                    print "TERMINOU"
                    for b in busca:
                      print b

                    b = busca[-1]
                    print b
                    print "CAMINHO FINAL:"
                    for c in b:
                      print c
                    exit();

    for op in operadores:
        
        if lista.getBarco() == 'direita':
            dm = mdir.getm() - op.getm();
            dc = mdir.getc() - op.getc();
            em = mesq.getm() + op.getm();
            ec = mesq.getc() + op.getc();

            print em, ec, dm, dc

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    caminhof = lista.getCaminho();
                    caminhof.append(op)

                    barco = 'esquerda';
                    novo = Estado(Operador(em,ec), Operador(dm,dc), barco, caminhof);

                if (novo in busca) == False:
                    busca.append(novo)

        else:
            dm = mdir.getm() + op.getm();
            dc = mdir.getc() + op.getc();
            em = mesq.getm() - op.getm();
            ec = mesq.getc() - op.getc();

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    caminhof = lista.getCaminho();
                    caminhof.append(op)
                    barco = 'direita';
                    novo = Estado(Operador(em,ec), Operador(dm,dc), barco, caminhof);

                if (novo in busca) == False:
                    busca.append(novo);

