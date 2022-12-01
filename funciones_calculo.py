from math import sqrt

#FUNCIONES MRU
def mru_calcular_posicio_final(posicio_inicial, velocitat, temps):
    posicio_final = posicio_inicial + velocitat * temps
    return posicio_final

def mru_calcular_temps(posicio_inicial, velocitat, posicio_final):
    temps = (posicio_final - posicio_inicial) / velocitat
    return temps

def mru_calcular_velocitat(posicio_inicial, posicio_final, temps):
    velocitat = (posicio_final - posicio_inicial) / temps
    return velocitat

def mru_calcular_posicio_inicial(posicio_final, velocitat, temps):
    posicio_inicial = posicio_final - velocitat * temps
    return posicio_inicial 


#FUNCIONES FUERZAS
def forca_calcular_forca(massa, acceleracio):
    forca_total = massa * acceleracio
    return forca_total

def forca_calcular_massa(forca, acceleracio):
    massa = forca / acceleracio 
    return massa

def forca_calcular_acceleracio(forca, massa):
    acceleracio = forca / massa 
    return acceleracio 

#FUNCIONES ENERGIA POTENCIAL

def ep_calcular_ep(massa, gravetat, altura):
    ep_total = massa * gravetat * altura
    return ep_total

def ep_calcular_massa(energia_potencial, gravetat, altura):
    massa = energia_potencial / (altura * gravetat)
    return massa

def ep_calcular_gravetat(energia_potencial, massa, altura):
    gravetat = energia_potencial / (massa * altura)
    return gravetat

def ep_calcular_altura(energia_potencial, massa, gravetat):
    altura = energia_potencial / (massa * gravetat)
    return altura 

#FUNCIONES ENERGIA CINETICA
def ec_calcular_ec(massa, velocitat):
    ec = (1/2) * massa * (velocitat)**2
    return ec

def ec_calcular_massa(energia_cinetica, velocitat):
    ec_massa = (energia_cinetica * 2) / (velocitat)**2
    return ec_massa 

def ec_calcular_velocitat(energia_cinetica, massa):
    ec_velocitat = sqrt((energia_cinetica * 2) / massa)
    return ec_velocitat 


#FUNCION MRUA

def calcular_x(x0, v, t, a):
    x = x0 + v * t + 1/2 * a * t**2
    return x 

# FUNCION FORÇA DE FREGAMENT

def forca_fregament_calcular_ff(coeficient_friccio, forca_normal):
    forca_fregament = coeficient_friccio * forca_normal
    return forca_fregament

def ff_calcular_coeficient_friccio(forca_fregament, forca_normal):
    coeficient_friccio = forca_fregament / forca_normal
    return coeficient_friccio

def ff_calcular_normal(forca_fregament, coeficient_friccio):
    forca_normal = forca_fregament / coeficient_friccio
    return forca_normal 

#FUNCIONS INTENSTITAT DE CAMP

def intensitat_camp_calcul(forca, massa):
    intensitat_camp = forca / massa
    return intensitat_camp

def ic_calcular_forca(intensitat_camp, massa):
    forca = massa * intensitat_camp
    return forca 

def ic_calcular_massa(intensitat_camp, forca):
    massa = forca / intensitat_camp
    return massa

#FUNCIONS ENERGIA MECANICA

def energia_mecanica_calcul(ec, ep):
    energia_mecanica = ec + ep
    return energia_mecanica

def em_calcular_ec(em, ep):
    energia_cinetica = em - ep 
    return energia_cinetica

def em_calcular_ep(em, ec):
    energia_potencial = em - ec
    return energia_potencial

#FUNCIONES CAMP GRAVITATORI

def camp_gravitatori_calcul(massa, r):
    intensitat_camp_gravitatori = 6.67 * 10**-11 * (massa / (r)**2)
    return intensitat_camp_gravitatori

def cg_calcul_massa(cg, r):
    massa = (cg * (r)**2) / 6.67 * 10**-11 
    return massa

def cg_calcul_distancia(cg, massa):
    distancia = sqrt(((6.67 * 10**-11) * massa) / cg )
    return distancia

#FUNCIONES EP GRAVITATORIA

def ep_gravitatoria_calcul(m_1, m_2, r):
    ep = -(6.67 * 10**-11) * ((m_1 * m_2) / r)
    return ep 

def epg_calcular_massa_1(ep, m_2, r):
    m_1 = (ep * r) / (-(6.67 * 10**-11) * m_2)
    return m_1

def epg_calcular_massa_2(ep, m_1, r):
    m_2 = (ep * r) / (-(6.67 * 10**-11) * m_1)
    return m_2

def epg_calcular_distancia(ep, m_1, m_2):
    r = (-(6.67 * 10**-11) * m_1 * m_2) / ep
    return r

#FUNCIONES GRAVITACIÓ UNIVERSAL

def gu_calcular_forca_atraccio(m_1, m_2, r):
    forca_atraccio = (6.67 * 10**-11) * ((m_1 * m_2) / (r)**2)
    return forca_atraccio

def gu_calcular_r(f, m_1, m_2):
    r = sqrt(((6.67 * 10**-11) * m_1 * m_2) / (f))
    return r 

def gu_calcular_massa_1(f, m_2, r):
    m_1 = (f * (r)**2) / ((6.67 * 10**-11) * m_2)
    return m_1

def gu_calcular_massa_2(f, m_1, r):
    m_2 = (f * (r)**2) / ((6.67 * 10**-11) * m_1)
    return m_2 