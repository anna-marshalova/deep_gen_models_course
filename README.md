# Task4. Stable Diffusion training

1. Собран датасет из 19 изображений одного персонажа. Пример изображения (чтобы понимать как выглядит человек для сравнения с генерациями):
[!reference]()
2. Обучен чекпоинт модели Stable diffusion 1.5. Примеры генераций см. в таблице 1
3. Обучена LoRA. Проведены эксперименты с rank = 2, 4, 16, 128, 256. Примеры генераций см. в таблице 1
   
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
<td>a portrait portrait of sks woman, with a laced collar, in a victorian mansion, standing, 4k, hd, extremely detailed, beautiful, high quality, realism, sharp focus</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/dreambooth/mansion.jpg' alt = 'mansion_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_2/mansion.jpg' alt = 'mansion_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_16/mansion.jpg' alt = 'mansion_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/lora/lora_128/mansion.jpg' alt = 'mansion_lora_128' ></td>
</tr>


</table>

В пайплайн добавлен ControlNet. Примеры генераций см. в таблице 2
   
<p>Таблица 2. Примеры генераций ControlNet. Для всех генераций использовались следующие параметры: <code>num_inference_steps=20, guidance_scale=7, seed=42, negative_prompt="monochrome, lowres, bad anatomy, worst quality, low quality"</code>.</p>


<table>
<th>
<td  >Prompt</td>
<td >Dreambooth</td>
<td >LoRA (rank=2)</td>
<td >LoRA (rank=16)</td>
<td >LoRA (rank=128)</td>
</th>
<tr>
<td>mona_lisa</td>
<td>portrait of sks woman face, best quality, extremely detailed, 4k, hdr, super resolution</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/dreambooth/mona_lisa.jpg' alt = 'mona_lisa_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_2/mona_lisa.jpg' alt = 'mona_lisa_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_16/mona_lisa.jpg' alt = 'mona_lisa_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_128/mona_lisa.jpg' alt = 'mona_lisa_lora_128' ></td>
<tr>
<td>pearl_earring</td>
<td>portrait of sks woman face, best quality, extremely detailed, 4k, hdr, super resolution</td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/dreambooth/pearl_earring.jpg' alt = 'pearl_earring_dreambooth' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_2/pearl_earring.jpg' alt = 'pearl_earring_lora_2' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_16/pearl_earring.jpg' alt = 'pearl_earring_lora_16' ></td>
<td><img src='https://github.com/anna-marshalova/deep_gen_models_course/blob/homework_4/HW_4.StableDiffusion/report_images/controlnet/lora/lora_128/pearl_earring.jpg' alt = 'pearl_earring_lora_128' ></td>
</tr>


</table>