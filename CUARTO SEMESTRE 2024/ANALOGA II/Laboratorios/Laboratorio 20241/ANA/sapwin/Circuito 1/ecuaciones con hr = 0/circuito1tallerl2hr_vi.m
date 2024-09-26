function [out]=circuito1tallerl2hr_vi(s,Fhfe_Q1,Ghoe_Q1,Rb,Rhie_Q1,Rl,Rs,Vs)
num = + ( -Vs*Ghoe_Q1*Rb*Rhie_Q1*Rl -Vs*Rb*Rhie_Q1 );
den = + ( -Ghoe_Q1*Rhie_Q1*Rl*Rs -Ghoe_Q1*Rb*Rl*Rs -Ghoe_Q1*Rb*Rhie_Q1*Rl -Rhie_Q1*Rs -Rb*Rs -Rb*Rhie_Q1 );
out = num/den;
end
