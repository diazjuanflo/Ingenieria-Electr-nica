function [out]=circuito1tallerl2hrho_vi(s,Fhfe_Q1,Rb,Rhie_Q1,Rl,Rs,Vs)
num = + ( -Vs*Rb*Rhie_Q1 );
den = + ( -Rhie_Q1*Rs -Rb*Rs -Rb*Rhie_Q1 );
out = num/den;
end
