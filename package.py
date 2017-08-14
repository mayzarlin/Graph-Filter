import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import collections as mc
from matplotlib import lines
from numpy import linalg as la
import numpy.matlib as mat
from scipy.spatial.distance  import pdist, squareform# Function to find the Euclidean distance between Node

## import my class
from NetworkClasses import Local
from NetworkClasses import Network as Graph
from SPClasses import GF as gf