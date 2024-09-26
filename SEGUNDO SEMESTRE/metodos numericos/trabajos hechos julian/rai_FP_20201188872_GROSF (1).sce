function y=f(x) //FUNCION
    y=89*exp(-0.02*x)+11*exp(-0.9*x)-29
endfunction
clc
// GRAFICO LA FUNCION
x=0:70;
plot(x,f(x))
xarrows([0 70],[0 0],60,5)
xarrows([0 0],[-10 80],60,5)
xgrid

//FORMULA METODO-FALSA POSICION
//m=(a*f(b)-b*f(a))/(f(b)-f(a))
a=input("Digita el Primer Valor inicial A: ");
b=input("Digita el Segundo Valor inicial B: ");
printf('\n METODO DE FALSA POSICION \n');
printf('\n \ta \tf(a)    \tb    \tf(b) \n')
h=1e-6;
m=a;
while abs(f(m))>=h

//APLICO FORMULA DE FALSA POSICION
m=(a*f(b)-b*f(a))/(f(b)-f(a));
fa=f(a);
fb=f(b);
printf('%11.3f %9.3f %13.3f %9.3f\n',a,fa,b,fb)

//INTERACTUO O CONDICIONO A Y B
if f(a)*f(m)>0 then
a=m;
else
b=m;
end
end

//RESULTADO RAIZ
printf('\n La Raiz es: %5.3f\n',m);
