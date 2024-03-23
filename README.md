# Task 2. Имплементация GAN 📸⭐👱‍♀️
# Ход работы:
- [X] Имплементирован CSPup блок
- [X] Имплементировать генератор GAN, состоящий из CSPup блоков
- [X] Имплементированный GAN обучен на датасете CelebA
- [X] Проведены эксперименты с целью достижения сходимости
      
**[Ноутубук с обучением](https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_2/gan-celeba.ipynb).**

# Эксперименты
Было проведено более **40** экспериментов, включабщих в себя:
- Изменение **learning rate**: уменьшение для дискриминатора и/или увеличение для генератора, использование шедулера
- Добавление **регуляризации** (изменение параметра weight decay) для дискриминатора и в некоторых случаях генератора
- Использование оптимизатора **SGD** (вместо Adam) для дискриминатора
- Увеличение **частоты обучения генератора** в X раз (где X= 2 или X=5): на каждом шаге дискриминатор обучался 1 раз, а генератор X раз подряд
- Изменение фаункции активации генератора на **Tanh** (вместо Leaky ReLU)
- Изменение **размера скрытого пространства**

**Подробнее ознакомиться с результатами можно в [W&B репорте](https://wandb.ai/missmarshal22/deep-gen-hw2/reports/GAN-CelebA-report--Vmlldzo3MjY4MjI5?accessToken=0s6jpvs19f92bd7bsbo24ndv2ydm15blclx2ks4l4j5brgexpf4n8ku7kgddg6fm).**

# Пример эксперимента

|Hyperparam|Value|
|---|---|
|Discriminator_lr|0.0002|
|Generator lr|0.0004|
|Discriminator weight decay|0.0001|
|Epochs|15|
|Latent space size|200|
|Generator activation function| Tanh|

Лоссы генератора (🟦) и дискриминатора (🟧) для этого эксперимента.

![losses](https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_2/charts/rare-microwave-77.png)

Изображения, полученные в этом эксперименте.

![images](https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_2/images/rare-microwave-77.png)


