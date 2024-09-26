function y=f(t)
    y=6+(2.35*t^2)-(0.0035*t^4)
endfunction
function g=g(t)
    g=2*2.29*t-0.0029*4*t^3
endfunction
t=0:30
dy=2*2.29*t-0.0029*4*t^3
plot(t,f(t))
plot(t,g(t),"r")
title("TRAYECTORIA DEL COHETE");
ylabel("Altura (m)")
xlabel("Tiempo (s)")
xarrows([0 30],[0 0],500,5)
xarrows([0 0],[-300 500],500,5)
xgrid
clc

x0=input("Digita el Primer Valor inicial de x0: ");
x2=input("Digita el Primer Valor inicial de x1: ");
printf('\n METODO DE NEWTON RAPHSON \n');
printf('\n TIEMPO DE VUELO \n');
printf('\n \tx0 \tf(x0)  \tdf(x0)  \tx1 \n')
//f'(x0)
h=1e-6;
while abs(f(x0))>=h

dfx=(f(x0+h)-f(x0))/h;

//f(x0)
fx=f(x0);

//APLICO FORMULA DE NEWTON RAPHSON
x1=x0-fx/dfx;

//TABULO
printf('%11.3f %9.3f %8.3f %13.3f\n',x0,fx,dfx,x1)

//REINICIO PROCESO
x0=x1;

end

printf('\n La Raiz es: %5.3f\n',x1)



printf('\n ALTURA DEL COHETE \n');
printf('\n \tx2 \tg(x2)  \tdg(x2)  \txm \n')

while abs(g(x2))>=h

dgx=(g(x2+h)-g(x2))/h;

gx=g(x2);

xm=x2-gx/dgx;

printf('%11.3f %9.3f %8.3f %13.3f\n',x2,gx,dgx,xm)

x2=xm;

end
printf('\n La Raiz es: %5.3f\n',-1*x2)

Altura=f(x2)

printf('\n El Tiempo Maximo de Vuelo es: %5.3f',x1," s\n")
printf('\n La Altura Maxima Alcanzada es: %5.3f',Altura," m\n")



