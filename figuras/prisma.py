import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
INK='#1f1f1f'; LINE='#555555'; BOX='#ffffff'; SIDE='#f3f3f3'; STAGE='#dde3ea'
fig,ax=plt.subplots(figsize=(10,12.4)); ax.set_xlim(0,100); ax.set_ylim(0,124); ax.axis('off')
def box(x,y,w,h,txt,fc=BOX,fs=9.5,bold_first=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.25,rounding_size=0.8",fc=fc,ec=LINE,lw=1))
    ax.text(x+1.5,y+h/2,txt,va='center',ha='left',fontsize=fs,color=INK,linespacing=1.35)
def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=LINE,lw=1.1,shrinkA=0,shrinkB=0))
def stage(y,h,label):
    ax.add_patch(FancyBboxPatch((0.5,y),5,h,boxstyle="round,pad=0.2,rounding_size=0.8",fc=STAGE,ec='none'))
    ax.text(3,y+h/2,label,rotation=90,va='center',ha='center',fontsize=10,fontweight='bold',color=INK)
LX,LW=9,46; RX,RW=61,38.5
ax.text(50,122.5,'Identificação de estudos em bases de dados',ha='center',fontsize=11,fontweight='bold',color=INK)
# Identificação
stage(102,18,'Identificação')
box(LX,104,LW,14,'Registros identificados (n = 2.897)\n  Scopus: bloco A 1.234; bloco B 325\n  Web of Science: bloco A 1.022; bloco B 228\n  arXiv (bloco B): 88')
box(RX,106,RW,10,'Registros removidos antes da triagem\n  Duplicatas (DOI ou título\n  normalizado): n = 965',fc=SIDE)
arrow(LX+LW,111,RX,111)
# Triagem
stage(45,54,'Triagem')
box(LX,88,LW,8,'Registros triados por título e resumo\n(n = 1.932)')
box(RX,88,RW,8,'Registros excluídos (n = 1.647)',fc=SIDE)
arrow(LX+LW/2,104,LX+LW/2,96); arrow(LX+LW,92,RX,92)
box(LX,74,LW,8,'Textos completos buscados\n(n = 285)')
box(RX,74,RW,8,'Textos completos não obtidos\n(acesso pago; n = 78)',fc=SIDE)
arrow(LX+LW/2,88,LX+LW/2,82); arrow(LX+LW,78,RX,78)
box(LX,55,LW,8,'Textos completos avaliados quanto\nà elegibilidade (n = 207)')
box(RX,47,RW,24,'Textos completos excluídos (n = 28)\n  EC3 sem avaliação fora da\n        amostra ou sem métricas: 11\n  EC4 fora do domínio: 8\n  EC2 agregado nacional anual: 7\n  EC1 preço, produção ou\n        comércio: 1\n  EC7 duplicata ou versão\n        anterior: 1',fc=SIDE,fs=9)
arrow(LX+LW/2,74,LX+LW/2,63); arrow(LX+LW,59,RX,59)
# Inclusão
stage(2,32,'Inclusão')
box(LX,4,LW,28,'Artigos incluídos (n = 179)\n  = 176 estudos (3 publicações\n     redundantes contadas uma vez)\n  Revisões: 6\n  Estudos empíricos ou comparativos: 170\n     Bloco A (gás natural): 108\n     Bloco B (modelos globais e de\n     fundação em energia): 62')
arrow(LX+LW/2,55,LX+LW/2,32)
fig.text(0.5,0.005,'Adaptado do modelo de fluxograma PRISMA 2020 (Page et al., 2021).',ha='center',fontsize=8.5,color='#666666')
plt.savefig('fig_prisma.png',dpi=300,bbox_inches='tight',facecolor='white'); plt.savefig('fig_prisma.svg',bbox_inches='tight',facecolor='white'); plt.savefig('fig_prisma.pdf',bbox_inches='tight',facecolor='white')
