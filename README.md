## Gold Point Game

### Game Rules:
There are several bots which output two real numbers limited to (0,100) range. Every round a gold number is computed by computing the mean of all numbers multiplied by 0.618. The team who submits the nearest number get scores. The team who submits the most further number deducts two points. After a certain rounds, the team who gets highest score wins the game.
Detailed rules are in [Gold Number](https://edu.cnblogs.com/campus/ustc/InnovatingLeadersClass/homework/2231)

### Directory Illustration
.
|--docs : The explanation about the rules, game background and some hints
|--src : The src code
|-- test dataset : Dataset provided for training and testing models
|-- test platform : Provided for running your program to compete with previous bot using data provided in test_dataset




#### environment:
Python 3.6

#### package dependency:
numpy





### Results in Given Dataset

| Policy                            | Nearest | Farthest | Score | Ranking | Dataset |
| --------------------------------- | ------- | -------- | ----- | ------- | ------- |
| moving_exp_avg + detect +disturb  | 83/400  | 268/400  | 1028  | 1/24    | 1       |
| moving_exp_avg + detect + disturb | 77/400  | 267/400  | 916   | 1/24    | 2       |
| moving_exp_avg + disturb          | 59/400  | 257/400  | 594   | 1/24    | 1       |
| moving_exp_avg + disturb          | 60/400  | 255/400  | 612   | 2/24    | 2       |
|                                   |         |          |       |         |         |
|                                   |         |          |       |         |         |

### Competition Results
* Last but one in first 400 rounds
* Third in second 400 rounds after a few revises.
