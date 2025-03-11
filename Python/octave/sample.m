pkg load control
pkg load symbolic

syms s I1 I2 I3 V
a = [(s^2+7*s+5) -(s^2-2*s) -(5*s); -(s^2-2*s) (2*s^3+4*s+3) -(s^2-2*s); -(5*s) -(s^2-2*s) (s^2+8*s+4); (s^2+7*s+5) -(s^2-2*s) -(5*s); -(s^2-2*s) -(2*s^2+4*s+3) -(5^2-2*s)]
