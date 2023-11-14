# Dataset: [World Cup Prediction Model](https://colab.research.google.com/drive/1rzajCOjjXiDNpz-Vv9XayGYTkFShX-9o?usp=sharing#scrollTo=OLZ3iOi4Wx31)

## About Dataset
We crafted a custom dataset derived from ODI (One Day International) cricket matches, meticulously extracted and organized from the comprehensive cricketing data available on [cricsheet.org](https://cricsheet.org/).

This dataset encapsulates detailed information such as bowler's name, team, innings, runs, balls, wickets, extras, average, strike_rate, economy, and wicket hauls, providing a rich resource for in-depth analysis and insights to predict the bowler, who will be the leading wicket taker in ICC Mens World Cup 2023.

This project consists of 5 parts:
1. Introduction
2. Data Cleaning
3. Data visualization
4. Data Preprocessing
5. Modeling

# 1. Introduction

## Feature Description
1. **Name:** Name of the Bowler
2. **Team:** Name of Bowler's team
3. **Innings:** Number of innings in which player bowled
4. **Runs:** Total runs conceeded by bowler
5. **Balls:** No. of balls
6. **Wicket:** Total wickets taken
7. **Extras:** Total Extra runs conceeded
8. **Average:** Runs given per wicket taken
9. **Strike Rate:** Balls bowled per wicket taken
10. **Economy:** Average runs given per over
11. **Wicket Hauls:** No. of 5 or more wickets taken in a match

# 2. Data Cleaning

![This is an Image of the head of the dataset.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/dataset_head.png)

The above dataset needs to be updated since the analysis would have an obselete dataset. Adding data for matches Bangladesh vs Australia (11 Nov. 2023), England vs Pakistan (11 Nov. 2023) and India vs Netherlands (12 Nov. 2023).

Moreover, we made many changes to this dataset like converting overs to balls and merging the old dataframe with the new one. We got the selected list of bowlers for our analysis.

![This is an Image of the selected list of bowlers after Data Cleaning.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/selected_bowlers_list.png)

# 3. Data Visualization

![This is an Image of the Economy Rate of the Bowlers.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/bowling_economy_rate.png)
![This is an Image of the Bowling Strike Rate of the Bowlers.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/bowling_strike_rate.png)
![This is an Image of the Bowling Average Rate of the Bowlers.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/bowling_average.png)

It is self-understandable that, as there are only a few matches left in the world cup, there are very high chances that only those players who has most wickets till now, only one of them can be the batsman with most wickets.

So, making the list of batsman who has wickets more than 10.

Also, only India, Australia, New Zealand, and South Africa will be in the semi-final. So, bowlers belonging to this team, can gain addtional wickets, other then this team, there are no chances that there batsmen will score more than that they currently have.

![This is an Image of the Scatter Plot of the best bowlers.](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/scatter_plot_best_bowlers.png)

From this graph, we can see that these will be top 5 wicket takers from these set of bowlers.

# 4. Pre-Processing
We have made a new dataframe consisting of 'date' feature with only the selected list of bowlers from the data cleaning section that we achieved.

We also sorted the new dataframe using 'Label Encoding'.

# 5. Modeling
It is confirmed that, the Semi-Finale will matches will happen between India vs. New Zealand and South Africa vs. Australia from this plot training graph:
![This is the Screenshot of the Model Results](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/plot_training_history.png)

As per the prediction in task-2, the **Finale** will happen between **India and South Africa**.

We are going to predict the wickets for bowler in these 4 teams, from my **selected_bowler list** for Semi-Finale and Finale, using **RNN** and **LSTM model**.

This are the top 5 bowlers predicted:

![This is the Screenshot of the Model Results](https://github.com/srikarpadaliya/WorldCup_prediction/blob/top_bowlers/Images/top_5_bowlers.png)

# Conclusion
Considering semi final match scores for (South Africa, Australia) and (India, New Zealand) and final match between India and South Africa players, we got the top five wicket takers of the tournament.

# Contributors
* Aditya Singhania (202101086) - Data Cleaning, Preprocessing and Modeling
* Kirtan Mevada (202101012) - Data Visualization and Documentation
