Clockwork Recurrent Neural Network using Theano
===============================================

This is an implementation of the clockwork-rnn described in the paper http://arxiv.org/abs/1402.3511,
which I am using to with the idea. 

#### WARNING! Hastily written and unreadable code. Also, it will probably not work so use at your own discretion.

In this revision, I try to make the network learn a function and giving as input the steps it should take towards that function.

Big problem I am currently facing is that theano.grad is really slow when constructing networks with many groups in each layer.

If you have any suggestions and/or want to make this better don't hesitate to open issue/pull request