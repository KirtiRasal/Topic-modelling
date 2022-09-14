from pathlib import Path
import pandas as pd
import os


def all_year_docs_vis(legal_docs_df):

    all_year_df = pd.DataFrame({'count' : legal_docs_df.groupby( [ "Year"] ).size()}).reset_index()
    all_year_df.set_index('Year', inplace=True)
    all_year_docs_fig = all_year_df['count'].plot().get_figure()

    return all_year_docs_fig


def renewable_energy__vis(legal_docs_df):

    mylist = ['renewable energy', 'wind', 'solar','geothermal', 'biomass','hydropower', 'biofuel','green economy',
              'reduction of gas emissions','energy efficiency','security of supply','price of energy', 'energy saving','air quality',
               'renewable resources','environmental cooperation', 'adaptation to climate change','energy diversification',
               'sustainable mobility','sustainable development', 'peaceful use of energy','sustainable development']
    pattern = '|'.join(mylist)

    renewable_energy_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern) == True]

    # dropping duplicate values
    renewable_energy_df.drop_duplicates(keep=False, inplace=True)

    renewable_energy_df.reset_index()

    ren_eng_df = pd.DataFrame({'count' : renewable_energy_df.groupby( [ "Year"] ).size()}).reset_index()

    ren_eng_df.set_index('Year', inplace=True)

    renewable_fig = ren_eng_df['count'].plot(grid = True,title= 'Electricity Topic', ylabel='Frequency',legend=['topics']).get_figure()

    return renewable_fig


def electricity__vis(legal_docs_df):

    mylist0 = ['electricity', 'power plant', 'hydroelectric development','electrical energy', 'hydroelectric power']
    pattern0 = '|'.join(mylist0)

    elec_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern0) == True]

    # dropping duplicate values
    elec_df.drop_duplicates(keep=False, inplace=True)

    elec_df.reset_index()

    el_df = pd.DataFrame({'count' : elec_df.groupby( [ "Year"] ).size()}).reset_index()

    el_df.set_index('Year', inplace=True)

    electricity_fig = el_df['count'].plot(grid = True,title= 'Electricity Topic', ylabel='Frequency',legend=['topics']).get_figure()

    return electricity_fig

def energy_indus__vis(legal_docs_df):

    mylist1 = ['energy industry', 'energy conversion', 'energy-generating product','energy technology', 'fuel cell','fuel',
                'hard energy','gas','fossil fuel']
    pattern1 = '|'.join(mylist1)

    energy_indus_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern1) == True]

    # dropping duplicate values
    energy_indus_df.drop_duplicates(keep=False, inplace=True)

    energy_indus_df.reset_index()

    eng_ind_df = pd.DataFrame({'count' : energy_indus_df.groupby( [ "Year"] ).size()}).reset_index()

    eng_ind_df.set_index('Year', inplace=True)

    energy_industry_fig =  eng_ind_df['count'].plot(grid = True, title= 'Energy industry Topics', ylabel='Frequency',legend=['topics']).get_figure()

    return energy_industry_fig


def coal_mining__vis(legal_docs_df):

    mylist2 = ['mining industry', 'mineral prospecting', 'ore deposit','mining operation', 'mining production',
            'mining of ore','drilling','drilling equipment','mining extraction', 'mining product','ore processing',
            'non-metallic ore', 'asbestos', 'salt','phosphate', 'sulphur', 'precious stones', 'metallic ore', 'iron ore',
            'non-ferrous ore', 'bauxite', 'bituminous materials', 'earths and stones','coal industry', 'coalmining policy',
            'coal processing','coal by-products industry','coal','lignite','coke','coal mining']
    pattern2 = '|'.join(mylist2)

    coal_mining_indus_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern2) == True]

    # dropping duplicate values
    coal_mining_indus_df.drop_duplicates(keep=False, inplace=True)

    coal_mining_indus_df.reset_index()

    coalmining_ind_df = pd.DataFrame({'count' : coal_mining_indus_df.groupby( [ "Year"] ).size()}).reset_index()

    coalmining_ind_df.set_index('Year', inplace=True)

    coal_mining_fig = coalmining_ind_df['count'].plot(grid = True, title= 'Coal and Mining industry Topic', ylabel='Frequency',legend=['topics']).get_figure()

    return coal_mining_fig

