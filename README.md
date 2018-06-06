# Generative Adversarial Imitation Learning  
Implementation of Generative Adversarial Imitation Learning(GAIL) using tensorflow  

## Dependencies
python>=3.5  
tensorflow>=1.4   
gym>=0.9.3  

## Gym environment

Env==CartPole-v0  
State==Continuous  
Action==Discrete  

## Usage

**Train experts**  
```  
python3 run_ppo.py     
```  
**Sample trajectory using expert** 
```
python3 sample_trajectory.py
```
**Run GAIL**  
```
python3 run_gail.py  
```
**Run supervised learning**  
```
python3 run_behavior_clone.py 
```
**Test trained policy**  
```
python3 test_policy.py  
```
Default policy is trained with gail  
--alg=bc or ppo allows you to change test policy  

If you want to test bc policy, specify the _number_ of model.ckpt-_number_ in the directory trained_models/bc  
Example  
```
python3 test_policy.py --alg=bc --model=1000
```
**Tensorboard**  
```
tensorboard --logdir=log
```

## Results

| ![](./images/graph.png) | ![](./images/legend.png) |  
| :---: | :---: |  
| Fig.1 Training results | legend |  

## LICENSE
MIT LICENSE
