function y=f(x)
    y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
clc;sA=0;
li=input('Digite lim inf :');Li=li;
ls=input('Digite lim sup :')
n=input('Digite num subareas :')
dx=(ls-li)/(3*n);h=dx/2;
i=1;while (i<=n)
y0=f(Li);
y1=f(Li+dx);
y2=f(Li+2*dx);
y3=f(Li+3*dx);
At=3*dx/8*(y0+3*y1+3*y2+y3)
sA=sA+At;
Li=Li+3*dx;
i=i+1;
end
disp(sA)
