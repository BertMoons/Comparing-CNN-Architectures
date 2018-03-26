# A Comparison of Network Architectures

This is a comparison of Network Architectures in the accuracy - operations - model_size space.  
The repo will be regularly updated if new network architectures come out. Let me know
if you have any suggestions for architectures to add, or if any relevant data is missing.

This comparison is built on the work done by [Canziani et al](https://arxiv.org/abs/1605.07678).  


## Network Efficiency
In the graphs below, 'MSD' are [Multi-Scale DenseNets](https://arxiv.org/abs/1703.09844), 'DN' are [DenseNets](https://arxiv.org/abs/1608.06993) and 'MobNets' are [MobileNets](https://arxiv.org/abs/1704.04861).
Checkout [interactive_plot.py](interactive_plot.html) for a more readable visualization of all data points.

MobileNets stand out through their high accuracy using tiny models. 
DenseNets and Multi-Scale DenseNets achieve higher accuracy at the same computational budget, but require larger models.



**Figure 1** IMAGENET top-1 accuracy vs #flops, blob size is the model size
<img src="https://raw.githubusercontent.com/BertMoons/Comparing-CNN-Architectures/master/figures/accuracy_ops_modelsize.png">

**Figure 2** IMAGENET top-1 accuracy vs #weights, blob size is the #flops
<img src="https://raw.githubusercontent.com/BertMoons/Comparing-CNN-Architectures/master/figures/accuracy_modelsize_ops.png">


## Remarks

A higher amount of operations or a larger model-size does not necessarily translate in a 
higher __energy consumption__ on an embedded platform. The real relevant comparison point would hence be top-1 accuracy vs energy/classification, which is heavily platform dependent.

If you like/use this comparison, please cite [Canziani et al](https://arxiv.org/abs/1605.07678) and:

```
(to appear)
@phdthesis{moons2018Embedded,
    title={Embedded Deep Learning - Algorithms, Architectures and Circuits for Always-On Neural Network Processing},
    author = {Bert Moons},
    advisor = {prof. Marian Verhelst}
    school=[KU Leuven},
    year={2018}
    }
```
