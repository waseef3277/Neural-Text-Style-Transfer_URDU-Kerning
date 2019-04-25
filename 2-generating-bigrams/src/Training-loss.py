import pylab
from matplotlib import pyplot;
from pylab import genfromtxt;
mat0 = genfromtxt("training_error_log.txt");
mat1 = genfromtxt("validation_error_log.txt");
pyplot.plot(mat0[:,0], mat0[:,1], label = "Training Error");
pyplot.plot(mat1[:,0], mat1[:,1], label = "Validation Error");
pyplot.yscale('linear')
pylab.title("Training and Validation Error")
pylab.xlabel("Iteration")
pylab.ylabel("Error")
pyplot.legend();
pyplot.show();