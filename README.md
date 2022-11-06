# surfs_up

## Purpose of Analysis

The purpose of this analysis is to examine data from weather stations scattered across the island of Oahu with the end goal of using the data to determine the location of Surf and Shake, an ice cream and surf shop. Specifically we will be looking at temperature observations for the months of June and December to determine if there are suitable temperatures to maintain a surf and ice cream shop year round.

## Results of Analysis

### June Analysis

<img width="134" alt="june_desc_stats" src="https://user-images.githubusercontent.com/112291888/200152318-cdbeeeba-0a44-4822-ba3b-670fadb16762.png">

The above image is a screen grab of the descriptive statistics for the temperature observations in June. The average temperature is 75 degrees with the min and max being 64 and 85 degrees respectively. The low standard deviation and the mean being close to the 2nd percentile indicate that the data has little variation in its distribution. This indicates that temperatures are relatively consistent on the island, this makes sense as Oahu is not that far from the equator. These traits are definite pros for the location of a surf and ice cream shop.

### December Analysis

<img width="134" alt="dec_desc_stats" src="https://user-images.githubusercontent.com/112291888/200152338-8645f941-4c1a-4aac-8a1a-8c44a47927f6.png">

Shown above is a table of the summary statistics for the December temperature observations. With just over 1,500 observations the mean temperature is 71 degrees with the min and max temperatures being 56 and 83. The min temperature is only 8 degrees lower than in June and the max is also only slightly decreased at 2 degrees lower then the June max of 85. The distribution of the data points is also relatively narrow for December, with only a marginal difference between the mean temperature and the 2nd percentile of the data. The data indicates that there is not much of a difference between the summer and winter highs and lows for temperature which means that Oahu would be a suitable location for a surf and ice cream shop.

## Summary of Anlysis

The overall analysis of the data is that Oahu would be a suitable location for a surf shop that also sells ice cream. Based on the data analyzed, there are sufficiently warm temperatures for the business to be profitable.

To be sure that Oahu is the best location there are two additioal queries that we recommend should be run to verify that the weather is sufficient for a surf and ice cream shop. 1. We recommend that an additional query be run to determine the summary statistics for rainfall during all months of the year, we would also like to recommend broadening the queries of summary statistics of temperature observations for all months of the year and not just one month in summer and one month in early winter. 2. We would also recommend that determining the average weather patterns by station would be more informative to determining the best location for the surf shop. We would also like to recommend counting the number of observations that each station provides, this would give additional information indicating active stations and inactive ones as well as which station provides the most accurate and descriptive data. 
