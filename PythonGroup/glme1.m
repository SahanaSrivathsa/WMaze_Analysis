
m1 = csvread('../Responses_oxygen.csv');
  
T1 = array2table(m1','VariableNames',{'a','b','c','d','e','f','g','h'});
T1.trial = [1:887]';
T1.drug = repmat(0, 887, 1);

S1 = stack(T1,{'a','b','c','d','e','f','g','h'});
S1.Properties.VariableNames = {'trial','drug','id','response'}  ; 

m2 = csvread('../Responses_sevo.csv');
  
T2 = array2table(m2','VariableNames',{'a','b','c','d','e','f','g','h'});
T2.trial = [1:887]';
T2.drug = repmat(1, 887, 1);

S2 = stack(T2,{'a','b','c','d','e','f','g','h'});
S2.Properties.VariableNames ={'trial','drug','id','response'}  ;
S = [S1;S2];

S.drug = categorical(S.drug);

glme = fitglme(S,...
'response ~  1 + trial*drug + (1|id)', ...
'Distribution','Binomial','FitMethod','Laplace')

FEglme = fitglme(S,...
'response ~  1 + trial*drug', ...
'Distribution','Binomial','FitMethod','Laplace')

results = compare(FEglme,glme,'CheckNesting',true)

[psi,dispersion,stats] = covarianceParameters(glme);

stats{1}

% figure(1)
% mufit = fitted(FEglme);
% scatter(S.trial,mufit)
% title('Observed Values versus Fitted Values')
% xlabel('Fitted Values')
% ylabel('Observed Values')
% 
% figure(2)
% plotResiduals(glme,'histogram','ResidualType','Pearson')

% trials= S.trial
% drugs = double(S.drug)
% 
% means  = -0.31006 + 0.0018111*trials + 0.19578*drugs;
% std    = (-0.31006 + .38643)/1.96;
% 
% ps=[]
% for i= 1:length(means)
%     xs   = normrnd(means(i),std, 100,1)
%     ps   = exp(xs)./(1.0+exp(xs))
%     sortps = 
% 
% % mdl = fitglm(S.trial, [S.response ones(height(S),1)], ...
% %     'linear','Distribution','binomial','link','logit')
% % 
% % pltSlice(mdl)






