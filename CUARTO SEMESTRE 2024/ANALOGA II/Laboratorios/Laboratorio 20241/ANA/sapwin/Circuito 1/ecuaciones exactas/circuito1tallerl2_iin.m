function [out]=circuito1tallerl2_iin(s,Ehre_Q1,Fhfe_Q1,Ghoe_Q1,Rb,Rhie_Q1,Rl,Rs,Vs)
num = + ( Vs*Fhfe_Q1*Ehre_Q1*Rl -Vs*Ghoe_Q1*Rhie_Q1*Rl -Vs*Ghoe_Q1*Rb*Rl -Vs*Rhie_Q1 -Vs*Rb );
den = + ( Fhfe_Q1*Ehre_Q1*Rl*Rs +Fhfe_Q1*Ehre_Q1*Rb*Rl -Ghoe_Q1*Rhie_Q1*Rl*Rs -Ghoe_Q1*Rb*Rl*Rs -Ghoe_Q1*Rb*Rhie_Q1*Rl -Rhie_Q1*Rs -Rb*Rs -Rb*Rhie_Q1 );
out = num/den;
end
