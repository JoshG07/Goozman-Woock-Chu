# Goozman-Woock-Chu

This repo contains data and analysis for a course project analyzing the impacts of prescribed burns on invasive plant species presence across California.

Team Name: We Didn't Start the Fire

Members: Daisy Chu, Lowell Woock, Josh Goozman

## Project Summary
Using invasive species observation data and prescribed burn polygon data, we examined whether there was a difference in changes of species presence between prescribed burn areas and non-prescribed burn areas. We also examined if there was a difference in changes of species presence between single burn sites and repeated burn sites. Using two-sample t-tests, we found both of these analysis to be statistically insignificant, but noted that there was an increase in invasive species presence in prescribed burn ares and an average decrease in invasive species presence in non-prescribed burn areas. 

**Research Question:** How does the occurence of prescribed fires affect the prevalence of invasive species across the state of California?
We aim to determine how prescribed fires affect the presence and population of invasive plant species

**Audience of interest:** Environmental land managers


## Data Dictionary:
### Prescribed Fire Data(CAL FIRE):
Data source: [CalFire File Geodatabase](https://publish.data.ca.gov/dataset/california-fire-perimeters-all)

*Each row represents one prescribed fire in the state of California*
​
| Variable Name | Description | Units |
| --- | --- | --- |
| Year | Calendar year the prescribed burn took place | date (YYYY) |
| agency | Name of the protection agency that conducted the burn | agency code text |
| treatment_name | Name of the prescribed burn | text |
| treatment_type | Type of prescribed burn according to the following:<br>1 - Broadcast Burn<br>2 - Fire Use<br>3 - Hand Pile Burn<br>4 - Jackpot Burn<br>5 - Machine Pile Burn | value from 1-5 |
| start_date | Start date of fire | date (YYYY-MM-DD)|
| end_date | End date of fire | date (YYYY-MM-DD) |
| acres_treated | Number of treated acres by the prescribed fire | number |
| gis_acres_treated | Number of treated acres calculated in GIS | number |
| Shape_Length | Perimeter of fire polygon in GIS | meters |
| Shape_Area | Area of fire polygon in GIS | square meters |
| geometry | Spatially defined geometric polygon of the prescribed fire burn area | multipolygon file |


### Invasive Flora Species Data(Calflora):
*Each row represents one observation of an invasive species on Calflora in the state of California.*
​
| Variable Name | Description | Units |
| --- | --- | --- |
| id | Unique identification code for each observation | text |
| common_name | Common name of the observed taxon in Calflora | text |
| scientific_name | Scientific name of the observed taxon in Calflora | text |
| date | Calendar date when the species was observed | Date (YYYY-MM-DD) |
| latitude | Latitude at which the species was observed | Decimal Degrees |
| longitude | Longitude at which the species was observed | Decimal Degrees |
| geometry | Observation location from the publicly visible latitude and longitude | points |
| year | Calendar year when the species was observed | Date (YYYY) |



## Our Analysis:
1. Downloaded and cleaned Calflora and CAL Fire datasets by renaming and removing unnecessary columns, adding spatial features to the tables, checking for duplicate data, and removing missing values.
2. Performed a spatial join on the cleaned dataset and conducted a data quality audit, resulting in preliminary plots and tables of invasive species observations in prescribed burn areas.
3. Run linear regression analysis on invasive species presence from 2016 to 2026 for burned and unburned areas
4. Conducted a sample t-test on linear regression slopes assess if there is a difference between invasive species presence in prescribed burn areas and non-prescribed burn areas
5. Conducted a second two sample t-test on changes in invasive species observations before and after a single burn site and a repeated burn site
6. Developed specific plots and tables, such as a map of invasive species found before and after prescribed burns from our cleaned datasets to answer our research questions.
7. Generated a dashboard using the plots, tables, and figures from before while adding interactive components.

## Dashboard:
Access the published dahboard via this link: https://01a1c78c-4a9a-8566-e326-59a59e32fc52.share.connect.posit.cloud/ 
