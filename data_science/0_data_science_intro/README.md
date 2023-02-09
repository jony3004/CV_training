### DS Intro 

 - Read chapter 2 in ISLR: p.15-42.
 - What are the parameteric and non-parameteric approaches in statistical learning? What are the pros and cons of each approach?
 - What are the pros and cons of flexible methods in machine learning?
 - Explain the bias-variance trade-off? Give an example to illustrate your explanation.
 

1. Both parametric and non-parametric approaches deal with the subject of correctly estimating the function f, such that f(X)= Y.
The parametric approach tries to estimate the function by using an explicit set of parameters, for example - y = f(x) = a_0 + a_1x_1 + ... + a_nx_n.
The main advantage of the parametric approach is that it's usually much simpler than other approaches, as estimating parameters is less costly and easier.
The main disadvantage is that such a model will have an initial tendency of being too simplistic, or even at times very inaccurate,
and even though it can be altered to express a complex function, in this case it might overfit.

The non-parametric approach doesn't make explicit assumptions about the functional form of f, and thus doesn't use parameters like the parametric one.
Instead, it aims to find a close estimate to the given points, and focuses less on the function itself.
This approach avoids several problems that the parametric approach encounters - it's less like to be "a wrong fit", as in this method we don't assume
anything about f's shape, and just focus on matching f to our data.
Thus f is much more flexible - we don't expect it to be of a certain shape, and there's a wide variety for configurations for it.
The main disadvantage is the complexity of the approach.
It requires multiple observations in order to be accurate (it can't be easily and often accurately built like the parametric approach), 
and thus is more costly and slow.

2. In general, flexible methods are those that are able to generate a larger amount of shapes of f in order to describe f in contrast to less flexible 
methods that are more set on a particular set of shapes.
The main advantage of a more strict model is in the subject of inference, if instead of predicting correctly, we're keen on finding the relations between 
the variables and how they affect Y.
Flexible methods for example might not be ideal for this goal, due to them possibly being too complex and intricate.
Inflexible methods are also less in danger of overfitting, and hence are sometimes the preferable choice even for the goal of prediction.
Yet, flexible methods also have several clear advantages in the field of predictions.
They are an instrument that makes our estimation tailor-made and much more accurate often, and so will most likely cause us to get better prediction results.
As in question 1, they will be less constrained in terms of options for shapes, and hence be more suitable for complex Y patterns.

3. The mentioned bias and variance are both part of expected test MSE.
Variance refers to the amount by which the estimation of f would change if we used a different training set - using a different set might cause us to fit 
an entirely different function, and the difference between those estimation will be the variance.
Bias refers to our level of simplification of the model - by using a less complex model to imitate the data, we might be less accurate, and to be
further from the real-life distribution.
The meaning of the bias-variance trade-off term is that usually by finding a model that lowers the bias, we will cause the variance to go up, and the same
the other way around, so we'd want to find a certain sweet-spot for which the bias will already be low, and the variance wouldn't go up yet, as 
the model won't be too complex and overfitted yet.
In regards to the previous questions - more flexibility equals less variance and more bias, and the other way around.

An example can be a certain model which is averagly complex and non linear - By using a linear estimation we'll get a simple and less accurate model, thus
we expect it to be more suited for different pieces of data from the training set, but also to underfit, as it's not complex enough to catch certain
patterns in the real time data, and by that affecting the inaccuracy of the test MSE.
Now we can try and improve this model by adding complexity to it, and by some extent it will work, as the bias will clearly go down, and the variance won't 
go up yet.
But if we don't find the sweet-spot and go too far with making the model complex, we might get into the territory of overfitting, and will have a worse
variance rate.
