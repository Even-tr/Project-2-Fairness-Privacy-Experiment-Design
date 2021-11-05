# Our model of choice

We will estimate $p(s_i|a_t )$ using a beta-Bernouli model (like in the last project), where we model the probability of a symptom as independently with different $\theta_i$. To update this model, we need a summary statistic, i.e. the number of sick given treatment, and the number of sick given no treatment. Since this is a simple count, it has a sensitivity of 1, making the implementation of the Laplace mechanism easy. 

For the decision of giving treatment, using a privacy method adapted for database queries makes little sense, because a single decision would be equivalent with a database with one row. Therefore, we choose the randomized response mechanism, with some parameter $p$ to be decided. 