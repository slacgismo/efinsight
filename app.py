import marimo

__generated_with = "0.1.64"
app = marimo.App(width="full")


@app.cell
def __(
    credits_view,
    data_view,
    electrification_view,
    loadshape_view,
    mo,
    report_view,
    results_view,
    sector_view,
):
    #
    # Main page
    #

    mo.vstack([mo.md("""# North American Electrification Loadshape Forecasting

    CAUTION: This is software is currently under development. Use of the output from this software is not recommended at this time.

    ---

    """),
        mo.tabs({
            "Introduction" : sector_view,
            "Potential" : electrification_view,
            "Loadshape" : loadshape_view,
            "Results" : results_view,
            "Data" : data_view,
            "Report" : report_view,
            "About" : credits_view,
        }),
        mo.md("""---

    ---

    *Copyright (C) 2023 Regents of the Leland Stanford Junior University*""")
    ])
    return


@app.cell
def __(
    credits_view,
    data_view,
    electrification_view,
    loadshape_view,
    mo,
    results_view,
    sector_view,
):
    report_view = mo.vstack([
        sector_view,
        electrification_view,
        loadshape_view,
        results_view,
        data_view,
        credits_view,
    ])
    return report_view,


@app.cell
def __(by, mo, sector, type, view):
    #
    # Sector view tab
    #
    sector_view = mo.md(
        f"""
    ## Introduction

    This tool performs loadshape forecasting for residential and commercial buildings using publicly available datasets. Building loadshapes are generated using NREL <a href="https://resstock.nrel.gov/" target="_blank">Resstock</a> and <a href="https://comstock.nrel.gov/" target="_blank">Comstock</a> data sets. An important assumption in electricity loadshape forecasts is the amount of natural gas consumption that will be converted to electric energy demand, which is expected to vary by region, sector, and subsector. 

    The first step in generating a loadshape forecast is to identify the region, sector, and subsector for which you want the loadshape forecast, as shown in Table 1.

    <table>
        <caption>Table 1: Scenario description</caption>
        <tr><th align=left>Select an aggregation region</th><td align=left>{view}{by}</td><td align=left>(HI and AK not available)</td></tr>
        <tr><th align=left>Select the load sector (e.g., residential, commercial)</th><td align=left>{sector}</td></tr>
        <tr><th align=left>Select the customer subsector (e.g., building type)</th><td align=left>{type}</td></tr>
    </table>

    Click on the **`Potential`** tab to develop the electrification potential.
    """
    )
    return sector_view,


@app.cell
def __(
    appliance_name,
    checkbox_eu1,
    checkbox_eu2,
    checkbox_eu3,
    checkbox_eu4,
    eu1_AR,
    eu1_year,
    eu2_AR,
    eu2_year,
    eu3_AR,
    eu3_year,
    eu4_AR,
    eu4_year,
    fig1,
    mo,
    start_year,
    target_year,
):
    #
    # Electrification potential view tab
    #

    electrification_view = mo.md(
        f"""
    ## Electrification Potential

    Now you can develop the total electrification potential over time based on technology adoption rates for each enduse. A technology adoption curve is used to model the technology adoption rates for end-uses. A sigmoid function gives a characteristic 'S' shape which tends to start slowly, then accelerates to a peak adoption rate at the peak year, and then declines as it approaches a steady turn-over rate. 

    The target year specifies the year when technology adoption reaches a steady state turn-over rate. The peak adoption year rate can be changed to adjust the shape of the technology adoption function. The default peak adoption rate is set to 50% at the year midway between target and current year. These options are specified in Table 2.

    Start year: {start_year}
    Target year: {target_year}

    <table>
      <caption>Table 2: End-use electrification edoption rate</caption>
      <tr>
        <th>End-use</th>
        <th>Enable</th>
        <th>Peak Year</th>
        <th>Peak Rate </th>
      </tr>
      <tr>
        <th>{appliance_name[0]}</th>
        <td>{checkbox_eu1}</td>
    """ +
    (f"""
        <td>{eu1_year} </td>
        <td>{eu1_AR}%  </td>
    """ if checkbox_eu1.value else "<td colspan=2>(na)</td>") +
    f"""
      </tr>
      <tr>
        <th>{appliance_name[1]}</th>
        <td>{checkbox_eu2}</td>
    """ +
    (f"""
        <td>{eu2_year} </td>
        <td>{eu2_AR}% </td>
    """ if checkbox_eu2.value else "<td colspan=2>(na)</td>") +
    f"""
      </tr>
      <tr>
        <th>{appliance_name[2]}</th>
        <td>{checkbox_eu3}</td>
    """ +
    (f"""
        <td>{eu3_year} </td>
        <td>{eu3_AR}% </td>
    """ if checkbox_eu3.value else "<td colspan=2>(na)</td>") +
    f"""
      </tr>
      <tr>
        <th>{appliance_name[3]}</th>
        <td>{checkbox_eu4}</td>
    """ +
    (f"""
        <td>{eu4_year} </td>
        <td>{eu4_AR}% </td>
      </tr>
    """ if checkbox_eu4.value else "<td colspan=2>(na)</td>") +
    f"""  
    </table>

    <center>

    {mo.as_html(fig1)} 
    Figure 1: Adoption curves for 95% end-use electrification by {target_year.value}


    </center>

    Click on the **`Loadshape`** tab to develop the composite load shape for any given year.
    """
    )
    return electrification_view,


