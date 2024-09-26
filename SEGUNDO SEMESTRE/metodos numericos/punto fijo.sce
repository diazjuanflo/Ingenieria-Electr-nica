function y=f(x)
   y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
x0=input('Digite un primer valor ');
while (abs(x1)>=1e-6)
    x1=((80*exp(-0.05*x0)+20*exp(-0.3*x0))x0)/53;
disp([x0 x1])
end
