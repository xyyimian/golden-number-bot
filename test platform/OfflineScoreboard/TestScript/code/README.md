## Gold Point Game

Python 3.6

require numpy



### Test Result

| Policy                            | Nearest | Farthest | Score | Ranking | Dataset |
| --------------------------------- | ------- | -------- | ----- | ------- | ------- |
| moving_exp_avg + detect +disturb  | 83/400  | 268/400  | 1028  | 1/24    | 1       |
| moving_exp_avg + detect + disturb | 77/400  | 267/400  | 916   | 1/24    | 2       |
| moving_exp_avg + disturb          | 59/400  | 257/400  | 594   | 1/24    | 1       |
| moving_exp_avg + disturb          | 60/400  | 255/400  | 612   | 2/24    | 2       |
|                                   |         |          |       |         |         |
|                                   |         |          |       |         |         |