@app.cell
def __(
    aggregation,
    by,
    by_month,
    day_type,
    fig2,
    mo,
    study_year,
    type,
    view_month,
):
    #
    # Loadshape view tab
    #

    loadshape_view = mo.md(
        f"""
    ## Loadshape Forecast

    The overall loadshape of {type.value} in {by.value} is generated by changing each affected enduse loadshape based on the load growth from electrification of the end-use accumulated up to that year. You can change the time of year for which the load shape is generated, as well as which day type and aggregation to use, as shown in Table 3.

    <table>
      <caption>Table 3: Loadshape forecast parameters</caption>
      <tr><th>Loadshape year</th><td>{study_year}</td></tr>
      <tr><th>Season</th><td>{view_month} {by_month}</td></tr>
      <tr><th>Daytype</th><td>{day_type}</td></tr>
      <tr><th>Aggregation</th><td>{aggregation}</td></tr>
    </table>

    <center>
        {mo.as_html(fig2)}
        Figure 2: Aggregated {type.value} loadshape for {study_year.value}
    </center>

    Click on the **`Results`** tab to see the overall results for this scenario.
    """
    )
    return loadshape_view,


@app.cell
def __(
    by,
    df,
    load_growth,
    mo,
    new_peak,
    new_peak_time,
    np,
    peak,
    peak_time,
    study_year,
    supply_peak,
    supply_peak_time,
    type,
):
    #
    # Results view
    #

    results_view = mo.md(f"""

    ## Loadshape Forecast Summary Results

    The result of the analysis suggests that the total new energy supply required to meet the load growth from electricifation of {type.value} in {by.value} is {np.round(df['New Supply'].values.sum()/1e9,1)} TWh.  A summary of the peak load impacts is shown in Table 4.

    <table style="width:50%">
      <caption>Table 4 - Peak load changes for {type.value} in {study_year.value}</caption>
      <tr>
        <th>Load</th>
        <th>Value</th>
        <th>Unit</th>
        <th>Time</th> 
      </tr>
      <tr>
        <th>Current Peak</th>
        <td>{np.round(peak[0],0)} </td>
        <td> MW </td>
        <td>{peak_time}</td>

      </tr>
      <tr>
        <th>New Peak</th>
        <td>{np.round(new_peak[0],0)} </td>
        <td>MW </td>
        <td>{new_peak_time} </td>
      </tr>
      <tr>
        <th>New Supply</th>
        <td>{np.round(supply_peak[0],0)} </td>
        <td>MW </td>
        <td>{supply_peak_time}</td>
      </tr>
      <tr>
        <th>Load Growth</th>
        <td>{np.round(load_growth,2)} </td>
        <td>% </td>
        <td></td>
      </tr>
    </table>

    Click on the **`Data`** tab to view and download the raw data.
    """)
    return results_view,


@app.cell
def __(df_agg, mo):
    #
    # Data view
    #

    data_view = mo.vstack([
        mo.md("## Loadshape data"),
        mo.ui.table(df_agg.round(2).set_index('hour'),pagination=False)],
    )
    return data_view,


