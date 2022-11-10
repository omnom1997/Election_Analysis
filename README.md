# Election Analysis

## Project Overview
A Colorado Board of Election employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate won.
4. Determine the winner of the election based on popular vote.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 total votes cast in the election.
- Break down of votes per county:
  - Jefferson County had 10.5% of the votes which translates to 38,855 votes.
  - Denver County had 82.8% of the votes which translates to 306,055 votes.
  - Arapahoe County had 6.7% of the votes which translates to 24,801 votes.
- The county with the largest number of voter was Denver.
- The candidate results were:
  - Charles Casper Stockahn received 23.0% of the vote which translates to 85,213 votes.
  - Diana DeGette received 73.8% of the vote which translates 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote which translates 11,606 votes.
- The winner of the election was Diana DeGette.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.

The analysis of the election was also printed to a text file and the results are pictured below:

![Screenshot 2022-11-09 171433](https://user-images.githubusercontent.com/114427019/200969254-2794725e-b9f2-4027-aed5-661a60dddc79.png)

## Election Audit Summary
This script could be modified to show, if the information is available, how many people voted using the various methods of voting such as mail-in ballot, in-person, or early voting. This can help election officials and election analysts to determine how people are voting and if there is a need for additional infrastructure, such as more in-person voting sites. This can be accomplished by following the same pattern established in the script to find the counties and candidates as well as count each instance of the counties and candidates.

And additional way the code could be modified to show if a run off election is needed if no candidate wins the majority of votes. This could be added to the `if` statement that determines the winning candidate, pictured below.

![Screenshot 2022-11-09 163417](https://user-images.githubusercontent.com/114427019/200964801-0c1e5da1-3867-4d36-a620-14fced15d44c.png)
