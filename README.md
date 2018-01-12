# A Comparison of Network Architectures

This is a comparison of Network Architectures in the accuracy - operations - model_size space.  
The repo will be regularly updated if new network architectures come out. Let me know
if you have any suggestions for architectures to add, or if any relevant data is missing.

This comparison is built on the work done by [Canziani et al](https://arxiv.org/abs/1605.07678).  


## Network Efficiency
'MSD' are [Multi-Scale DenseNets](), 'DN' are [DenseNets](), 'MobNets' are [MobileNets]()


**Figure 1** IMAGENET top-1 accuracy vs #flops, blob size is the model size

<img src="https://raw.githubusercontent.com/BertMoons/Comparing-CNN-Architectures/master/figures/accuracy_ops_modelsize.png">

**Figure 2** IMAGENET top-1 accuracy vs #weights, blob size is the #flops

<img src="https://raw.githubusercontent.com/BertMoons/Comparing-CNN-Architectures/master/figures/accuracy_modelsize_ops.png">


## Remarks

A higher amount of operations or a larger model-size does not necessarily translate in a 
higher __energy consumption__ on an embedded platform. The real relevant comparison point would  
hence be top-1 accuracy vs energy/classification, which is heavily platform dependent.