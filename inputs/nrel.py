# For residential and commercial
from sg2t.io.loadshapes.nrel.api import API
from sg2t.io.loadshapes.nrel.naming import BUILDING_TYPES, HOME_TYPES, CLIMATE_ZONES, CLIMATE_ZONES_IECC, NREL_COL_MAPPING


sector_vars = {
    "Resstock" : {
        "appliance name" : ["Space Heater", "Water Heater", "Clothes Dryer", "Oven"],
        "appliance cols" : {
            "Space Heater" : ["Fuel Oil Heating", "Natural Gas Heating", "Propane Heating"] ,
            "Water Heater" : ["Fuel Oil Hot Water","Natural Gas Hot Water","Propane Hot Water"],
            "Clothes Dryer" : ["Natural Gas Clothes Dryer", "Propane Clothes Dryer"],
            "Oven" : ["Natural Gas Oven", "Propane Oven"]
        },
        "type" : HOME_TYPES,
        "view options" : ['State', 'Climate Zone - Building America','Climate Zone - IECC'],
        "climate zones ba" : CLIMATE_ZONES,
        "climate zones iecc" : CLIMATE_ZONES_IECC
    },

    "Comstock": {
        "appliance name": ["Space Heater", "Water Heater", "Cooling", "Interior Equipment"],
        "appliance cols": {
            "Space Heater": ["Other Fuel Heating", "Natural Gas Heating"],
            "Water Heater": ["Fuel Oil Water Heating", "Natural Gas Water Heating"],
            "Cooling": ["Other Fuel Cooling", "Natural Gas Cooling"],
            "Interior Equipment": ["Other Fuel Interior Equipment", "Natural Gas Interior Equipment"]
        },
        "type" : BUILDING_TYPES,
        "view options" : ['State', 'Climate Zone - Building America','Climate Zone - IECC'],
        "climate zones ba": CLIMATE_ZONES,
        "climate zones iecc": CLIMATE_ZONES_IECC

    }
}


def _format_columns_df(df):
    # rename columns using NREL_COL_MAPPING and drop the rest of the columns
    df.rename(columns=NREL_COL_MAPPING, inplace=True)
    df = df[df.columns.intersection([*NREL_COL_MAPPING.values()])]
    return df


def nrel_get_data(sector, view, by, type):

    api = API()

    if sector == "Resstock":
        if view == "State":
            df = api.get_data_resstock_by_state(by, type)
        elif view == "Climate Zone - Building America":
            df = api.get_data_resstock_by_climatezone(by, type)
        elif view == "Climate Zone - IECC":
            df = api.get_data_resstock_by_climatezone_iecc(by, type)

    elif sector == "Comstock":
        if view == "State":
            df = api.get_data_comstock_by_state(by, type)
        elif view == "Climate Zone - Building America":
            df = api.get_data_comstock_by_climatezone(by, type)
        elif view == "Climate Zone - IECC":
            df = api.get_data_comstock_by_climatezone_iecc(by, type)
    # except HTTPError:
    #     raise

    df = _format_columns_df(df)
    return df[:-1]