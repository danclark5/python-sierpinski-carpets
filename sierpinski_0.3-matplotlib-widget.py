
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.widgets import TextBox
plt.subplots_adjust(bottom=0.2)
img=[[1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,]*33]*36
def ontextch(*args,**kw): print(args,kw)
axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'Evaluate', '2')
text_box.on_submit(ontextch)
plt.show()
# widget works but img array is not visible