def oil_indus__vis(legal_docs_df):

    mylist3 = ['oil industry', 'hydrocarbon', 'natural gas','gas industry', 'shale gas','petroleum ','crude oil','offshore oil','storage of hydro carbons',
            'offshore drilling','petroleum policy','petroleum exploration','extraction of oil','fracking','offshore oil structure','petroleum production',
            'oil technology','oil refining','oilfield','petrochemicals','petroleum product','heavy oil','mineral oil','butane','paraffin','fuel oil','propane gas',
            'motor fuel','petrol','lead-free petrol','diesel fuel','aviation fuel','marine fuel']
    pattern3 = '|'.join(mylist3)

    oil_indus_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern3) == True]

    # dropping duplicate values
    oil_indus_df.drop_duplicates(keep=False, inplace=True)

    oil_indus_df.reset_index()

    oil_ind_df = pd.DataFrame({'count' : oil_indus_df.groupby( [ "Year"] ).size()}).reset_index()

    oil_ind_df.set_index('Year', inplace=True)

    oil_indus_fig = oil_ind_df['count'].plot(grid = True, title= 'Oil industry Topics', ylabel='Frequency',legend=['topics']).get_figure()

    return oil_indus_fig

def nuclear_indus__vis(legal_docs_df):

    mylist4 = ['nuclear industry', 'nuclear policy', 'nuclear research','nuclear safety', 'radioactivity','radiation protection ','nuclear accident','nuclear technology',
            'nuclear fission','nuclear fusion','fuel reprocessing','reactor cooling system','nuclear chemistry','fuel enrichment','nuclear test','nuclear security',
            'nuclear power station','nuclear reactor','breeder reactor','nuclear energy','radioactive materials','plutonium','uranium','thorium','nuclear fuel','irradiated fuel']
    pattern4 = '|'.join(mylist4)

    nuclear_indus_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern4) == True]

    # dropping duplicate values
    nuclear_indus_df.drop_duplicates(keep=False, inplace=True)

    nuclear_indus_df.reset_index()

    nuc_ind_df = pd.DataFrame({'count' : nuclear_indus_df.groupby( [ "Year"] ).size()}).reset_index()

    nuc_ind_df.set_index('Year', inplace=True)

    nuclear_energy_fig = nuc_ind_df['count'].plot(grid = True, title= 'Nuclear Energy Topics', ylabel='Frequency',legend=['topics']).get_figure()

    return nuclear_energy_fig

def softenergy_vis(legal_docs_df):

    mylist5 = ['soft energy', 'biorenergy', 'biogas','wind energy', 'offshore wind energy production','geothermal production','hydraulic energy',
            'renewable energy','solar energy', 'solar energy end-use applications','photovoltaic cell','solar architecture','solar collector','thermal energy',
            'marine energy','wave energy','tidal energy']
    pattern5 = '|'.join(mylist5)

    soft_energy_df = legal_docs_df[legal_docs_df.Eurovoc_Descriptor.str.contains(pattern5) == True]

    # dropping duplicate values
    soft_energy_df.drop_duplicates(keep=False, inplace=True)

    soft_energy_df.reset_index()

    sft_eng_df = pd.DataFrame({'count' : soft_energy_df.groupby( [ "Year"] ).size()}).reset_index()

    sft_eng_df.set_index('Year', inplace=True)

    soft_energy = sft_eng_df['count'].plot(grid = True, title= 'Soft Energy Topics', ylabel='Frequency',legend=['topics']).get_figure()

    return soft_energy


def main():


    legal_docs_df = pd.read_json('original_data/data_files.json')

    legal_docs_df['Effective_date'] = legal_docs_df['Effective_date'].apply(lambda x: pd.Timestamp(x))

    legal_docs_df['Year'] = legal_docs_df['Effective_date'].dt.year

    #calling  all the function to create visualizations

    all_year_docs_vis(legal_docs_df).savefig('Graphs/all_year.png')

    renewable_energy__vis(legal_docs_df).savefig('Graphs/renewable.png')

    electricity__vis(legal_docs_df).savefig('Graphs/electricity.png')

    energy_indus__vis(legal_docs_df).savefig('Graphs/energy_industry.png')

    coal_mining__vis(legal_docs_df).savefig('Graphs/coal_mining.png')

    oil_indus__vis(legal_docs_df).savefig('Graphs/oil_industry.png')

    nuclear_indus__vis(legal_docs_df).savefig('Graphs/nuclear_industry.png')

    softenergy_vis(legal_docs_df).savefig('Graphs/soft_energy.png')



if __name__ == "__main__":
	main()

