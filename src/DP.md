# Differential Privacy

The definition of differential privacy is:

-----

    Definition 3.4.2 (ε-Differential Privacy). A stochastic algorithm π : X → A, where X is
    endowed with a neighbourhood relation N, is said to be ε-differentially private if:

$$
|\ln \frac{\pi(a|x)}{\pi(a|x')} | \leq \epsilon
$$

-----

In particular: If $\pi$ is a counting algorithm, i.e.

$$
\pi(a|x) = \sum_{i} \mathbb{1}(x \text{ satisiying some condition})
$$
Then the centralized Laplace algorithm is ε-differentially given $\lambda =  1/\epsilon$. This is due to the fact that a counting function has sensitivity 1, because given a database $x$ and a neighboring database $x'$ (i.e. $xNx'$ is satisfied), then the diverging row could either satisfy the same condition, making the count equal, or not satisfy the condition, making the count one less.

We therefore use the Laplace mechanism in the beta - Bernoulli model explained below:

$$
    \theta_i \sim \operatorname{Beta}(a, b)\\
    y_i \sim \operatorname{Bernoulli}(\theta_i)\\
    \theta_i | y_i \sim \operatorname{Beta}(a', b')
$$
Where $a'$ and $b'$ are given by the Laplace mechanism instead of the usual counting:

$$
 c = \sum_{j=1}^{n} y_{i,j} + Laplace(1/\epsilon)\\
 a' = a + c\\
 b' = b + n - c
$$

## Additively updating our model
When updating our model, we have the possibility of either using the former posterior as a new prior, adding the noisy count, and proceeding as normal, however this would also add an increasing amount of Laplace noise. Another possibility is to retrain using our original prior and accumulated data. In this case, we must consider the privacy of repeated queries to our Data base. Let's say we in total apply $Q$ queries, giving the total DP of:
$$
    \sum_{i=1}^{Q} \epsilon = Q\epsilon
$$
To still achieve the same ε-differentially privacy, we must then use $\epsilon_Q = \epsilon/Q$. This could decrease the total noise at the end of our application of the policy, however it would apply greater noise in the beginning. Since our model is the least accurate in the beginning, this in undesirable. Therefore, we choose the accumulation approach.

# Randomized response
For any given individual, the decision to vaccinate is given but the maximizer of the reward, given a randomized response.
The response has the following structure:

* Flip a coin with probability $\theta_1$. If heads, answer truthfully.
* If tails, flip another coin with probability $\theta_2$ and answer yes or no given heads or tails. 

The goal of this mechanism is to satisfy the following equation:

$$
p(y|y') = \frac{p(y'|y)p(y)}{p(y')} = p(y)
$$
Where $y$ is the truth and $y'$ is the answer. In other words, knowing the response of the individual gives no additional information useful for determining the probability $y$ being true. It follows that $p(y'|y) = p(y')$ to achieve this.

$$
p(y'|y) = p(\text{answer 'yes' when it is the truth})\\
 = p_{f1} + (1-p_{f1})p_{f2} = \theta_1 + (1-\theta_1)\theta_2
$$

$$
p(y'|\overline{y}) = (1-\theta_1)\theta_2
$$

$$
p(y') = p(y)p(y'|y) + (1-p(y))p(y'|\overline{y})\\
= p(y)(\theta_1 + (1-\theta_1)\theta_2) + (1-p(y))((1-\theta_1)\theta_2)
$$

Where $p_{fi}$ is the probability of flip number $i$ giving heads. (to be continued...)