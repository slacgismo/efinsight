import json

states = [ "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
           "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME",
           "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
           "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX",
           "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

with open("inputs/counties.json") as f:
    counties = json.load(f)