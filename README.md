# StatisticsForDataScience_codes



### 1.  Central Tendency
For missing value imputation or to understand the data it is often required to find out the central tendency of the data. There are several ways to find out the central tendency. Those are namely, 
* Mean
* Median
* Mode

### 2.  Data Spread
To find out the spread of data, we have to rely on the variance or the standard deviation. Variance has some limitation in the calculation process as it uses the square term. Standard deviation rules out the problem because it is the square root of the variance. In this part of the code, i have done a practice on
* Variance
* Standard Deviation
* Range
* Percentile
* IQR(Inter Quartile Range)

### 3.  Hypothesis Test - Part 1
In this part, I have practiced the hypothesis testing using P value and T test/Z value. Hypotheis testing is necessary to find out the credibility of an assumption. It helps to figure out if the made assumption is accepted based on the confidence level or it need to be revised.

### 4. Finding outliers Using Z-Score and IQR(InterQuartile Range)

### 5. Normalization vs Standardization
In this part, I have practiced the normalization and standardization. By definition, normalization is a process to convert the values or magnitude of the features between 0 and 1. Standardization is a process to convert any distrubution into a standard normal distribution (SND) where the mean is 0 and standard deviation is 1.

Now, when to use Normalization and when to use Standardization?
  Normalization is basically required in deep learning techniques such as CNN, ANN etc. Lets assume we are using Image data for CNN. All the pixels of the data are between 0 to 255. Calculation this huge range for every pixel will consume time and wont be efficient. This is why for a situation like this, normalization is used. 
  
  Standardization is required to calculate within a certain range. Most of the supervised machine learning algorithms such as bagging, boosting, gradient descent etc use standardization process.
  
To Be Continued.....