@app.cell
def __(mo):
    credits_view = mo.md("""
    ## Acknowledgments

    This tool was developed by staff at <a href="https://slac.stanford.edu/" target="_blank">SLAC National Accelerator Laboratory</a> and graduate students at <a href="https://stanford.edu/">Stanford University</a>, which operates SLAC for the <a href="https://www.energy.gov/" target="_blank">US Department of Energy</a> under Contract No. DE-AC02-SF00515.

    This tool was implemented on <a href="https://docs.marimo.io/" target="_blank">Marimo</a>, developed under funding from the US Department of Energy's <a href="https://www.energy.gov/eere/solar/solar-energy-technologies-office" target="_blank">Solar Energy Technology Office</a> and the <a href="https://www.energy.gov/oe/advanced-grid-modeling" target="_blank">Office of Electricity's Advanced Grid Modeling program</a>.

    ## References

    1. Chassin, D.P., S.A. Miskovich, and M. Nijad, "North American Electrification Loadshape Forecasting Tool", SLAC National Accelerator Laboratory, November 2023, URL: <a href="https://github.com/slacgismo/sg2t/blob/main/examples/marimo_notebooks/loadshape_nrel_marimo.py" target="_blank">`https://github.com/slacgismo/sg2t/examples/marimo_notebooks/loadshape_nrel_marimo.py`</a>

    2. Nijad, M., S.A. Miskovich, and D.P. Chassin, "US Electrification Potential Impact on Electric Load Composition", SLAC National Accelerator Laboratory, March 2023, URL: <a href="https://github.com/slacgismo/sg2t/blob/develop/examples/marimo_notebooks/US_Electrification_Potential_Impact_on_Electric_Load_Composition%20(DRAFT).pdf" target="_blank">`https://github.com/slacgismo/sg2t/blob/develop/examples/marimo_notebooks/US_Electrification_Potential_Impact_on_Electric_Load_Composition%20(DRAFT).pdf`</a>
    """)
    return credits_view,


@app.cell
def __(API, NREL_COL_MAPPING, by, checkbox_run, sector, type, view):
    #
    # Column format for dataframes
    #

    def _format_columns_df(df):
         # rename columns using NREL_COL_MAPPING and drop the rest of the columns
        df.rename(columns=NREL_COL_MAPPING, inplace = True)
        df = df[df.columns.intersection([*NREL_COL_MAPPING.values()])]
        return df

    # Import annual energy data
    api = API()
    # try:
    if sector.value == 'Resstock' and checkbox_run.value == True:
        if view.value == 'state':
            df = api.get_data_resstock_by_state(by.value, type.value)
        elif view.value == 'climate zone - building America':
            df = api.get_data_resstock_by_climatezone(by.value, type.value)
        elif view.value == 'climate zone - iecc':
            df = api.get_data_resstock_by_climatezone_iecc(by.value, type.value)

    elif sector.value == 'Comstock' and checkbox_run.value == True:
        if view.value == 'state':
            df = api.get_data_comstock_by_state(by.value, type.value)
        elif view.value == 'climate zone - building America':
            df = api.get_data_comstock_by_climatezone(by.value, type.value)
        elif view.value == 'climate zone - iecc':
            df = api.get_data_comstock_by_climatezone_iecc(by.value, type.value)
    # except HTTPError:
    #     raise

    df = _format_columns_df(df)
    df = df[:-1]
    return api, df


@app.cell
def __(df, sector):
    # 
    # Calculation Step 1

    # Calculate the total annual non-electric energy use for the different end-uses

    if sector.value == 'Resstock':
        appliance_name = ["Space Heater", "Water Heater", "Clothes Dryer", "Oven"]
        eu1 = df[['Fuel Oil Heating', 'Natural Gas Heating', 'Propane Heating']].sum(axis=1)
        eu2 = df[['Fuel Oil Hot Water','Natural Gas Hot Water','Propane Hot Water']].sum(axis=1)
        eu3 = df[['Natural Gas Clothes Dryer', 'Propane Clothes Dryer']].sum(axis=1)
        eu4 = df[['Natural Gas Oven', 'Propane Oven']].sum(axis=1)

    elif sector.value == 'Comstock':
        appliance_name = ["Space Heater", "Water Heater", "Cooling", "Interior Equipment"]
        eu1 = df[['Other Fuel Heating', 'Natural Gas Heating']].sum(axis=1)
        eu2 = df[['Other Fuel Water Heating', 'Natural Gas Water Heating']].sum(axis=1)
        eu3 = df[['Other Fuel Cooling', 'Natural Gas Cooling']].sum(axis=1)
        eu4 = df[['Other Fuel Interior Equipment', 'Natural Gas Interior Equipment']].sum(axis=1)

    #----------------------------------------------------------------------------#
    appliance = [eu1, eu2, eu3, eu4]
    return appliance, appliance_name, eu1, eu2, eu3, eu4


