function y=f(x)
    y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
clc;sA=0;
li=input('Digite lim inf :');Li=li;
ls=input('Digite lim sup :')
n=input('Digite num subareas :')
dx=(ls-li)/n
h=(dx)/(2)
i=1;while (i<=n)
y0=f(Li);
y1=f(Li+h);
y2=f(Li+2*h);
At=h/3*(y0+4*y1+y2)
sA=sA+At;
Li=Li+2*h;
i=i+1;
end
disp(sA)
