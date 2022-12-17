# Neural Networks

### In this article we will explore through neural networks and find what it actually is.

---

**Neural networks reflect the behavior of the human brain, allowing computer programs to recognize patterns and solve common problems in the fields of AI, machine learning, and deep learning.**

Lets start with a very simple neural network:

<aside>
💻 a program that takes a pictures of one digit numbers and give us the actual number the picture shows.

</aside>

Somehow identifying digits is incredibly easy for your brain to do, but almost impossible to describe how to do! The traditional methods of computer programming, with if statements and for loops and classes and objects and functions, just don’t seem suitable to tackle this problem.

But what if we could write a program that mimics the structure of your brain? That’s the idea behind neural networks. The hope is that by writing brain-inspired software, we might be able to create programs that tackle the kinds of fuzzy and difficult-to-reason-about problems that your mind is so good at solving.

But an important point is the “**learning**” part of machine learning comes from the fact that we never give the program any specific instructions for how to identify digits. Instead, we’ll show it many examples of hand-drawn digits together with labels for what they should be, and leave it up to the computer to adapt the network based on each new example.

![Capture.JPG](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/Capture.jpg)

### **Neurons**

when we say neuron, all you have to think is “a thing that holds a number.” Specifically, a number between 0.0 and 1.0. Neural networks are really just a bunch of neurons connected together.

and This number inside the neuron is called the “**activation**” of that neuron

![                    neuron lit up more when its activation is higher](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/activation.jpg)

                    neuron lit up more when its activation is higher

the image we feed to our model is a **28×28=784** pixels picture of a digit on the center which represent a matrix of numbers (0 to1) to the computer

![Each pixel in the original image has a value between 0.0 (black) and 1.0 (white).](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/pixel-values.png)

Each pixel in the original image has a value between 0.0 (black) and 1.0 (white).

To represent this in the network, we’ll create a layer of 784 neurons, where each neuron corresponds to a particular pixel.

The last layer of our network will have 10 neurons, each representing one of the possible digits. The activation in these neurons, again some number between 0.0 and 1.0, will represent how much the system thinks an image corresponds to a given digit.

### **The Hidden Layers**

![In this network we have 2 hidden layers, each with 16 neurons](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/hidden-layers.png)

In this network we have 2 hidden layers, each with 16 neurons

You’ll notice how in these pictures each neuron from one layer is connected to each neuron of the next with a little line. This is meant to indicate how the activation of each neuron in one layer has some influence on the activation of each neuron in the next layer.

However, not all these connections are equal. Some will be stronger than others.

What we’ll do is assign a weight to each of the connections between our neuron and the neurons from the first layer. These weights are just numbers.

Each weight is an indication of how its neuron in the first layer is correlated with this new neuron in the second layer.

If the neuron in the first layer is on, then a **positive** weight suggests that the neuron in the second layer should also be on, and a **negative** weight suggests that the neuron in the second layer should be off.

the activation of a neuron from a second layer is roughly calculated like this:

the hope is that if we add up all the desires from all the weights, the end result will be a neuron that does a reasonably good job of detecting the number we’re looking for (as long as the weights are well-chosen).

     $**w1​a1​+w2​a2​+w3​a3​+w4​a4​+⋯+wn​an​**$

The result of the weighted sum like this can be any number, but for this network we want the activations to be values between 0 and 1. So it’s common to pump this weighted sum into some function that squishes the real number line into the range between 0 and 1.

One common function that does this is called the “sigmoid” function

![sigmoid.png](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/sigmoid.png)

![another function that is easier to train and more used is “ReLU” function.](Neural%20Networks%204bdf87d93d6a45f3b0a06895ca12da49/download_(1).png)

another function that is easier to train and more used is “ReLU” function.

And that’s just one neuron! Every other neuron in the second layer is also going to have weighted connections to all 784 neurons from the first layer

And all of this is just the connection from the first layer to the second. The connections between the other layers also have a bunch of weights as well. All said and done, this network has 13,002 total weights! 13,002 knobs and dials that can be tweaked to make this network behave in different ways

**So when we talk about learning  we mean getting the computer to find an optimal setting for all these many, many numbers that will solve the problem at hand.**

And that was it for this article. you can find more specific information at the link below

[But what is a neural network? | Chapter 1, Deep learning](https://www.youtube.com/watch?v=aircAruvnKk&list=RDCMUCYO_jab_esuFRV4b17AJtAw&start_radio=1&rv=aircAruvnKk&t=215)