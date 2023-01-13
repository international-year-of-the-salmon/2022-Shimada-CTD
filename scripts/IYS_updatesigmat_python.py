
import pandas as pd
import seawater as sw

df = pd.read_csv('original_data/CTD_sh2202l1_final_a1a5_1d93_e1c7.csv')

df

def sigmat_update(salinity=None,temperature=None):
    '''
    Changes to T or S (commonly to despike values or apply a salinity offset) will need corresponding changes in sigmat
    '''
    # calculate sigmaT at 0db gauge pressure (s, t, p=0)
    sigt = (sw.eos80.dens0(s=salinity, t=temperature) - 1000)
    
    return sigt

df['sigma_t_ch1'] = sigmat_update(df.sea_water_salinity_ch1, df.sea_water_temperature_ch1)
df['sigma_t_ch2'] = sigmat_update(df.sea_water_salinity_ch2, df.sea_water_temperature_ch2)

df.to_csv('original_data/CTD_sh2202l1_final_a1a5_1d93_e1c7.updated.csv')