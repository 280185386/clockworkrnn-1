__author__ = 'mike'

import theano
from theano import tensor as T
import numpy as np

def variance(input_size):
    return 2.0 / input_size


def negative_log_likelihood(output, prediction):
    output, prediction = T.flatten(output), T.flatten(prediction)
    return -T.mean(T.log(output)[prediction])

def adam(loss, all_params, learning_rate=0.001, b1=0.9, b2=0.999, e=1e-8,
         gamma=1 - 1e-8):
    """
    Code taken from https://gist.github.com/skaae/ae7225263ca8806868cb

    ADAM update rules
    Default values are taken from [Kingma2014]

    References:
    [Kingma2014] Kingma, Diederik, and Jimmy Ba.
    "Adam: A Method for Stochastic Optimization."
    arXiv preprint arXiv:1412.6980 (2014).
    http://arxiv.org/pdf/1412.6980v4.pdf

    """
    updates = []
    all_grads = theano.grad(loss, all_params)
    alpha = learning_rate
    t = theano.shared(np.float32(1))
    b1_t = b1 * gamma ** (t - 1)  # (Decay the first moment running average coefficient)

    for theta_previous, g in zip(all_params, all_grads):
        m_previous = theano.shared(np.zeros(theta_previous.get_value().shape,
                                            dtype=theano.config.floatX))
        v_previous = theano.shared(np.zeros(theta_previous.get_value().shape,
                                            dtype=theano.config.floatX))

        m = b1_t * m_previous + (1 - b1_t) * g  # (Update biased first moment estimate)
        v = b2 * v_previous + (1 - b2) * g ** 2  # (Update biased second raw moment estimate)
        m_hat = m / (1 - b1 ** t)  # (Compute bias-corrected first moment estimate)
        v_hat = v / (1 - b2 ** t)  # (Compute bias-corrected second raw moment estimate)
        theta = theta_previous - (alpha * m_hat) / (T.sqrt(v_hat) + e)  # (Update parameters)

        updates.append((m_previous, m))
        updates.append((v_previous, v))
        updates.append((theta_previous, theta))
    updates.append((t, t + 1.))
    return updates

def quadratic_loss(a, b):
    a, b = a.flatten(), b.flatten()
    # return T.mean(binary_crossentropy(a, b))
    return T.mean((b - a) ** 2)

