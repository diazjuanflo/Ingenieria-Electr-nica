function plotBothHistograms(sig_norm, sig_afib, Labels)
    mn_norm = mean(sig_norm{1,:});
    med_norm = median(sig_norm{1,:});
    std_norm = std(sig_norm{1,:});
    skew_norm = skewness(sig_norm{1,:}, 1, 2);
    k_norm = kurtosis(sig_norm{1,:}, 1, 2);
    
    mn_afib = mean(sig_afib{1,:});
    med_afib = median(sig_afib{1,:});
    std_afib = std(sig_afib{1,:});
    skew_afib = skewness(sig_afib{1,:}, 1, 2);
    k_afib = kurtosis(sig_afib{1,:}, 1, 2);
    
    str_norm = {['Mean: ', num2str(mn_norm)], ['Median: ', num2str(med_norm)], ['Std:', num2str(std_norm)], ...
        ['Skewness: ', num2str(skew_norm)], ['Kurtosis: ', num2str(k_norm)]};
    str_afib = {['Mean: ', num2str(mn_afib)], ['Median: ', num2str(med_afib)], ['Std:', num2str(std_afib)], ...
        ['Skewness: ', num2str(skew_afib)], ['Kurtosis: ', num2str(k_afib)]};
    
    tiledlayout(2,1)
    ax1 = nexttile;
    histogram(ax1, sig_norm{1,:}, 'FaceColor', 'blue');
    legend(Labels(1,:))
    text(400, 1000,str_norm);
    
    ax2 = nexttile;
    histogram(ax2, sig_afib{1,:}, 'FaceColor', 'red');
    legend(Labels(5,:))
    text(400, 1000,str_afib);
end
