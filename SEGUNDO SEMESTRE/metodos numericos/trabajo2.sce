function y=f(x)
    y=80*exp(0.05*x)+20*exp(0.3*x)-53;
    yi=t(x)
    t=
endfunction
h=1e-6;
x0=input('Denme un primer valor ');
while (f(x0)>=h)
   fx=f(x0);
    dfx=(f(x0+h)-f(x0))/h;
    x1=x0-fx/dfx;
   disp([fx dfx  x1])
    x0=x1;
end
