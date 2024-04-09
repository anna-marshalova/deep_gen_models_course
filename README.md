# Task4. Stable Diffusion training

1. Собран датасет из 19 изображений одного персонажа. Пример изображения (для сравнения с генерациями):
   
<img alt="reference" src="https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/reference.jpg" width="300px">

2. Обучен чекпоинт модели Stable diffusion 1.5. Примеры генераций см. в таблице 1
3. Обучена LoRA. Проведены эксперименты с rank = 2, 16, 128. Примеры генераций см. в таблице 1
   
<p>Таблица 1. Примеры генераций модели. Для всех генераций использовались следующие параметры: <code>num_inference_steps=35, guidance_scale=7, seed=42, negative_prompt="naked, nsfw, deformed, distorted, disfigured, poorly drawn, bad anatomy, extra limb, missing limb, floating limbs, mutated hands disconnected limbs, mutation, ugly, blurry, amputation"</code>.</p>

<table>
<th>
<td  >Prompt</td>
<td >Dreambooth</td>
<td >LoRA (rank=2)</td>
<td >LoRA (rank=16)</td>
<td >LoRA (rank=128)</td>
</th>
<tr>
<td>garden</td>
<td>photo of sks woman face, wearing jeans, in a graden with many plants and flowers, standing, smiling, 4k, sunny lighting, raw, hrd, hd, high quality, realism, sharp focus, beautiful, detailed eyes</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/dreambooth/garden.jpg' alt = 'garden_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_2/garden.jpg' alt = 'garden_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_16/garden.jpg' alt = 'garden_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_128/garden.jpg' alt = 'garden_lora_128' ></td>
</tr>

<tr>
<td>computer game</td>
<td>close-up portrait of sks woman, in a teenage room, unreal engine, artstation, detailed, cinematic, hyperrealistic, octane render, daz, unreal 5</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/dreambooth/computer%20game.jpg' alt = 'computer game_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_2/computer%20game.jpg' alt = 'computer game_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_16/computer%20game.jpg' alt = 'computer game_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_128/computer%20game.jpg' alt = 'computer game_lora_128' ></td>
</tr>

<tr>
<td>mansion</td>
<td>a portrait of sks woman, with a laced collar, in a victorian mansion, standing, 4k, hd, extremely detailed, beautiful, high quality, realism, sharp focus</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/dreambooth/mansion.jpg' alt = 'mansion_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_2/mansion.jpg' alt = 'mansion_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_16/mansion.jpg' alt = 'mansion_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_128/mansion.jpg' alt = 'mansion_lora_128' ></td>
</tr>


</table>

4. В пайплайн добавлен ControlNet. Примеры генераций см. в таблице 2
   
<p>Таблица 2. Примеры генераций ControlNet. Для всех генераций использовались следующие параметры: <code>num_inference_steps=35, guidance_scale=9, seed=20240410, negative_prompt="monochrome, lowres, bad anatomy, worst quality, low quality"</code>.</p>


<table>
<th>
<td width='200px'>Prompt</td>
<td>Reference</td><td width='200px'>Dreambooth</td>
<td width='200px'>LoRA (rank=2)</td>
<td width='200px'>LoRA (rank=16)</td>
<td width='200px'>LoRA (rank=128)</td>
</th>
<tr>
<td>mona_lisa</td>
<td>portrait of sks woman face, best quality, extremely detailed, 4k, hdr, super resolution</td>
<td><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/1024px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg' alt = 'mona_lisa_reference' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/dreambooth/mona_lisa.jpg' alt = 'mona_lisa_dreambooth' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_2/mona_lisa.jpg' alt = 'mona_lisa_lora_2' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_16/mona_lisa.jpg' alt = 'mona_lisa_lora_16' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_128/mona_lisa.jpg' alt = 'mona_lisa_lora_128' width='200px'></td>
<tr>
<td>pearl_earring</td>
<td>portrait of sks woman face, best quality, extremely detailed, 4k, hdr, super resolution</td>
<td><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/1665_Girl_with_a_Pearl_Earring.jpg/800px-1665_Girl_with_a_Pearl_Earring.jpg' alt = 'pearl_earring_reference' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/dreambooth/pearl_earring.jpg' alt = 'pearl_earring_dreambooth' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_2/pearl_earring.jpg' alt = 'pearl_earring_lora_2' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_16/pearl_earring.jpg' alt = 'pearl_earring_lora_16' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_128/pearl_earring.jpg' alt = 'pearl_earring_lora_128' width='200px'></td>
</tr>
<tr>
<td>peaches</td>
<td>portrait of sks woman face, best quality, extremely detailed, 4k, hdr, super resolution</td>
<td><img src='https://static.tildacdn.com/tild3230-3566-4334-a135-303835333033/photo.png' alt = 'peaches_reference' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/dreambooth/peaches.jpg' alt = 'peaches_dreambooth' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_2/peaches.jpg' alt = 'peaches_lora_2' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_16/peaches.jpg' alt = 'peaches_lora_16' width='200px'></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_128/peaches.jpg' alt = 'peaches_lora_128' width='200px'></td>
</tr>


</table>

Ноутбук с обучение и экспериментами: [HW_4.StableDiffusion/DreamBooth_Stable_Diffusion.ipynb](https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/DreamBooth_Stable_Diffusion.ipynb)


# Выводы
Почти во всех экспериментах (кроме разве что `computer game`) генерации обученного чекпоинта оказались лучше, чем генерации LoRA: они больше похожи на оригинал и в целом в большинстве случаев более качественные и реалистичные. 

Для LoRA сходство с оригиналом растет с ростом ранга. LoRA с рангом 2 генерирует качественные изображения, но имеющие мало общего с человеком, на фотографиях которого она обучалась. Изображения, сгенерированные LoRA с раногом 128, уже куда больше похожи на оригинал, но, на мой взгляд, до качества чекпоинта все равно не дотягивают. 