# Simple model used to predict symtoms given
import numpy as np

class model:
    def __init__(self, nsymptom, nvacc):
        # Priors for the beta-bernoulli model
        self.a = np.ones(shape=[nvacc, nsymptom])/2 # using jeffreys prior
        self.b = np.ones(shape=[nvacc, nsymptom])/2 # using jeffreys prior
        self.nvacc = nvacc
        self.nsymptom = nsymptom

    def update(self, features, actions, outcomes):
        for index, v in enumerate(self.a):

            if np.sum(outcomes[np.where(actions == index)], axis=1).size != 0:
                self.a[index] += np.sum(outcomes[np.where(actions == index)], axis=1)
                    
                self.b[index] += np.sum(outcomes[np.where(actions == index)]==0, axis=1)\
                    - np.sum(outcomes[np.where(actions == index)], axis=1)
            else:
                self.b[index] += np.sum(outcomes[np.where(actions == index)]==0, axis=1)


    def get_prob(self, features, action):
        return self.a[action] / (self.a[action] + self.b[action])

    
    def retrain(self, features, actions, outcomes):
        # Use aggregated database of outcomes etc...

        self.a = np.ones(shape=[self.nvacc, self.nsymptom])/2 # using jeffreys prior
        self.b = np.ones(shape=[self.nvacc, self.nsymptom])/2 # using jeffreys prior

        self.update(features, actions, outcomes)