@app.cell
def __(
    appliance,
    appliance_name,
    checkbox_eu1,
    checkbox_eu2,
    checkbox_eu3,
    checkbox_eu4,
    data_model_year,
    eu1_AR,
    eu1_year,
    eu2_AR,
    eu2_year,
    eu3_AR,
    eu3_year,
    eu4_AR,
    eu4_year,
    np,
    plt,
    start_year,
    target_year,
):
    #
    # Figure 1 - Electrification potential
    #

    def sigmoid(x, L, k, x0):
        return L / (1 + np.exp(-k*(x-x0)))

    # Generate x values
    x = np.linspace(start_year.value, target_year.value, 100)
    new_sup = np.zeros((len(x), 4))

    X0 = [eu1_year.value, eu2_year.value, eu3_year.value, eu4_year.value]
    K = [eu1_AR.value, eu2_AR.value, eu3_AR.value, eu4_AR.value]

    # applying arithmetic or geometric growth rate to achieve electrification
    for i in range(len(appliance)):
        # Initial and target value
        initial_value = appliance[i].sum()

        # Calculate parameters
        x0 = X0[i]
        k = K[i]/100  # adjust this to suit your needs

        new_sup[:,i] = sigmoid(x, 1, k, x0)
        new_sup[:,i] = (new_sup[:,i] - min(new_sup[:,i])) / (max(new_sup[:,i]) - min(new_sup[:,i])) 

        # If data_model_year > start_year, backpropagate data by appropriate growth amount to start at zero electrification at start_year
        if data_model_year > start_year.value and data_model_year in x:
            # Find growth amount at model year
            model_year_idx = list(x).index(data_model_year)
            model_year_supply_growth = new_sup[model_year_idx]
            # Adjust what appliance initial consumption is by the growth at model year
            initial_value /= model_year_supply_growth

        # Get new supply
        new_sup[:,i] = new_sup[:,i] * initial_value

    plt.figure(figsize=(7,5))

    if checkbox_eu1.value == True:
        plt.plot(x, new_sup[:,0]/1e9, color='tab:blue', label = f'{appliance_name[0]}')
        plt.axvline(x=X0[0],ls=':', color='tab:blue', label= f'Peak adoption year - {appliance_name[0]}')
    if checkbox_eu2.value == True:
        plt.plot(x, new_sup[:,1]/1e9, color='tab:orange', label = f'{appliance_name[1]}')
        plt.axvline(x=X0[1], ls=':', color='tab:orange', label= f'Peak adoption year - {appliance_name[1]}')
    if checkbox_eu3.value == True:
        plt.plot(x, new_sup[:,2]/1e9, color='tab:green', label = f'{appliance_name[2]}')
        plt.axvline(x=X0[2], ls=':', color='tab:green', label= f'Peak adoption year - {appliance_name[2]}')
    if checkbox_eu4.value == True:
        plt.plot(x, new_sup[:,3]/1e9,color='tab:red', label = f'{appliance_name[3]}')
        plt.axvline(x=X0[3], ls=':', color='tab:red', label= f'Peak adoption year - {appliance_name[3]}')


    # plt.axvline(x=X0[0], color='b', ls=':', label='Peak Adoption Year')
    plt.ylabel('New Supply (billion kWh)')
    plt.xlabel('year')
    plt.legend(loc=2, prop={'size': 6})
    plt.grid()

    fig1 = plt.gca()
    return (
        K,
        X0,
        fig1,
        i,
        initial_value,
        k,
        model_year_idx,
        model_year_supply_growth,
        new_sup,
        sigmoid,
        x,
        x0,
    )


