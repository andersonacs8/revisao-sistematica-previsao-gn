import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.ticker as mt, numpy as np, os
SAIDA = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.edgecolor': '#8a8984', 'axes.labelcolor': '#52514e', 'xtick.color': '#52514e', 'ytick.color': '#52514e',
    'figure.facecolor': 'white', 'axes.grid': True, 'grid.color': '#e6e5e1', 'grid.linewidth': 0.6,
    'axes.axisbelow': True, 'legend.frameon': False})
TXT, MUT = '#0b0b0b', '#8a8984'
AZUL, LARANJA, VERDE, ROXO = '#2a78d6', '#eb6834', '#1baf7a', '#6250d6'
N = 108

# Figura A: itens de comparabilidade e lacunas (funde Tabelas 4.2 e 4.6)
itens = [('Modelo de fundação', 0, 'c'), ('Consumidor industrial individual', 2, 'c'),
         ('Exigência de erro declarada', 2, 'c'), ('Compara com ingênuo', 5, 'r'),
         ('Modelo global', 6, 'c'), ('Métrica escalada (MASE)', 6, 'r'),
         ('Teste de significância', 10, 'r'), ('Validação com origem móvel', 13, 'r'),
         ('Relata custo computacional', 15, 'r'), ('Unidade = consumidor (qualquer tipo)', 17, 'c'),
         ('Dados públicos', 32, 'r')]
cor = {'r': AZUL, 'c': LARANJA}
fig, ax = plt.subplots(figsize=(7, 4.2))
y = np.arange(len(itens))
for i, (nome, n, g) in enumerate(itens):
    p = 100 * n / N
    ax.barh(i, p, color=cor[g], height=.62)
    ax.text(p + .6, i, f'{n} ({p:.1f}%)'.replace('.', ','), va='center', fontsize=9, color=TXT)
ax.set_yticks(y); ax.set_yticklabels([i[0] for i in itens]); ax.invert_yaxis()
ax.set_xlim(0, 40); ax.xaxis.set_major_formatter(mt.PercentFormatter(decimals=0))
ax.set_xlabel('% dos 108 estudos do bloco A'); ax.grid(axis='y', visible=False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=AZUL, label='Rigor e comparabilidade'), Patch(color=LARANJA, label='Cobertura de temas')],
          loc='upper right')
fig.savefig(os.path.join(SAIDA, 'fig_rigor_lacunas.png'), dpi=300, bbox_inches='tight')

# Figura B: família vencedora nas comparações neutras por metade do período, com IC de Wilson
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z**2 / n; c = (p + z**2 / (2*n)) / d
    h = z * np.sqrt(p*(1-p)/n + z**2/(4*n**2)) / d
    return 100*p, 100*max(0, c-h), 100*min(1, c+h)
fams = ['Estatístico', 'ML clássico', 'Rede neural', 'Híbrido']
dados = {'2015–2021 (n = 8)': ([3, 3, 1, 1], 8, '#9bbfe9'), '2022–2026 (n = 7)': ([2, 2, 3, 0], 7, AZUL),
         'Total (n = 15)': ([5, 5, 4, 1], 15, TXT)}
fig, ax = plt.subplots(figsize=(7, 3.8))
off = [-.22, 0, .22]
for j, (lab, (ks, n, c)) in enumerate(dados.items()):
    for i, k in enumerate(ks):
        p, lo, hi = wilson(k, n)
        ax.plot([lo, hi], [i + off[j]]*2, color=c, lw=2)
        ax.plot(p, i + off[j], 'o', color=c, ms=6, mec='white', mew=1, label=lab if i == 0 else None)
ax.axvline(100*2/3, color=LARANJA, lw=1, ls='--'); ax.axvline(50, color=MUT, lw=1, ls=':')
ax.text(100*2/3 + 1, -.6, 'consenso (2/3)', color=LARANJA, fontsize=8.5, va='center')
ax.text(49, -.6, 'tendência (maioria)', color=MUT, fontsize=8.5, va='center', ha='right')
ax.text(wilson(3,7)[0] + 1.5, 2 - .02, '*', fontsize=11, color=TXT, va='bottom')
ax.text(77, 2 + .0, '* 2 de 3 vitórias em comparações\n   só entre redes neurais', fontsize=8, color=MUT, va='center')
ax.set_yticks(range(4)); ax.set_yticklabels(fams); ax.set_ylim(3.5, -.85)
ax.set_xlim(0, 100); ax.xaxis.set_major_formatter(mt.PercentFormatter(decimals=0))
ax.set_xlabel('% das comparações neutras vencidas (IC 95% de Wilson)'); ax.grid(axis='y', visible=False)
ax.legend(loc='lower right', fontsize=9)
fig.savefig(os.path.join(SAIDA, 'fig_neutras_periodo.png'), dpi=300, bbox_inches='tight')

# Figura C: ganho por estrato (mediana e IIQ), Tabela 4.4
grupos = [('Ajuste dos concorrentes descrito', [('Sim', 9, 12.5, 3.6, 29.5), ('Parcial', 17, 33.4, 12.4, 50.9), ('Não', 40, 29.0, 8.6, 45.1)]),
          ('Nº de concorrentes', [('1–2', 13, 31.9, 12.9, 34.6), ('3–4', 29, 24.4, 8.9, 39.6), ('5 ou mais', 22, 24.1, 6.8, 63.5)]),
          ('Compara com ingênuo', [('Sim', 5, 22.8, 4.3, 28.8), ('Não', 62, 29.3, 8.1, 43.5)]),
          ('Validação', [('Origem móvel', 7, 24.4, 14.2, 27.1), ('Holdout único', 44, 31.9, 11.4, 51.2), ('Não clara', 16, 23.4, 2.8, 33.5)])]
cores = [AZUL, LARANJA, VERDE, ROXO]
fig, ax = plt.subplots(figsize=(7, 5.6))
y = 0; ticks, labs, heads = [], [], []
for g, (nome, est) in enumerate(grupos):
    heads.append((y, nome)); y += 1
    for lab, n, md, q1, q3 in est:
        ax.plot([q1, q3], [y, y], color=cores[g], lw=2.2)
        ax.plot(md, y, 'o', color=cores[g], ms=7, mec='white', mew=1)
        ax.text(q3 + 1.2, y, f'{md:.1f}%  (n = {n})'.replace('.', ','), va='center', fontsize=8.5, color=TXT)
        ticks.append(y); labs.append(lab); y += 1
    y += .5
for yy, nome in heads:
    ax.text(-1, yy, nome, fontweight='bold', fontsize=9.5, color=TXT, ha='left', va='center', transform=ax.get_yaxis_transform() if False else ax.transData)
ax.axvline(28.8, color=MUT, lw=.9, ls=':'); ax.text(28.8, -1.1, 'mediana geral 28,8%', color=MUT, fontsize=8, ha='center')
ax.set_yticks(ticks); ax.set_yticklabels(labs); ax.set_ylim(y - .5, -1.6)
ax.set_xlim(-1, 80); ax.xaxis.set_major_formatter(mt.PercentFormatter(decimals=0))
ax.set_xlabel('ganho sobre o melhor concorrente de outra família (mediana e IIQ)'); ax.grid(axis='y', visible=False)
fig.savefig(os.path.join(SAIDA, 'fig_ganho_estratos.png'), dpi=300, bbox_inches='tight')
print('ok')
