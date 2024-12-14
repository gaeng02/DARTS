# RobustDARTS
Code accompanying the paper:
> [Understanding and Robustifying Differentiable Architecture Search](https://openreview.net/forum?id=H1gDNyrKDS)\
> Arber Zela, Thomas Elsken, Tonmoy Saikia, Yassine Marrakchi, Thomas Brox and Frank Hutter.\
> _In: International Conference on Learning Representations (ICLR 2020)_.


# Codebase
The code is basically based on the original [DARTS implementation](https://github.com/quark0/darts).  
The original code before modification is [RobustDARTS](https://github.com/automl/RobustDARTS).   
Check [NOTICE file](./NOTICE.md). 


## Requirements
```
Python >= 3.5.5, PyTorch == 0.3.1, torchvision == 0.2.0
```

## Modification 
```
- scripts/DARTS_search.sh
- scripts/DARTS_eval.sh 
> Convert to fit the experimental environment. 
```
```
- src/search/model_search.py
> Change the number of "Search Edges". (default : 2)
> Append with node and weight. 
```
```
- src/evaluation/model.py
> Consider with Search Edges's drop_prob. 
```
```
- src/evaluation/train.py
> Evaluate time for evaluation. (Consider batch size and epochs)
```
```
- src/timer.py
> Parse time sign. 
```