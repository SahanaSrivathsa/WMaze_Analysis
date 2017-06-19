
load groupdata_bytrial
load groupdata_bysession

mat_oxy_N = NaN*ones(200,8)
mat_oxy_n = NaN*ones(200,8)


for animals = 1:8
    an  = animals_oxygen(animals)
    [animals an]
    dat = bysession(:,:,an)
    mat_oxy_N(1:length(dat),animals) = dat(:,1)
    mat_oxy_n(1:length(dat),animals) = dat(:,2)
end    

mat_sev_N = NaN*ones(200,8)
mat_sev_n = NaN*ones(200,8)


for animals = 1:8
    an  = animals_sevo(animals)
    [animals an]
    dat = bysession(:,:,an)
    mat_sev_N(1:length(dat),animals) = dat(:,1)
    mat_sev_n(1:length(dat),animals) = dat(:,2)
end

csvwrite('oxyg_denom.csv' ,mat_oxy_N )
csvwrite('oxyg_num.csv' ,mat_oxy_n )
csvwrite('sevo_denom.csv' ,mat_sev_N )
csvwrite('sevo_num.csv' ,mat_sev_n )