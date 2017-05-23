print('Digite o numero de canibais e missionarios:')
n = input(); #leitura do numero


class Operador:        
   def __init__(self, m = 0, c = 0):
      self.m = m
      self.c = c

   def __str__(self):
   	return "[%s, %s]" % (self.m, self.c)

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

   def __str__(self):
      return "[%s, %s, %s, %s]" % (self.m_esq, self.barco, self.m_dir, self.caminho)

   def getM_esq(self):
      return self.m_esq
   def getM_dir(self):
      return self.m_dir
   def getBarco(self):
      return self.barco
   def getCaminho(self):
      return self.caminho


operadores = []
print operadores

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

for lista in busca:
    print lista

    mesq = lista.getM_esq();
    mdir = lista.getM_dir();

    print mesq, mdir

    if mdir.getm() == 0 and mdir.getc() == 0:
                    print "TERMINOU", busca
                    exit();

    for op in operadores:
        cam = op
        print cam
        print lista.getBarco()
        if lista.getBarco() == 'direita':
            dm = mdir.getm() - op.getm();
            dc = mdir.getc() - op.getc();
            em = mesq.getm() + op.getm();
            ec = mesq.getc() + op.getc();

            print dm, dc, em, ec
            print lista.getCaminho();

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    caminhof = lista.getCaminho();
                    print caminhof
                    caminhof.append(cam)
                    print caminhof

                    barco = 'esquerda';
                    novo = [Operador(em,ec), Operador(dm,dc), barco, caminhof];
 
                if (novo in busca) == False:
                    busca.append(novo);
                    print busca

        else:
            dm = mdir.getm() + op.getm();
            dc = mdir.getc() + op.getc();
            em = mesq.getm() - op.getm();
            ec = mesq.getc() - op.getc();

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    caminhof = lista.getCaminho();
                    caminhof.append(cam)
                    barco = 'direita';
                    novo = [Operador(em,ec), Operador(dm,dc), barco, caminhof];
                
                if (novo in busca) == False:
                    busca.append(novo);
                    print busca

