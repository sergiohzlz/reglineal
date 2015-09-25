#!/usr/bin/python
#-*-coding:utf8-*-

from pylab import *

def error(b,m, P):
    ET = 0.0
    for i in xrange(0,len(P)):
        x = P[i,0]
        y = P[i,1]
        ET += (y - (m*x + b))**2
    return ET / float(len(P))


def paso_gradiente(b_act, m_act, P, ca):
    """
    b_act interseccion abscisas actual
    m_act pendiente actual
    P array con puntos
    ca constante de aprendizaje
    """
    b_grad, m_grad = 0,0
    N = len(P)
    for i in xrange(0,N):
        x = P[i,0]
        y = P[i,1]
        b_grad += (2/N) * (y - (m_act*x + b_act))
        m_grad += (2/N) * (y - (m_act*x + b_act))
    b_nva = b_act - (ca * b_grad)
    m_nva = m_act - (ca * m_grad)
    return [b_nva, m_nva]

def grad_desc( P, b_0, m_0, ca, iters):
    b = b_0
    m = m_0
    for i in xrange(iters):
        b, m = paso_gradiente( b, m, P, ca)
    return [b,m]

def ejemplo():
    P = genfromtxt('data.csv', delimiter=',')
    ca = 0.00001
    b_ini = 0
    m_ini = 0
    iters = 1000
    error_i = error(b_ini, m_ini, P)
    print "Descenso en b= {0}, m={1}, error={2}".format(b_ini, m_ini, error_i)
    [b,m] = grad_desc( P, b_ini, m_ini, ca, iters )
    error_f = error(b,m,P)
    print u"Después de {0} iteraciones b={1}, m={2}, error={3}".format(iters, b,m,error_f)
    
if __name__ =='__main__':
    ejemplo()
