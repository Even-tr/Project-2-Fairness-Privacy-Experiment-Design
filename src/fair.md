# Fairness
We choose the equal opportunity definition of fairness defined as:

$$
\operatorname{equal-op} = min(\frac{P(\hat{y}|z=1, y=1)}{P(\hat{y}|z=0, y=1)},\frac{P(\hat{y}|z=0, y=1)}{P(\hat{y}|z=1, y=1)} )
$$

Dubbed we call $S$ for 'score'. Let $z=$ 'gender' and $y=$ 'death' for the remainder of this discussion. 

Since we do not know $P(\hat{y}|z,y)$, we must estimate it with a predictive model: $\hat{f}(x) = \hat{y}$, thus our $\hat{S}$ is conditioned on our data $X\in\mathcal{X}$, indicated with the notation:

$$
\hat{S}_X =min(\frac{\hat{P}(\hat{y}|z=1, y=1)}{\hat{P}(\hat{y}|z=0, y=1)},\frac{\hat{P}(\hat{y}|z=0, y=1)}{\hat{P}(\hat{y}|z=1, y=1)} )
$$

Currently, our predictive model is the beta-Bernoulli model, which completely ignores the features $x_i$, however this could change, and our code must thereafter be flexible enough to accept any other model.