@app.cell
def __(mo):
    #
    # Checkboxes for Figure 1
    #
    checkbox_eu1 = mo.ui.checkbox(True)
    checkbox_eu2 = mo.ui.checkbox(False)
    checkbox_eu3 = mo.ui.checkbox(False)
    checkbox_eu4 = mo.ui.checkbox(False)
    return checkbox_eu1, checkbox_eu2, checkbox_eu3, checkbox_eu4


@app.cell
def __(
    K,
    X0,
    appliance,
    data_model_year,
    df,
    elec_col,
    np,
    sigmoid,
    start_year,
    study_year,
    target_year,
):
    #
    # Calculation for the new supply for a given year
    #
    year = int(study_year.value)
    x1 = np.arange(start_year.value, target_year.value + 1, 1)

    # If study year is after target year, set it to target year, fully electrified
    if year > target_year.value:
        year = target_year.value
        year_idx = list(x1).index(target_year.value)

    if year in list(x1):
        year_idx = list(x1).index(year)

    elif year < list(x1)[0]:
        # Electrification has not started yet
        # Assume state is same as start year
        year = list(x1)[0]
        year_idx = 0

    new_sup_sum = []

    for ii, ap in enumerate(appliance):
        # Get new supply for all years
        new_sup1 = sigmoid(x1, 1, K[ii]/100, X0[ii])
        # Normalize sigmoid from 0 to 1
        new_sup1 = (new_sup1 - min(new_sup1)) / (max(new_sup1) - min(new_sup1))

        # If data_model_year > start_year, backpropagate data by appropriate growth amount to start at zero electrification at start_year
        if data_model_year > start_year.value and data_model_year in x1:
            # Find growth amount at model year
            model_year_idx_calc = list(x1).index(data_model_year)
            model_year_supply_growth_calc = new_sup1[model_year_idx_calc]
            # Adjust what appliance initial consumption is by the growth at model year
            ap /= model_year_supply_growth_calc

        elif data_model_year > target_year.value: # not in range of years, ie model data is fully electrified 
            raise("Not Implemented.")

        # For a given study year, retrieve the corresponding index
        new_sup1 = new_sup1[year_idx] * ap
        new_sup_sum.append(new_sup1.values)

    # Sum up the value for all appliances
    new_supply = np.asarray(new_sup_sum).transpose().sum(axis=1)

    df['New Supply'] = new_supply
    df['New Electricity Total'] = new_supply  + df[elec_col]
    return (
        ap,
        ii,
        model_year_idx_calc,
        model_year_supply_growth_calc,
        new_sup1,
        new_sup_sum,
        new_supply,
        x1,
        year,
        year_idx,
    )


@app.cell
def __():
    #
    # Total current electricity column key
    #

    elec_col = "Electricity Total"
    return elec_col,


@app.cell
def __(
    Timeseries,
    aggregation,
    by,
    day_type,
    df,
    elec_col,
    loadshape_analysis,
    mo,
    month_end,
    month_start,
    new_supply,
    np,
    pd,
    study_year,
    timezone,
):
    #
    # Aggregation loadshape
    #

    run_this = new_supply
    df_agg = Timeseries.timeseries_aggregate(df, aggregation.value, month_start, month_end, day_type.value)

    # Time zone adjusting
    shift = timezone.value
    df_old_values = df_agg[:-shift]
    df_agg = df_agg.shift(periods=shift)
    df_agg[shift:] = df_old_values.values

    df_agg['hour'] = pd.date_range("00:00", "23:45", freq="1H").hour
    # df_agg['minute'] = pd.date_range("00:00", "23:45", freq="1").minute
    df_agg['Load Growth'] = (df_agg['New Supply']/df_agg[elec_col]).values 

    t = np.linspace(0,24,len(df_agg))

    # Loadshape analysis
    peak, peak_time, new_peak, new_peak_time, load_growth, supply_peak, supply_peak_time = loadshape_analysis(df_agg)

    class SaveData:
        """
        This class determines what gets saved.
        """
        def __init__(self):
            # CSV name
            self.by_val = by.value
            self.yr = study_year.value
            # headers
            # TODO: add headers to CSV corresponding to query
            self.headers = []
            # TODO: add units to current columns headers as well

        def save_csv(self):
            df_agg.to_csv(f'sg2t_electrification_loadshapes_{self.by_val}_{self.yr}.csv', index=False)
            return self

    save_data = SaveData()

    save_to_csv = mo.ui.button(
        value=save_data,
        on_click=lambda save_data: save_data.save_csv(),
        label="Save to CSV",
    )
    return (
        SaveData,
        df_agg,
        df_old_values,
        load_growth,
        new_peak,
        new_peak_time,
        peak,
        peak_time,
        run_this,
        save_data,
        save_to_csv,
        shift,
        supply_peak,
        supply_peak_time,
        t,
    )


