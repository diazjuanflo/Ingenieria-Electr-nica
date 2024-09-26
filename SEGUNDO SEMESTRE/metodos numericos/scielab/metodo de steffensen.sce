function y=f(x)
    y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
x0=input('Digite un primer valor ');
while (abs(f(x0))>=1e-6) 

x1=x0-(f(x0)^2)/(f(x0+f(x0))-f(x0))
disp([x0 x1])
x0=x1

end
