# Goozman-Woock-Chu

Team Name: We Didn't Start the Fire

Members: Daisy Chu, Lowell Woock, Josh Goozman

Research Question: How does the occurence of prescribed fires affect the prevalence of invasive species across the state of California?
We aim to determine how prescribed fires affect the presence and population of invasive plant species

Audience: Environmental land managers



Data Dictionary:

Prescribed Fire Data:
    Each row represents one prescribed fire in the state of California

year: Year in which the prescribed burn occurred
agency: Name of protection agency that conducted the burn
treatment_name: Name of the prescribed burn
treatment_type: type of prescribed burn according to the following:
    1 - Broadcast Burn
    2 - Fire Use
    3 - Hand Pile Burn
    4 - Jackpot Burn
    5 - Machine Pile Burn
start_date: Start date of fire
end_date: End date of fire
acres_treated: Number of treated acres by the prescribed fire
gis_acres_treated: Number of treated acres calculated in GIS
Shape_Length: Perimeter of fire polygon in GIS
Shape_Area: Area of fire polygon in GIS
fire_polygon: Spatially defined geometric polygon of the prescribed fire burn area

iNaturalist California Invasive Species Data: 
iNaturalist Observation ID: id
Universally Unique Identifiers: uuid 
Species Observation Date String: observed_on_string
Species Observation Date: Observed_on
iNaturalist Observation Creation Date: created_at
Most Recent Update to Observation Date: updated_at
Observation's Accuracy, Completeness, And Suitability For Sharing With Data Partner: quality_grade
License & Copyright Ownership: license
iNaturalist Observation URL Link: url
iNaturalist Image URL Link: Image_url
iNaturalist Audio File URL: Sound_url
Tags Users Add For Their Personal Identification Notes: Tag_list
Description Users Add To Their iNaturalist Observation: Description
How Many Users Identifications Support The Taxonomic Classification Of That Specific Observation: Num_identification_agreements
How Many Users Identifications Oppose The Taxonomic Classification Of That Specific Observation: Num_identification_disagreements
Status of iNaturalist Observation based on if the observation is naturally occurring or found there because of humans: Captive_cultivated
iNaturalist OAuth Application ID: Oauth_application_id
Name of Observation Location (City, State, Country): Place_guess
iNaturalist Observation Latitude coordinate: latitude
iNaturalist Observation Longitude coordinate: longitude
Citizen’s Guess at Species Identification: Species_guess
Scientific Name of Species: Scientific_name
Common Name of Species: Common_name
Most Distinct Taxonomic Identifier of the Species: Iconic_taxon_name
Taxonomic ID: taxon_id