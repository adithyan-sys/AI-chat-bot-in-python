from pylab import *
theta = linspace(0,5*pi,1000)
r = 5*abs(cos(2*theta))
polar(theta,r,'r')
show()