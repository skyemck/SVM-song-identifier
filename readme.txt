Conventions:
- Write your name above block of code you write
- Add short comments for what you're doing in each line of code
- Use proper spacing to make it easier to read
- If you test, add what you tested and the output


PLAN:
1. Import dataset
2. Create vectors for each song and it's attributes
-> ex.) CSV the data set, seperate every 68 values and set that as vector 1, 2...n
3. state which label refers to what country
4. cluster all variables against the label (1-33 countries)
5. weight the variable based on how many of the tracks with that label had the variable in that cluster
6. use the weighted sum of squares error like in hw2 with the weight for each variable
7. KNN based on their total 'score' 
8. Train with the training data
9. Check accuracy
10. Test the testing data
11. Prove results:
    -> Scatter plot with 0 as error rate 
    -> Clusters vs. labels
    -> Overall accuracy rate in training
    -> Overall accuracy rate in testing
