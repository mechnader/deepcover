# DeepCover: Uncover the Truth Behind AI

![alt text](images/deepcover-logo.png)

DeepCover explains image classifiers using [statistical fault localization](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730392.pdf) and 
[causal theory](https://openaccess.thecvf.com/content/ICCV2021/papers/Chockler_Explanations_for_Occluded_Images_ICCV_2021_paper.pdf).

Videos: [ECCV2020](https://www.youtube.com/watch?v=vTyfOBAGm_o), [ICCV2021](https://www.cprover.org/deepcover/iccv2021/iccv2021-talk-compatible.mp4) 

# Install and Setup
### Create conda envirronement
```
conda create -n deepcover python
```
#### Install requirements
```
pip install -r requirement.txt
```

# Hello DeepCover
```
python ./src/deepcover.py --help
usage: deepcover.py [-h] [--model MODEL] [--inputs DIR] [--outputs DIR]
                    [--measures  [...]] [--measure MEASURE] [--mnist-dataset]
                    [--normalized-input] [--cifar10-dataset] [--grayscale]
                    [--vgg16-model] [--inception-v3-model] [--xception-model]
                    [--mobilenet-model] [--attack] [--text-only]
                    [--input-rows INT] [--input-cols INT]
                    [--input-channels INT] [--x-verbosity INT]
                    [--top-classes INT] [--adversarial-ub FLOAT]
                    [--adversarial-lb FLOAT] [--masking-value INT]
                    [--testgen-factor FLOAT] [--testgen-size INT]
                    [--testgen-iterations INT] [--causal] [--wsol FILE]
                    [--occlusion FILE]
```


## To start running the Statistical Fault Localization (SFL) based explaining:
```
python ./src/deepcover.py --mobilenet-model --inputs data/panda --outputs outs --testgen-size 200
```
`--mobilenet-model`   pre-trained keras model 

`--inputs`            input images folder

`--outputs`           output images folder

`--testgen-size`      the number of input mutants to generate for explaining (by default, it is 2,000) 


## More options
```
python src/deepcover.py --mobilenet-model --inputs data/panda/ --outputs outs --measures tarantula zoltar --x-verbosity 1 --masking-value 0
```
`--measures`      to specify the SFL measures for explaining: tarantula, zoltar, ochiai, wong-ii

`--x-verbosity`   to control the verbosity level of the explanation results

`--masking-value` to control the masking color for mutating the input image


## To load your own model
```
python src/deepcover.py --model models/gtsrb_backdoor.h5 --input-rows 32 --input-cols 32 --inputs data/gtsrb/ --outputs outs
```
`--input-rows`    row number for the input image

`--input-cols`    column number for the input image



# Publications
```
@inproceedings{sck2021,
  AUTHOR    = { Sun, Youcheng
                and Chockler, Hana
                and Kroening, Daniel },
  TITLE     = { Explanations for Occluded Images },
  BOOKTITLE = { International Conference on Computer Vision (ICCV) },
  PUBLISHER = { IEEE },
  PAGES     = { 1234--1243 },
  YEAR = { 2021 }
}
```
```
@inproceedings{schk2020,
AUTHOR = { Sun, Youcheng
and Chockler, Hana
and Huang, Xiaowei
and Kroening, Daniel},
TITLE = {Explaining Image Classifiers using Statistical Fault Localization},
BOOKTITLE = {European Conference on Computer Vision (ECCV)},
YEAR = { 2020 }
}
```

# Miscellaneous
[Roaming Panda Dataset](https://github.com/theyoucheng/deepcover/tree/master/roaming-panda/)

[Photo Bombing Dataset](https://github.com/theyoucheng/deepcover/tree/master/data/photobombing/)

[DeepCover Site](https://www.cprover.org/deepcover/)
