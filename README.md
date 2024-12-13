# RobustDARTS
Code accompanying the paper:
> [Understanding and Robustifying Differentiable Architecture Search](https://openreview.net/forum?id=H1gDNyrKDS)\
> Arber Zela, Thomas Elsken, Tonmoy Saikia, Yassine Marrakchi, Thomas Brox and Frank Hutter.\
> _In: International Conference on Learning Representations (ICLR 2020)_.

# Codebase
The code is basically based on the original [DARTS implementation](https://github.com/quark0/darts).

## Requirements
```
Python >= 3.5.5, PyTorch == 0.3.1, torchvision == 0.2.0
```

## Modification
- scripts/DARTS_search.sh
- scripts/DARTS_eval.sh
- src/search/model_search.py
- src/evaluation/model.py
- src/evaluation/train.py

## Citation
```bibtex
@inproceedings{zela2020understanding,
	title={Understanding and Robustifying Differentiable Architecture Search},
	author={Arber Zela and Thomas Elsken and Tonmoy Saikia and Yassine Marrakchi and Thomas Brox and Frank Hutter},
	booktitle={International Conference on Learning Representations},
	year={2020},
	url={https://openreview.net/forum?id=H1gDNyrKDS}
}
```
