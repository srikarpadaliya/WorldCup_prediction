# Task 2: Predicting the Finalist Teams and Players

## About The Dataset

I have crafted a custom dataset derived from ODI (One Day International) cricket matches, meticulously extracted and organized from the comprehensive cricketing data available on cricsheet.org. I have used the modified script from Aadita Agarwal's [GitHub](https://github.com/aaditagarwal) to convert YAML to Excel format.


### **Features**

#### Dataset 1 - Batsman:
**player_name**: Name of the player (batsman).<br>
**team:** Name of the team player belongs to.<br>
**innings:** The number of times the player has batted in matches, representing their opportunities to score runs.<br>
**runs:** The total number of runs scored by the batsman across all their innings, indicating their overall batting performance.<br>
**balls:** The total number of deliveries the batsman faces, reflecting their involvement and time spent at the crease.<br>
**average:** The mean value of runs scored per dismissal, offering a measure of the batsman's consistency and effectiveness.<br>
**strike_rate:** The speed at which the batsman scores runs, calculated as the number of runs scored per 100 balls faced.<br>
**centuries:** The number of times the batsman has scored 100 or more runs in a single inning, highlighting their ability to achieve high scores.<br>
**fifties:** The number of times the batsman has scored between 50 and 99 runs in a single inning, showcasing consistent half-century performances.<br>
**zeros:** The number of times the batsman has been dismissed without scoring any runs, indicating instances of unsuccessful innings.


#### Dataset 2-Bowler:
**player_name:** Name of the player (batsman).<br>
**team:** Name of the team player belongs to.<br>
**innings:** The number of times the player has bowled in matches, representing their opportunities to take wickets.<br>
 **runs:** The total number of runs conceded by the bowler, reflecting their effectiveness in limiting the opposition's scoring.<br>
 **balls:** The total number of deliveries bowled by the player, indicating their workload and contribution to the team's bowling efforts.<br>
 **wickets:** The total number of wickets taken by the bowler showcasing their ability to dismiss opposing batsmen.<br>
 **extras:** Additional runs conceded through no-balls, wides, and byes, contributing to the overall runs given away by the bowler.<br>
 **average:** The mean value of runs conceded per wicket taken, providing a measure of the bowler's effectiveness in getting dismissals.<br>
 **strike_rate:** The rate at which the bowler takes wickets, calculated as the number of balls bowled per wicket taken.<br>
 **economy:** The average number of runs conceded per over bowled, indicating the bowler's ability to control the scoring rate.<br>
 **wicket_hauls:** The number of times the bowler has taken a specified number of wickets in a single inning, highlighting exceptional bowling performances.<br>


### Dataset 3-Custom:
This dataset has been created especially to help predict the 11 members of each team for the ICC World Cup Finals.

**date:** The date of the Match<br>
**player_name:** The name of the player<br>
**team:** The team player belongs to.<br>
**opposition:** The opposition team of the player's team.<br>
**venue:** The location(In India) where the match took place.<br>
**player_rating:** The player's ICC Rankings for ODI fetched from [here](https://www.icc-cricket.com/rankings/mens/player-rankings/odi).<br>
**selected:** A boolean value that determines if the player played in The play-in 11 or not.


## Results
#### Team India
![image-ind-team](https://github.com/srikarpadaliya/WorldCup_prediction/blob/vrishin/Images/image1.png)

![image-ind](https://github.com/srikarpadaliya/WorldCup_prediction/blob/vrishin/Images/image2.png)



#### Team South Africa
![image-sa-team](https://github.com/srikarpadaliya/WorldCup_prediction/blob/vrishin/Images/image3.png)


![image-sa](https://github.com/srikarpadaliya/WorldCup_prediction/blob/vrishin/Images/image4.png)


# Contributors
### Vrishin Shah (202101094)
