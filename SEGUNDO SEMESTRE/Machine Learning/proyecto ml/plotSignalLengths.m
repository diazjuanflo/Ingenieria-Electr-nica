function plotSignalLengths(Signals)
L = cellfun(@length,Signals);
h = histogram(L);

xticks(0:3000:18000);
xticklabels(0:3000:18000);
title('Signal Lengths') 
xlabel('Length')
ylabel('Count')
end

