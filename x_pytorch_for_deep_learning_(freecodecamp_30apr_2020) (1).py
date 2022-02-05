# -*- coding: utf-8 -*-
"""x_PyTorch_for_Deep_Learning-(freeCodeCamp-30Apr-2020).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15SWum4GdRiFKXDXA8Z2jcy8OXcldURGh
"""

import torch

"""# Tensors
At its core, PyTorch is a library for processing tensors. A tensor is a number, vector, matrix or any n-dimensional array. Let's create a tensor with a single number:
"""

# Number 
t1 = torch.tensor(4.) 
t1

"""4. is a shorthand for 4.0. It is used to indicate Python (and PyTorch) that you want to create a floating point number. We can verify this by checking the dtype attribute of our tensor:"""

t1.dtype

"""Let's try  creating slightly more complex tensors:"""

# Vector
t2 = torch.tensor([1., 2, 3, 4])
t2
t2.dtype



#Matrix
t3 = torch.tensor([[5., 6], [7, 8], [9, 10]])
print(t3, '\n',t3.dtype)

# 3-dimensional array
t4 = torch.tensor([
                   [[11, 12, 13],
                    [13, 14, 15]],
                   [[15, 16, 17],
                    [17, 18, 19.]]])
t4

"""tensors can have any number of dimensions, and different lengths along each dimension. We can inspect the length along each dimension using the .shape property of a tensor."""

t1.shape

print(t2)
t2.shape

print(t3)
t3.shape

print(t4)
t4.shape

"""# Tensor operations and gradients
We can combine tensors with the usual arithmetic operations. Let's look an example:
"""

# Create tensors.
x = torch.tensor(3.)
w = torch.tensor(4., requires_grad=True)
b = torch.tensor(5., requires_grad=True)

"""We've created 3 tensors x, w and b, all numbers. w and b have an additional parameter requires_grad set to True. We'll see what it does in just a moment.

Let's create a new tensor y by combining these tensors:
"""

# Arithmetic operations
y = w * x + b
y

"""As expected, y is a tensor with the value 3 * 4 + 5 = 17. What makes 
PyTorch special is that we can automatically compute the 
derivative of y w.r.t. the tensors that have requires_grad set 
to True i.e. w and b. To compute the derivatives, we can call the
.backward method on our result y.
"""

# Compute derivatives
y.backward()

"""The derivatives of y w.r.t the input tensors are stored in the .grad property of the respective tensors."""

# Display gradients
print('dy/dx:', x.grad)
print('dy/dw:', w.grad)
print('dy/db:', b.grad)

"""`1. Note that x.grad is None, because x 
doesn't have requires_grad set
to True`

`2. The "grad" in w.grad stands for gradient, which is another term
for derivative, used mainly when dealing with matrices.`

# Interoperability with Numpy

[Numpy](http://www.numpy.org/) is a popular open-source library used for mathematical and scientific computing in Python. It enables efficient operations on large multi-dimensional arrays and has a vast ecosystem of supporting libraries, including:

* [Pandas](https://pandas.pydata.org/) for file I/O and data analysis
* [Matplotlib](https://matplotlib.org/) for plotting and visualization
* [OpenCV](https://opencv.org/) for image and video processing


If you're interested in learning more about Numpy and other data science libraries in Python, check out this tutorial series: https://jovian.ai/aakashns/python-numerical-computing-with-numpy .

Instead of reinventing the wheel, PyTorch interoperates well with Numpy to leverage its existing ecosystem of tools and libraries.

##Here's how we create an array in Numpy:
"""

import numpy as np

x = np.array([[1, 2], [3, 4.]])
x

"""`We can convert a Numpy array to a PyTorch tensor using 
torch.from_numpy`
"""

# Convert the numpy array to a torch tensor.
y = torch.from_numpy(x)
y

x.dtype, y.dtype

"""We can convert a PyTorch tensor to a Numpy using the .numpy
method of a tensor.
"""

# Convert a torch tensor to a numpy array
z = y.numpy()
z

"""`The interoperability between PyTorch and Numpy is really
important because most datasets you'll work with will likely be read and preprocessed as Numpy arrays.`
"""

