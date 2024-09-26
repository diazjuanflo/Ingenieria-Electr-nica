function y=fxy(x,y)
    y=1.131-(3.2/(192+0.7*x))*y;
endfunction
clc
clear x y
x0=input("Digite el valor de t0 : ")
y0=input("Digite el valor de C0 : ")
xf=input("Digite el t final : ")
n=input("Digite el numero de pasos : ")
h=(xf-x0)/n;1
i=1;x(1)=x0;y(1)=y0;
//plot(x0,y0,'or');xgrid
while (i<=n)
    m0=fxy(x0,y0);
    x1t=x0+h;
    y1t=y0+m0*h;
    m1=fxy(x1t,y1t);
    mm=(m0+m1)/2;
    x1=x0+h;
    y1=y0+mm*h;
    disp([x0 y0 mm x1  y1 ])
    i=i+1;
    x(i)=x1;y(i)=y1;  
    x0=x1;y0=y1;    
end
plot(x,y,'-r');xgrid
title("CONCENTRACION DE SAL");
ylabel("Concentracion (g)")
xlabel("Tiempo (m)")
plot(0,0)
