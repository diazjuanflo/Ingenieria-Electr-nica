(80e^(-0,05x)+20e^0,3x )x/53// punto medio
function y=f(x)
    y=80*exp(-0.05*x)+20*exp(-0.3*x)-53;
endfunction
clc //
a = input("Digite un primer valor: ");
b = input("Digite un segundo valor: ");
error=1e-8;m=a;
while abs(f(m))>=error
    m=(a*f(b)-b*f(a))/(f(b)-f(a))
    if f(a)*f(m)>=0
        a=m
    else
        b=m
    end
    disp ([m f(m)])
end

