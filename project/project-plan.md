# Project Plan

## Title
Assessing Life Expectancy and Healthcare Access in the Americas: A Comparative Analysis of Brazil and the USA

## Main Question
Does healthcare access impact life expectancy in the Americas, specifically between the USA and Brazil?

## Description
Healthcare access is a critical pillar in shaping health outcomes, such as life expectancy, which is a key measure of public health in societies.  This project analyzes the impact of healthcare access on life expectancy in the Americas, focusing on a comparison between the USA and Brazil. Statistical analysis and visualization techniques are used on the tabular data to examine different factors like immunization rates, density of doctors and nurses, and the Universal Health Coverage (UHC) index.
This analysis aims to reveal patterns that connect healthcare access with life expectancy outcomes.  The results can provide valuable insights into the disparities between two healthcare systems and the influence of public health in different geographic contexts. 

## Data Sources
### Datasource1: World Health Organization (WHO)
The metadata URL is shared across all sheets. 
* Metadata URL: https://data.who.int/countries/840
* Description: The World Health Organization is a specialized agency of the United Nations responsible for international public health. It is headquartered in Geneva, Switzerland, and has six regional offices and 150 field offices worldwide.
* License Copyright: [CC BY-NC-SA 3.0 IGO licence](https://www.who.int/about/policies/publishing/copyright)


#### Sheet 1
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%2790E2E48WHOSIS_000001%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20AMOUNT_N&$format=csv
* Data Type: CSV
* Data Information: Life expectancy at birth
* Sheet Description: The average number of years that a newborn could expect to live.

#### Sheet 2
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27C64284DWHOSIS_000002%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20AMOUNT_N&$format=csv
* Data Type: CSV
* Data Information: Healthy life expectancy (HALE) at birth
* Sheet Description: The average number of years that a person can expect to live in “full health” from birth.


#### Sheet 3
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27C288D13MDG_0000000020%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20RATE_PER_100000_N,%20RATE_PER_100000_NL,%20RATE_PER_100000_NU&$format=csv
* Data Type: CSV
* Data Information: People living with tuberculosis (TB).
* Sheet Description: Number of TB cases per year per 100,000 population.


#### Sheet 4
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%271F96863NCDMORT3070%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20RATE_PER_100_N,%20RATE_PER_100_NL,%20RATE_PER_100_NU&$format=csv
* Data Type: CSV
* Data Information: Probability of dying from non-communicable diseases
* Sheet Description: Percentage of 30-year-old people who would die before their 70th birthday from non-communicable diseases.


#### Sheet 5
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27D6176E2RS_198%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20RATE_PER_100000_N&$format=csv
* Data Type: CSV
* Data Information: Road traffic deaths
* Sheet Description: Number of road traffic deaths per 100 000 population



#### Sheet 6
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%2716BBF41SDGSUICIDE%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20DIM_AGE,%20RATE_PER_100000_N,%20RATE_PER_100000_NL,%20RATE_PER_100000_NU&$format=csv
* Data Type: CSV
* Data Information: Suicide deaths
* Sheet Description: Number of suicide deaths in a given year




#### Sheet 7
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27608DE39NCD_HYP_PREVALENCE_A%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20RATE_PER_100_N,%20RATE_PER_100_NL,%20RATE_PER_100_NU&$format=csv
* Data Type: CSV
* Data Information: Prevalence of hypertension
* Sheet Description: Percentage of adults (30-79) with hypertnesion



#### Sheet 8
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27BEFA58BNCD_BMI_30A%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20DIM_AGE,%20RATE_PER_100_N,%20RATE_PER_100_NL,%20RATE_PER_100_NU&$format=csv
* Data Type: CSV
* Data Information: Adult obesity
* Sheet Description: Percentage of adults aged 18+ years with a body mass index (BMI) of 30 kg/m2 or higher

#### Sheet 10
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%2775DDA77M_Est_tob_curr_std%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20PERCENT_POP_N,%20PERCENT_POP_NL,%20PERCENT_POP_NU&$format=csv
* Data Type: CSV
* Data Information: Tobacco use
* Sheet Description: WHO estimate of current tobacco use prevalence among persons 15 years and older % (age-standardized) (SDG 3.a.1)


#### Sheet 11
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27EE6F72ASA_0000001688%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_SEX,%20RATE_PER_CAPITA_N,%20RATE_PER_CAPITA_NL,%20RATE_PER_CAPITA_NU&$format=csv
* Data Type: CSV
* Data Information: Alcohol consumption
* Sheet Description: Amount of alcohol consumed per adult (15+ years) over a calendar year, in litres of pure alcohol


#### Sheet 12
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%2712EE54AWSH_SANITATION_SAFELY_MANAGED%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_DEG_URB,%20PERCENT_POP_N&$format=csv
* Data Type: CSV
* Data Information: Safely managed sanitation
* Sheet Description: Percentage of population that have access to safely managed, improved sanitation facilities that are not shared with other households


#### Sheet 13
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27F810947SDGPM25%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20DIM_DEG_URB,%20RATE_N,%20RATE_NL,%20RATE_NU&$format=csv
* Data Type: CSV
* Data Information: Fine particulate matter
* Sheet Description: Annual mean PM2.5 concentration in urban areas


#### Sheet 14
* Data URL: UHC index score
* Data Type: CSV
* Data Information: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%279A706FDUHC_INDEX_REPORTED%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20INDEX_N&$format=csv
* Sheet Description: Coverage of essential health services as expressed as the average score of 14 tracer indicators of health 

#### Sheet 15
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%271772666MDG_0000000025%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20RATE_PER_100_N&$format=csv
* Data Type: CSV
* Data Information: Births attended by skilled health personnel
* Sheet Description: Percentage of births attended by skilled health personnel

#### Sheet 16
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27F8E084CWHS4_100%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20RATE_PER_100_N&$format=csv
* Data Type: CSV
* Data Information: DTP3 immunization
* Sheet Description:Percentage of one-year-olds who have received three doses of the combined diphtheria, tetanus toxoid and pertussis vaccine (DTP3) in a given year.

#### Sheet 16
* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%27BB4567BMCV2%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20RATE_PER_100_N&$format=csv
* Data Type: CSV
* Data Information: MCV2 immunization
* Sheet Description: Percentage of children who received two doses of measles containing vaccine (MCV2) by the locally recommended age

#### Sheet 17

* Data URL: https://xmart-api-public.who.int/DATA_/RELAY_WHS?$filter=IND_ID%20eq%20%272D6FBE4SDGNTDTREATMENT%27&$select=IND_ID,%20IND_CODE,%20IND_UUID,%20IND_PER_CODE,%20DIM_TIME,%20DIM_TIME_TYPE,%20DIM_GEO_CODE_M49,%20DIM_GEO_CODE_TYPE,%20DIM_PUBLISH_STATE_CODE,%20IND_NAME,%20GEO_NAME_SHORT,%20COUNT_N&$format=csv
* Data Type: CSV
* Data Information: Interventions against NTDs
* Sheet Description: Number of people requiring treatment and care for any neglected tropical diseases (NTDs)


### Datasource 2: World Bank Group
* Description: The World Bank is an international financial institution that provides loans and grants to the governments of low- and middle-income countries for the purposes of economic development.
* License Copyright: [Creative Commons Attribution 4.0 International license (CC-BY 4.0)](https://datacatalog.worldbank.org/public-licenses)


#### Sheet 1
* Meta URL: https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=BR
* Data URL: https://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv
* Data Type: CSV
* Data Information: Life expectancy at birth
* Sheet Description: Number of people requiring treatment and care for any neglected tropical diseases (NTDs)






## Work Packages

