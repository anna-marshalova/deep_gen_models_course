import os

import numpy as np
from PIL import Image
from tqdm.auto import trange


class AvatarGenerator:
    def __init__(self, saving_dir: str = "generated_images",
                 dtype: type = np.float16,
                 epsilon: float = 0.01):
        self.PAD_VALUE = -1
        self.dtype = dtype
        self.saving_dir = saving_dir
        self.epsilon = epsilon
        self.images = None
        self.img_shape = None
        self.probs = None

    def get_probs(self):
        probs = np.zeros((*self.img_shape, 256), dtype=self.dtype)
        for x in trange(self.img_shape[0]):
            for y in range(self.img_shape[1]):
                for z in range(self.img_shape[2]):
                    variants = self.images[:, x, y, z]
                    counts = np.array(
                        np.bincount(variants, minlength=256), dtype=self.dtype
                    )
                    # apply MLE
                    counts += self.epsilon
                    channel_probs = counts / sum(counts)
                    probs[x, y, z, :] = channel_probs
        return probs

    def fit(self, images: np.ndarray):
        self.images = images
        self.img_shape = images.shape[1:]
        self.probs = self.get_probs()

    def generate(self, convert_colors: bool = True, show: bool = True,
                 save: bool = False):
        log_prob = 0
        new_img = np.zeros(self.img_shape)

        for x in trange(self.img_shape[0]):
            for y in range(self.img_shape[1]):
                for z in range(self.img_shape[2]):
                    pixel_probs = self.probs[x, y, z, :]
                    channel_value = np.random.choice(np.arange(256),
                                                     p=pixel_probs)
                    channel_prob = pixel_probs[channel_value]
                    new_img[x, y, z] = channel_value
                    log_prob += np.log(channel_prob)

        prob = np.exp(log_prob)
        if convert_colors:
            new_img = new_img[:, :, ::-1]
        image = Image.fromarray(np.uint8(new_img))
        if show:
            display(image)
            print(f"The probability of this image is: {prob}.")
            print(f"The log-probability is {log_prob}.")
        if save:
            self.save_image(image)
        return image, prob

    def generate_image_path(self, n: int):
        return os.path.join(self.saving_dir, f"{n}.png")

    def save_image(self, image: Image.Image):
        if self.saving_dir:
            os.makedirs(self.saving_dir, exist_ok=True)
        n = 1
        path = self.generate_image_path(n)
        while os.path.exists(path):
            n += 1
            path = self.generate_image_path(n)
        image.save(path)
