#--------------------------------------------------------
#		MODULE - Creation de Fractals 
#
#	Le but de ce module est la creation de limage
#	des fractals et faire le tritement des differents
#	coloeurs. 
#--------------------------------------------------------
from PIL import Image

# pour le Zoom l'utilisateur doit choisir entre *1 , *2, .... ,*10
# pour le nombre d'itérations : 50 200 800 2000


#Fonction pour la creation du nom de limage.
def nomCreation(real,imag,n_int,color,zoom):	
#    if(str(real).count('.') == 0):
#       real = str(real) + '.0'	
    aux = str(real).split('.')
    nom = aux[0]+aux[1]+'_'
    aux = str(imag).split('.')
    nom = nom + aux[0] + aux[1] + '_' + str(n_int) + '_' + str(color) + '_' + str(zoom)
    return nom	

#Creation de limage des fractals 
def fractale(couleur,size1,size2,Re,Im,zoom,ite):
    size=(size1,size2)
    im=Image.new('RGB', size, (0,0,0) )
    px=im.load()
    c=complex(Re,Im)
    if (couleur==1):		#Traitement Noir et Blanc
        for i in range (size1):
            for j in range (size2) :
                TraitNoirBlanc(px,i,j,c,size1,size2,zoom,ite)
    if (couleur==2): 		#Traitement Rouge
        for i in range (size1):
            for j in range (size2) :
                TraitRouge(px,i,j,c,size1,size2,zoom,ite)
    if (couleur==3): 		#Traitement Vert
        for i in range (size1):
            for j in range (size2) :
                TraitVert(px,i,j,c,size1,size2,zoom,ite)
    if (couleur==4): 		#Traitement Blue
        for i in range (size1):
            for j in range (size2) :
                Traitbleu(px,i,j,c,size1,size2,zoom,ite)

    return im
        

def TraitNoirBlanc(px,i,j,c,size1,size2,zoom,ite):
    # si le résultat diverge le point sera blanc 
    # si le résultat ne diverge pas le point sera noir
    # c'est montré que c'est le module ne depasse pas 2 au bout d'un moment le résultat ne diverge pas
    
    n=ite  
    xmilieu=size1/2
    ymilieu=size2/2
    z=complex((i-xmilieu)/(0.4*zoom*size1),(j-ymilieu)/(0.4*zoom*size2))
    compt=0
    
    while(compt<n and abs(z)<2):
        z= z*z + c
        compt=compt +1
    if (compt==n) :
        px[i,j]=(0,0,0)
    if (compt<n) :
        px[i,j]=(255-compt,255-compt,255-compt)

def TraitRouge(px,i,j,c,size1,size2,zoom,ite):
    # si le résultat diverge le point sera coloré 
    # si le résultat ne diverge pas le point sera noir
    # c'est montré que c'est le module ne depasse pas 2 au bout d'un moment le résultat ne diverge pas
    
    n=ite
    xmilieu=size1/2
    ymilieu=size2/2
    z=complex((i-xmilieu)/(0.4*zoom*size1),(j-ymilieu)/(0.4*zoom*size2))
    compt=0
    
    while(compt<n and abs(z)<2):
        z= z*z + c
        compt=compt +1
    if (compt==n) :
        px[i,j]=(0,0,0)
    if (compt<n) :
#        px[i,j]=(255-compt,20+compt,20+compt)
        px[i,j]=(10*round(255*(compt/n)),6*round(255*(compt/n))-40,4*round(255*(compt/n)))
        
def TraitVert(px,i,j,c,size1,size2,zoom,ite):
    # si le résultat diverge le point sera coloré 
    # si le résultat ne diverge pas le point sera noir
    # c'est montré que c'est le module ne depasse pas 2 au bout d'un moment le résultat ne diverge pas
    
    n=ite 
    xmilieu=size1/2
    ymilieu=size2/2
    z=complex((i-xmilieu)/(0.4*zoom*size1),(j-ymilieu)/(0.4*zoom*size2))
    compt=0
    
    while(compt<n and abs(z)<2):
        z= z*z + c
        compt=compt +1
    if (compt==n) :
        px[i,j]=(0,0,0)
    if (compt<n) :
        px[i,j]=(4*round(255*(compt/n)),10*round(255*(compt/n)),6*round(255*(compt/n))-40)

def Traitbleu(px,i,j,c,size1,size2,zoom,ite):
    # si le résultat diverge le point sera coloré 
    # si le résultat ne diverge pas le point sera noir
    # c'est montré que c'est le module ne depasse pas 2 au bout d'un moment le résultat ne diverge pas
    
    n=ite 
    xmilieu=size1/2
    ymilieu=size2/2
    z=complex((i-xmilieu)/(0.4*zoom*size1),(j-ymilieu)/(0.4*zoom*size2))
    compt=0
    
    while(compt<n and abs(z)<2):
        z= z*z + c
        compt=compt +1
    if (compt==n) :
        px[i,j]=(0,0,0)
    if (compt<n) :
        px[i,j]=(4*round(255*(compt/n)),6*round(255*(compt/n))-40,10*round(255*(compt/n)))

