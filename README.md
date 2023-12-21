Funding of Agricultural projects by the Inter-American Development Bank – Assessing product water intensity and per-country water scarcity.


Table of Contents

1.	Introduction
2.	Our Dataset
3.	Questions
4.	Conclusion
	


Introduction

In our project, we posited a scenario in which a list of countries (Brazil, Colombia, Costa Rica and Mexico) has come to the bank in order to receive funding for developing agricultural projects. These projects must be directed towards cash-generating crops (in our case, nuts, soybean oil, palm oil, coffee, dark chocolate, beef, pork, lamb and cheese). The bank has come to us to advise which projects should be rejected based on the overall environmental impact of the given products, emphasizing water intensity, and linking it with each country’s water stress levels. 

Our Dataset
We used 2 datasets, which we extracted from one source, ultimately. Firstly, we found a dataset using www.kaggle.com, which contained information regarding a list of raw food products and a set of environmental impact markers, such as the carbon intensity of the products’ lifecycle, nitrogen leaching into the environment per kilogram, water used per kilogram, land use change, among others. 
We considered that this dataset by itself could not be used to answer meaningfully to any well posited question, so we checked what the source of the dataset was, which lead us to the website www.ourworldindata.org. Once there, we identified a second dataset containing information about the evolution of water-scarcity (measured as the rate between freshwater reserves and freshwater extraction) over number of years, for every country in the world. 

Both datasets were relatively clean, meaning they initially had no missing values, although we decided to change some column names to simplify the data processing and to round up the ciphers to 2 decimal digits. We also filtered both datasets in order to only analyze the data using the rows and columns we were interested in, and we did this to different degrees according to the needs presented by every question. 

Questions
We posited the following questions: 

1.	What product exhibits the highest environmental impact for all environmental markers used to measure (total emissions, nitrogen leaching, freshwater withdrawal, and land use change)? Is there a single product that ranks the highest across all of them?
The product with the highest overall impact across all environmental markers is Cheese.
2.	Which step from the food production cycle is the most carbon intensive across all products?
The most carbon-intensive step across all products is 'Farm' with a total of 149.20 emissions.
3.	Does the answer to the previous question changes if we divide products as plant and animal-based products? If so, which step becomes the most carbon intensive for each group?
No, the most carbon intensive step in the lifecycle of both groups is still farming.
4.	Which of these 2 categories exhibits the highest environmental impact across all markers?
Animal products have the highest impact across all markers, although when analyzing only the listed products, the difference is not as pronounced.
5.	Based in the water-scarcity information available, what agricultural projects would we advise the BID to finance in our listed countries?
Brazil, Colombia and Costa Rica should be able to receive funding for all projects, while for Mexico we would not advise investing in projects working with nuts, beef and cheese production. 

Conclusion 
We found that this methodology could be applied to real-life situations in which the environmental impact of development projects is being regarded. We have gathered enough information about a large number of agricultural produces, both animal and vegetal, such as their water intensity, generated land use change, carbon intensity, fertilizer requirements and associated emissions to the environment, insecticide requirements, etc. We also have vast arrays of information regarding climatic and geographical conditions, in many cases to the local level, as well as about climate change, which can be used to generate different scenarios. This means that we can not only assess the impact and viability of projects using currents conditions, but we can make educated predictions about the risks determined projects might suffer, such as a lack of water from precipitations or irrigation.
