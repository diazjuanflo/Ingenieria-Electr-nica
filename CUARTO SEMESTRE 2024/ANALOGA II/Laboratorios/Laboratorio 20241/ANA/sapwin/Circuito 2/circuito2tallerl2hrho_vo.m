function [out]=circuito2tallerl2hrho_vo(s,Fhfe_Q1,Rb,Re,Rhie_Q1,Rl,Rs,Vs)
num = + ( Vs*Fhfe_Q1*Rb*Rl );
den = + ( -Fhfe_Q1*Re*Rs -Fhfe_Q1*Rb*Re -Rhie_Q1*Rs -Re*Rs -Rb*Rs -Rb*Rhie_Q1 -Rb*Re );
out = num/den;
end
