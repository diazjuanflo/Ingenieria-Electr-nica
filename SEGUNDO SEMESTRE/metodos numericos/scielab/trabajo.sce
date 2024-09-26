function y=f(x)
    y=x*x-4;
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

