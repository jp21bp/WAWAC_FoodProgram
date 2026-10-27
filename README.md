# Table of Contents
1. [Project Background](#project-background)
2. [Insights And Recommendations](#insights-and-recommendations)
    * [1600-1700 hours has peak visitors](#1600-1700-hours-has-peak-visitors)
    * [Vistors are non-frecuent](#vistors-are-non-frecuent)
    * [Adults and Youth are the most assisted](#adults-and-youth-are-the-most-assisted)
    * [Women are the majority of visitors](#women-are-the-majority-of-visitors)
3. [KPIs](#kpis)
    * [Number of People fed](#number-of-people-fed)
    * [Zipcodes reaches](#zipcodes-reached)
    * [New Visitors](#new-visitors)

## Project Background

WAWAC is analyzing the efectiveness of their food drive program through the lens of their visitors and distributions. The following were metrics within the dataset:

* Number of monthly/hourly visitors
* New visitors per month
* Recurring visitors
* Household size
* Age populations served
* Gender distribution
* Zipcode distribution

![Visitors per Zipcode](./Images/VisitorsPerZipcode.png)


The following metrics were not available in the dataset:
* Pounds of food delivered
* Country of origin
* Leftover food


<br><br>

## Insights and Recommendations
### 1600-1700 hours has peak visitors
Considering that the food drives happen the first friday of the month, it is no surprise that a majority of visitors come during the afternoon hours, after the workday is over. The following insights are revealed:

* **Peak hours**: Occur between 1600-1700 hours, with approximately 30 visitors during that hour.
* **Anomalous January**: Jauary has received twice the number of visitors during the peak hours, but had the fewest visitors in most of the other hours.
* **70 visitors during 1500 - 1800**: the majority of visitors come during these three hours.

##### Recommendation
To increase efectiveness, it would be best to redistribute personel to focus on the food drive during 1500-1800 while other hours can be used as needed by the organization. This recommendation **depends on the already existing number of personel for the food drive**. 

![Visitors Per Hour](./Images/VisitorsPerHour.png)


<br><br>

### Vistors are non-frecuent
Food drives provide assitance during troubling moment, which is specific for each family. The number of visitors fluxuates in the following way:

* **Non-recurring visitors**: There is a decreasing number of new visitors, but the number of monthly visitors stays approximately consistent. This implies that visitors only come a few times and recurring visitors are rare.

* **Different needs per zipodes**: The average household size in all zipcodes is approximately the same, but 98204 consistently has the most number of visitors. It is possible that 98204 contains more families in need but may be discoraged due to distance.

* **Seasonal trends**: Considering the ups and downs of the data, there seems to be a seasonal trend to the number of monthly visitors. More data is needed in order to pinpoint the trend.

##### Recommendation
To increase effectiveness, it is recommend to become closer to families of 98204 and 98087 to assess the community needs. Other zipcodes would also need to be considered in order to provide a reference point for the data. It is possible that a food drive in 98204 **may increase WAWAC's food drive awareness and impact**.


![Zipcodes per month](./Images/ZipcodesPerMonth.png)

<br><br>

### Adults and Youth are the most assisted
Considering that a person has to come collect the food, children under the age of 18 cannot be the primary point of contact. Additionally, seniors are people over the age of 65, which means that adults between 18-65 is the most common point of contact. The following trends are noted:

* **Adults are the majority assisted**: Adults and youth tend to be the most common age populations marked in the dataset, followed by seniors and lastly by babies.

* **Seasonality**: Similar to previous graphs, there seems to be a seasonality to the age populations which are helped. However, more data is needed to assess its validity.

* **Seniors**: Although seniors are not the largest group, they are a good portion of the group and may benefit from other programs.

##### Recommendation
In order to increase the effectiveness in community impact, it'll be beneficial to offer senior programs (whether internal or external) during the food drive pickups. 

![Age Population Distribution](./Images/AgePopulationDistribution.png)

<br><br>


### Women are the majority of visitors

The gender distribution hourly distribution follows a similar trend as the hourly distribution, where almost every hour has more women than men visitors

![Gender Per Hour](./Images/GenderPerHour.png)

On a monthly distribution, the early part of the year sees more men visitors but the latter is superceeded by women. 

![Gender Per Month](./Images/GenderPerMonth.png)


<br><br>

## KPIs

### Number of People fed
$$
\sum_{\text{\{all visitors\}}} \sum_{\text{\{all populations\}}} IndividualsPerCategory
$$

### Zipcodes reached

Unique zipcodes in the data

### New Visitors

Unique((Visitors in Previous month) - (visitors in current month))
