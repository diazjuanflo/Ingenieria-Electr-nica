function [out]=circuito1tallerl2hrho_dvo(s,Fhfe_Q1,Rb,Rhie_Q1,Rl,Rs,Vs)
num = + ( Vs*Fhfe_Q1*Rb*Rl );
den = + ( -Rhie_Q1*Rs -Rb*Rs -Rb*Rhie_Q1 );
out = num/den;
end