@app.cell
def __():
    #
    # Loadshape Analysis
    #

    def loadshape_analysis(df):

        # Current peak value and timing
        current_peak = df[df['Electricity Total'] == df['Electricity Total'].max()]
        val = current_peak['Electricity Total'].values/1e3 *(60/15)
        current_peak_time = str(current_peak.hour.values[0]) + ':00'

        # New peak value and timing
        new_peak = df[df['New Electricity Total'] == df['New Electricity Total'].max()]
        new_val = new_peak['New Electricity Total'].values/1e3 *(60/15)
        new_peak_time = str(new_peak.hour.values[0]) + ':00'
        load_growth = new_peak['Load Growth'].values[0]*100

        # Greatest New Supply value and timing
        new_supply_peak = df[df['New Supply'] == df['New Supply'].max()]
        supply_val = new_supply_peak['New Supply'].values/1e3 *(60/15)
        supply_peak_time = str(new_supply_peak.hour.values[0]) + ':00'

        return val, current_peak_time, new_val, new_peak_time, load_growth, supply_val, supply_peak_time
    return loadshape_analysis,


@app.cell
def __(BUILDING_TYPES, CLIMATE_ZONES, CLIMATE_ZONES_IECC, HOME_TYPES, mo):
    #
    # Dropdown for main dataframe
    #

    climate_zone = mo.ui.dropdown(CLIMATE_ZONES, value = CLIMATE_ZONES[0])
    climate_zone_iecc = mo.ui.dropdown(CLIMATE_ZONES_IECC, value = CLIMATE_ZONES_IECC[0])
    sector =  mo.ui.dropdown(['Resstock', 'Comstock'], value = 'Resstock')
    building_type = mo.ui.dropdown(BUILDING_TYPES, value = BUILDING_TYPES[1])
    home_type =  mo.ui.dropdown(HOME_TYPES, value = HOME_TYPES[1])
    states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
               'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
               'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
               'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
               'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    state = mo.ui.dropdown(states, value = 'CA')
    view =  mo.ui.dropdown(['state', 'climate zone - building America',
                            'climate zone - iecc'], value = 'state')
    checkbox_run = mo.ui.checkbox(True)
    return (
        building_type,
        checkbox_run,
        climate_zone,
        climate_zone_iecc,
        home_type,
        sector,
        state,
        states,
        view,
    )


@app.cell
def __(mo):
    #
    # Dropdown for electrification stuff
    #
    # What is the target year set for the state
    target_year = mo.ui.slider(2023, 2080, value=2045)
    #start_year = mo.ui.slider(2000, 2080, value=2023)
    data_model_year = 2018 # This is NOT a user setting. This is model specific, and for Restock and Comstock data used it's 2018.
    return data_model_year, target_year


@app.cell
def __(mo, target_year):
    # When did electrification measures begin in the state
    start_year = mo.ui.slider(2000, target_year.value-1, value=2023)
    return start_year,


@app.cell
def __(mo, start_year, target_year):
    # End-uses/appliances target years
    # Resstock: space heater, water heater, clothes dryer, cooking
    # Comstock: space heater, water heater, cooling, interior equipment
    eu1_year = mo.ui.number(2000,2100, value=int((target_year.value + start_year.value)/2))
    eu2_year = mo.ui.number(2000,2100, value=int((target_year.value + start_year.value)/2))
    eu3_year = mo.ui.number(2000,2100, value=int((target_year.value + start_year.value)/2))
    eu4_year = mo.ui.number(2000,2100, value=int((target_year.value + start_year.value)/2))

    AR_options = dict(start=5,stop=100,step=5,value=50)
    eu1_AR = mo.ui.number(**AR_options)
    eu2_AR = mo.ui.number(**AR_options)
    eu3_AR = mo.ui.number(**AR_options)
    eu4_AR = mo.ui.number(**AR_options)
    return (
        AR_options,
        eu1_AR,
        eu1_year,
        eu2_AR,
        eu2_year,
        eu3_AR,
        eu3_year,
        eu4_AR,
        eu4_year,
    )


