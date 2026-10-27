# Goozman-Woock-Chu

Team Name: We Didn't Start the Fire

Members: Daisy Chu, Lowell Woock, Josh Goozman

Research Question: How does the occurence of prescribed fires affect the prevalence of invasive species across the state of California?
We aim to determine how prescribed fires affect the presence and population of invasive plant species

Audience: Environmental land managers



Data Dictionary:
​
Prescribed Fire Data(CAL FIRE):
   Each row represents one prescribed fire in the state of California
​
Year: calendar year the prescribed burn took place | Units: date (YYYY)
agency: name of the protection agency that conducted the burn. | Units: agency code text
treatment_name: Name of the prescribed burn | Units: text
treatment_type: type of prescribed burn according to the following:
   1 - Broadcast Burn
   2 - Fire Use
   3 - Hand Pile Burn
   4 - Jackpot Burn
   5 - Machine Pile Burn
| Unit: value from 1-5
start_date: Start date of fire | Units: date (YYYY-MM-DD)
end_date: End date of fire | Units: date (YYYY-MM-DD)
acres_treated: Number of treated acres by the prescribed fire | Units: number
gis_acres_treated: Number of treated acres calculated in GIS | Units: number
Shape_Length: Perimeter of fire polygon in GIS | Units: meters
Shape_Area: Area of fire polygon in GIS | Units: square meters
geometry: Spatially defined geometric polygon of the prescribed fire burn area | Units: multipolygon file
​
Invasive Flora Species Data(iNaturalist):
   Each row represents one observation of an invasive species on iNaturalist in the state of California.
​
id: unique identification number for each observation | Units: text
observation_date: calendar date when the species was observed | Units: Date (YYYY-MM-DD)
location: location described by the iNaturalist observer| Units: text
scientific_name: scientific name of the observed taxon in iNaturalist | Units: text
common_name: common name of the observed taxon in iNaturalist | Units: text
geometry: Observation location from the publicly visible latitude and longitude | Units: points
