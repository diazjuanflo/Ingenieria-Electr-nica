function y=F(x)
    y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
clc
x=0:10;
y=F(x)
plot(x,y);xgrid
error=1e-6;
a=input('Digite un valor para a :')   //0.035
b=input('Digite un valor para b :')   //0.075
m=a;
mprintf("     a         F(a)        b         F(b)       m        F(m)\n")
while  (abs(F(m))>=error)
   m=(a+b)/2                                  // Punto Medio
   mprintf("%10.6f %10.6f %10.6f %10.6f %10.6f %15.12f\n",a,F(a),b,F(b),m,F(m))
    if (F(a)*F(m)>=0) then
       a=m
    else
        b=m
  end
end
