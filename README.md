# Task3. StyleGAN sampling 👦🏻⚡👓

1. Найдены проекции изображений в пространстве StyleGAN. К пайплайну из исходного ноутбука добавлен MultiStepLR scheduler. Проведены эксперименты по подбору гиперпараметров:

|Hyperparam|Min|Max|Selected
|---|---|---|---|
|Learning rate|1e-3|5e-2|5e-3|
|Num steps|50|200|164|
|Lpips weight|0.5|10|5|
|Rec weight|0.5|10|2|
|Noise weight|5e-5|5e5|5e-1|

Более подробно ознакомиться с экспериментами можно в [W&B репорте](https://wandb.ai/missmarshal22/deep-gen-hw3/reports/StyleGAN2-latent-space-projections--Vmlldzo3MzUwNTU1).

Результат (гиперпараметры из столбца Selected):
![projections](HW_3.StyleGAN\results\best_params_projections.png)

2. На фото персонажей перенесен стиль с 3 изображений. Проведены эксперименты со следующими гиперпараметрами:

|Hyperparam|Min|Max|Selected
|---|---|---|---|
|Psi|4|10|4|
|Min index|6|10|9|
|Max index|17|18|18|

Наиболее удачный, на мой взгляд, результат (гиперпараметры из столбца Selected):
![style](HW_3.StyleGAN\results\best_params_style.png)


2. На фото персонажей перенесена улыбка. Проведены эксперименты со следующими гиперпараметрами:

|Hyperparam|Min|Max|Selected
|---|---|---|---|
|Psi|4|10|4|
|Min index|0|1|0|
|Max index|15|18|18|

Наиболее удачный, на мой взгляд, результат (гиперпараметры из столбца Selected):
![style](HW_3.StyleGAN\results\best_params_smile.png)

3. Лица персонажей перенесены друг на друга. Проведены эксперименты по подбору гиперпараметров:

|Hyperparam|Min|Max|Selected
|---|---|---|---|
|Learning rate|1e-3|5e-2|5e-3|
|Num steps|50|200|164|
|Arcface weight|0.5|10|5|
|Lpips weight|0.5|10|5|
|Rec weight|0.5|10|2|
|Noise weight|5e-5|5e5|5e-1|

Результат для одного персонажа (гиперпараметры из столбца Selected):

![projections](HW_3.StyleGAN\results\face_swap\ron_best_params_projections.png)

Результаты для других персонажей см. в папке [`HW_3.StyleGAN/results/face_swap`](HW_3.StyleGAN/results/face_swap).

Более подробно ознакомиться с экспериментами можно в [W&B репорте](https://wandb.ai/missmarshal22/deep-gen-hw3-faceswap/reports/StyleGAN2-Arcface-Face-Swap--Vmlldzo3MzUwNzIy).

Весь код в ноутбуке [HW_3.StyleGAN\Stylegan2.ipynb](HW_3.StyleGAN\Stylegan2.ipynb).