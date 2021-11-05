# Our Utility

We define utility $U(X, Y, A)\to\mathbb{R}$ (i.e. a function of pre vaccine/treatment features, post treatment features and the action we took) as the sum of rewards for each individual. The rewards are a weighted sum of the outcomes:

$$
U(X,Y,A) = \sum_{i=1}^{N}r_i(x_i, y_i, a_i)
$$
And reward is the weighted sum of symptoms:

$$
r_i^{\text{no action}} = w^Ty
$$
$$
r_i^{a_i} = w^Ty\cdot2 - \operatorname{Cost} (a_i)
$$

(Currently we ignore the features in our utility. This implies for instance that any-one dying is equally bad, regardless of their prior condition. Which is not necceastily a good property of our utility)

We can let 'Cost' be the monetary cost of the treatment/vaccine. I.e. 100$.

Further, we set the rewards to be all lower than zero, making it a loss function of sort, which implies that a utility of zero is the absoulte best. This makes the 'action' reward worse than the 'no action', refelcting that interfering is worse than not. If at a later stage we have more vaccines, then we must tune the coefficient more carefully.

# Expected utility
For each action we can calculate the expected utility given this formula:
$$
\operatorname{E}_{a_i} U = \sum_{y\in Y}U(x, y, a_i)\cdot p(y|x, a_i)
$$
We can then choose the action $a_{best}$ which maximizes this expectation. However, since we do not know $p(y|x,a_i)$, we must estimate it with a model.