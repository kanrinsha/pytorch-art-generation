from __future__ import print_function

import copy
import glob
import os
import os.path
import random

import torch
from PIL import Image


class ArtMoment:
    verbose = False
    seed = 10000
    # rgb = 3 bw = 1
    channels = 1
    radius = False
    bias = False
    device = 'cpu'
    z = None
    xlim = [-1.0, 1.0]
    xres = 2048
    depth = 8
    hidden_std = 1.0
    output_std = 1.0
    image_name_to_save = 'test.png'

    @property
    def get_devices(self):
        devices = ['cpu']
        return tuple(devices)

    def render(self, units=16):
        if self.device not in self.get_devices:
            raise RuntimeError('Device {} not in available devices: {}'.format(
                self.device, ', '.join(self.get_devices)))

        cpu_rng_state = torch.get_rng_state()

        torch.cuda.manual_seed_all(self.seed)
        torch.manual_seed(self.seed)

        ylim = copy.copy(self.xlim)

        yxscale = float(ylim[1] - ylim[0]) / (self.xlim[1] - self.xlim[0])
        yres = int(yxscale * self.xres)

        x = torch.linspace(self.xlim[0], self.xlim[1], self.xres, device=self.device)
        y = torch.linspace(ylim[0], ylim[1], yres, device=self.device)
        grid = torch.meshgrid([y, x])

        inputs = torch.cat((grid[0].flatten().unsqueeze(1), grid[1].flatten().unsqueeze(1)), -1)

        if self.radius:
            inputs = torch.cat((inputs, torch.norm(inputs, 2, 1).unsqueeze(1)), -1)

        if self.z is not None:
            zrep = torch.tensor(self.z, dtype=inputs.dtype, device=self.device).repeat((inputs.shape[0], 1))
            inputs = torch.cat((inputs, zrep), -1)

        n_hidden_units = [units] * self.depth

        activations = inputs
        for units in n_hidden_units:
            if self.bias:
                bias_array = torch.ones((activations.shape[0], 1), device=self.device)
                activations = torch.cat((bias_array, activations), -1)
            hidden_layer_weights = torch.randn((activations.shape[1], units), device=self.device) * self.hidden_std
            activations = torch.tanh(torch.mm(activations, hidden_layer_weights))

        if self.bias:
            bias_array = torch.ones((activations.shape[0], 1), device=self.device)
            activations = torch.cat((bias_array, activations), -1)
        output_layer_weights = torch.randn((activations.shape[1], self.channels), device=self.device) * self.output_std
        output = torch.sigmoid(torch.mm(activations, output_layer_weights))
        output = output.reshape((yres, self.xres, self.channels))

        torch.set_rng_state(cpu_rng_state)

        return (output.cpu() * 255).round().type(torch.uint8).numpy()

    def main_call(self):
        colourise = 'rgb' if self.channels != 1 else 'b&w'
        if self.seed is None:
            self.seed = random.randint(0, 999999)
        if self.verbose:
            print('Seed: {}'.format(self.seed))
            print(f'Color: {colourise}')
            print('Starting render...')
        im = Image.fromarray(self.render().squeeze())

        if self.image_name_to_save == ".png":
            self.image_name_to_save = "untitled.png"

        im.save('images/' + self.image_name_to_save, 'png')
        print('Render finished...')

        im = Image.open('images/' + self.image_name_to_save)

        im.show()


def main_render():
    init = ArtMoment()
    init.main_call()


def make_gif(log):
    frames = [Image.open(image) for image in glob.glob(f"{'images/frames'}/*.png")]
    frame_one = frames[0]
    frame_one.save("render_gif.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)
    frames_path = "images/frames/"
    if log:
        for root, dirs, files in os.walk(frames_path):
            for file in files:
                os.remove(os.path.join(root, file))


if __name__ == '__main__':
    main_render()