@app.cell
def __(mo):
    #
    # Dropdown for aggregation parameters
    #

    timezone = mo.ui.dropdown({'EST':-3, 'EDT':-4,'CST':-3, 'CDT':-4, 'MST':-3, 'MDT':-4, 'PST':-3,'PDT':-4}, value = 'PST')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    month = mo.ui.dropdown(months, value = months[0])
    season = mo.ui.dropdown(['winter', 'spring', 'summer', 'fall'], value = 'winter')
    view_month = mo.ui.dropdown(['by month', 'by season', 'all-year'], value = 'by month')
    day_type = mo.ui.dropdown(['weekday', 'weekend'])
    aggregation = mo.ui.dropdown(['avg', 'sum'], value = 'avg')
    return (
        aggregation,
        day_type,
        month,
        months,
        season,
        timezone,
        view_month,
    )


@app.cell
def __(mo, start_year, target_year):
    study_year = mo.ui.slider(start_year.value, target_year.value)
    return study_year,


@app.cell
def __(
    building_type,
    climate_zone,
    climate_zone_iecc,
    home_type,
    sector,
    state,
    view,
):
    # 
    # Dropdown option dependency
    #
    if view.value == 'state':
        by = state
    elif view.value == 'climate zone - building America':
        by = climate_zone
    elif view.value == 'climate zone - iecc':
        by = climate_zone_iecc

    if sector.value == 'Resstock':
        type = home_type
    elif sector.value == 'Comstock':
        type = building_type
    return by, type


@app.cell
def __(month, season, view_month):
    #
    # Month dependency
    #
    if view_month.value == 'by month':
        by_month = month
    elif view_month.value == 'by season':
        by_month = season
    elif view_month.value == 'all-year':
        by_month = 'all-year'
    return by_month,


@app.cell
def __(by_month, calendar, view_month):
    if view_month.value == 'by month':
        month_start = list(calendar.month_name).index(by_month.value)
        month_end = month_start + 1
    elif view_month.value == 'by season':
        if by_month.value == 'winter':
            month_start = 1
            month_end = 3
        elif by_month.value == 'spring':
            month_start = 3
            month_end = 6
        elif by_month.value == 'summer':
            month_start = 6
            month_end = 9
        elif by_month.value == 'fall':
            month_start = 9
            month_end = 12
    elif view_month.value == 'all-year':
        month_start = 1
        month_end = 12
    return month_end, month_start


@app.cell
def __(df_agg, plt, t):
    # 
    # Figure 2 - Loadshape forecast
    #
    plt.plot(t, df_agg['Electricity Total']/1e3 *(60/15), label = 'Current Loadshape')
    plt.plot(t, df_agg['New Electricity Total']/1e3 *(60/15),
             label = 'Loadshape with Electrification')
    #plt.ylim(bottom=0)
    plt.xlabel('Hour (hr)')
    plt.ylabel('Power demand (MW)')
    plt.xticks([0,6,12,18,24])
    # plt.title(str(by.value) + ' ' + str(sector.value) + ' Loadshape with Electrification - ' + str(aggregation.value) + ' over ' + str(by_month.value))
    plt.grid(alpha=0.3)
    plt.legend()

    fig2 = plt.gca()
    return fig2,


@app.cell
def __():
    # 
    # Imported packages and modules
    #

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import marimo as mo
    import calendar
    import datetime as dt

    from sg2t.io.loadshapes.nrel.api import API
    from sg2t.io.loadshapes.nrel.naming import BUILDING_TYPES, HOME_TYPES, CLIMATE_ZONES, CLIMATE_ZONES_IECC, NREL_COL_MAPPING
    from sg2t.utils.timeseries import Timeseries
    return (
        API,
        BUILDING_TYPES,
        CLIMATE_ZONES,
        CLIMATE_ZONES_IECC,
        HOME_TYPES,
        NREL_COL_MAPPING,
        Timeseries,
        calendar,
        dt,
        mo,
        np,
        pd,
        plt,
    )


if __name__ == "__main__":
    app.run()
