print('Digite o numero de canibais e missionarios:')
n = input(); #leitura do numero

#operadores fixos pois sempre cabem apenas 2 pessoas no barco
#[m,c]
operadores = [[0,1],[1,0],[1,1],[2,0],[0,2]];
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
    for op in operadores:
        if lista[1] == 'direita':
            dm = lista[2][0] - op[0];
            dc = lista[2][1] - op[1];
            em = lista[0][0] + op[0];
            ec = lista[0][1] + op[1];

            if dm<0 or dc<0 or em<0 or ec<0:
                break;

            if dm >= dc and em >= ec and dm >=0 and dc >= 0 and em >= 0 and ec >= 0 or dm ==0 or em == 0:

                barco = 'esquerda';
                busca.append([[em,ec], barco, [dm,dc]]);
                print busca

                if busca[busca.index(lista)+1][2][0] == 0 and busca[busca.index(lista)+1][2][1] == 0:
                    print "TERMINOU", busca
                    exit;
        else:
            dm = lista[2][0] + op[0];
            dc = lista[2][1] + op[1];
            em = lista[0][0] - op[0];
            ec = lista[0][1] - op[1];

            if dm<0 or dc<0 or em<0 or ec<0:
                break;

            if dm >= dc and em >= ec and dm >=0 and dc >= 0 and em >= 0 and ec >= 0:

                barco = 'direita';
                busca.append([[em,ec], barco, [dm,dc]]);
                print busca

                if busca[busca.index(lista)+1][2][0] == 0 and busca[busca.index(lista)+1][2][1] ==0:
                    print "TERMINOU", busca
                    exit;

