function [out]=circuito1tallerl2hrho_iin(s,Fhfe_Q1,Rb,Rhie_Q1,Rl,Rs,Vs)
num = + ( -Vs*Rhie_Q1 -Vs*Rb );
den = + ( -Rhie_Q1*Rs -Rb*Rs -Rb*Rhie_Q1 );
out = num/den;
end
