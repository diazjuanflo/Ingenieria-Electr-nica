function puntofijo(g)
x=input("digite un valor inicial: ");
n=input("digite el numero de interaciones deseadas: ");
tol=input("digite el porcentaje de error: ");

for k=1:n
    if (abs(x-g(x))<tol)
        fprintf('\nx%d=%f es muy aproximado \n',k,x)
        return
    end
    x=g(x);
fprintf('x%d=%f \n',k,x)
end