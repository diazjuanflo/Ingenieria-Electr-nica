function featuresTable = extractFeatures(signals,labels)
% Extract time-domain and frequency-domain features using the Signal
% Processing Toolbox.

featuresTable = table();

% Calculate mean value feature
featuresTable.meanValue = cellfun(@mean,signals,'UniformOutput',true);

% Calculate median value feature
featuresTable.medianValue = cellfun(@median,signals,'UniformOutput',true);

% Calculate standard deviation feature
featuresTable.standardDeviation = cellfun(@std,signals,'UniformOutput',true);

% Calculate mean absolute deviation feature
featuresTable.meanAbsoluteDeviation = cellfun(@mad,signals,'UniformOutput',true);

% Calculate signal 25th percentile feature
featuresTable.quantile25 = cellfun(@(x) quantile(x,0.25),signals,'UniformOutput',true);

% Calculate signal 75th percentile feature
featuresTable.quantile75 = cellfun(@(x) quantile(x,0.75),signals,'UniformOutput',true);

% Calculate signal inter quartile range feature
featuresTable.signalIQR = cellfun(@iqr,signals,'UniformOutput',true);

% Calculate skewness of the signal values
featuresTable.sampleSkewness = cellfun(@skewness,signals,'UniformOutput',true);

% Calculate kurtosis of the signal values
featuresTable.sampleKurtosis = cellfun(@kurtosis,signals,'UniformOutput',true);

featuresTable.class = labels;
end

