function y=fxy(x,y)
    y=1.34-(2.35/(1053+0.18*x))*y;
endfunction
clc
clear x y
x0=input("Digite el valor de x0 : ")
y0=input("Digite el valor de y0 : ")
xf=input("Digite el x final : ")
n=input("Digite el numero de pasos : ")
h=(xf-x0)/n;1
i=1;x(1)=x0;y(1)=y0;
while (i<=n)
    m0=fxy(x0,y0);
    m1=fxy(x0+h/2,y0+m0*h/2);
    m2=fxy(x0+h/2,y0+m1*h/2);
    m3=fxy(x0+h,y0+m2*h);
    mm=(m0+2*m1+2*m2+m3)/6;
    x1=x0+h;
    y1=y0+mm*h;
    disp([x0 y0 mm x1  y1])
    i=i+1;
    x(i)=x1;y(i)=y1;  
    x0=x1;y0=y1;    
end
plot(x,y,'.r');xgrid
plot(0,0)
