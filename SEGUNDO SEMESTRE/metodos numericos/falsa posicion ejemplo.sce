function y=F(x)
   y=x^2-4
endfunction
clc
x=0:5;
y=F(x)
plot(x,y);xgrid
error=1e-6;
a=input('Digite un valor para a :')   //0.035
b=input('Digite un valor para b :')   //0.075
m=a;
mprintf("     a         F(a)        b         F(b)       m        F(m)\n")
while  (abs(F(m))>=error)
   m=(a*F(b)-b*F(a))/(F(b)-F(a))    //Falsa Posicion
   //m=(a+b)/2                                  // Punto Medio
   mprintf("%10.6f %10.6f %10.6f %10.6f %10.6f %15.12f\n",a,F(a),b,F(b),m,F(m))
    if (F(a)*F(m)>=0) then
       a=m
    else
        b=m
  end
end
