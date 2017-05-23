print('Digite o numero de canibais e missionarios:')
n = input(); #leitura do numero

#operadores fixos pois sempre cabem apenas 2 pessoas no barco
#[m,c]
operadores = []

for o in xrange(0,n):
    for p in xrange(0,n):
         if p+o != 0:
            if o >= p and p+o<n or o == 0:
                operadores.append([o,p])

barco = 'direita'; #barco comeca na direita
#[m,c]
m_esq = [0,0]; #margem esquerda comeca vazia
m_dir = [n,n]; #margem direita comeca com n missionarios e n canibais
#estado do sistema, [margem esquerda, posicao do barco, margem direita]
estado = [m_esq,barco,m_dir];
busca = [estado];
#print "O barco esta na margem", barco
#print "Na margem esquerda estao", estado[0][0], "missionarios e", estado[0][1], "canibais."
#print "Na margem direita estao", estado[2][0], "missionarios e", estado[2][1], "canibais.\n"

for lista in busca:
    print lista
    if lista[2][0] == 0 and lista[2][1] == 0:
                    print "TERMINOU", busca
                    exit();

    for op in operadores:
        if lista[1] == 'direita':
            dm = lista[2][0] - op[0];
            dc = lista[2][1] - op[1];
            em = lista[0][0] + op[0];
            ec = lista[0][1] + op[1];

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    barco = 'esquerda';
                    novo = [[em,ec], barco, [dm,dc]];
 
                if (novo in busca) == False:
                    busca.append(novo);
                    print busca

        else:
            dm = lista[2][0] + op[0];
            dc = lista[2][1] + op[1];
            em = lista[0][0] - op[0];
            ec = lista[0][1] - op[1];

            if dm >=0 and dc >=0 and em >=0 and ec >=0:
                if dm >= dc and em >= ec or dm == 0 or em == 0:
                    barco = 'direita';
                    novo = [[em,ec], barco, [dm,dc]];
                
                if (novo in busca) == False:
                    busca.append(novo);
                    print busca

                

