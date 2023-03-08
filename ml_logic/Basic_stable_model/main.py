import pathlib
import pandas as pd
import numpy as np
from IPython import display
import time
import os
import pathlib
import glob
import zipfile
from io import StringIO
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import get_file
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow import zeros_like, ones_like, function, GradientTape
from tensorflow.train import Checkpoint
from tensorflow.random import normal
from tensorflow.data import Dataset
from tensorflow.keras import utils
from tensorflow.keras.layers import Rescaling
from tensorflow.keras.optimizers import Adam

def make_generator_model() :
    #Establish the sequential model
    model = Sequential()

    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Reshape((7, 7, 256)))

    assert model.output_shape == (None, 7, 7, 256)

    model.add(layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))

    assert model.output_shape == (None, 7, 7, 128)

    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))

    assert model.output_shape == (None, 14, 14, 64)

    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Conv2DTranspose(32, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())
    model.add(layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
    assert model.output_shape == (None, 112, 112, 3)

    return model

def make_discriminator_model():
    model = Sequential([
        layers.Conv2D(128, (5,5), strides=(2, 2), padding='same', input_shape=[112, 112 , 3]),
        layers.MaxPool2D(pool_size = (2,2), padding='same'),
        layers.LeakyReLU(),
        layers.Dropout(0.4),


        layers.Conv2D(64, (3,3), strides = (2,2), padding = 'same'),
        layers.LeakyReLU(),
        layers.Dropout(0.4),

        layers.Flatten(),
        layers.Dense(1, activation = 'tanh')])

    return model

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(ones_like(real_output), real_output)
    fake_loss = cross_entropy(zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss

def generator_loss(fake_output):
    return cross_entropy(ones_like(fake_output), fake_output)

def generate_and_save_images(model, epoch, test_input):
    predictions = model(test_input, training=False)

    fig = plt.figure(figsize=(4, 4))
    for i in range(predictions.shape[0]):
        plt.subplot(4, 4, i+1)
        plt.imshow(predictions[i, :, :, :]*255)
        plt.axis('off')

    plt.savefig(f'image_at_epoch_{epoch}.png',)
    plt.show()

    return

@function
def train_step(images):
    noise = normal([batch_size, noise_dim])

    with GradientTape() as gen_tape, GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))

    return

def train(dataset, epochs):
    for epoch in range(epochs):
        start = time.time()

        print(f'Working on {epoch}')

        for image_batch in dataset:
            train_step(image_batch)

        #Save the model every 100 epochs
        if (epoch + 1) % 100 == 0:
            checkpoint.save(file_prefix = checkpoint_prefix)
            print ('Time for epoch {} is {} sec'.format(epoch + 1, time.time()-start))
            display.clear_output(wait=True)
            generate_and_save_images(generator,epoch + 1, seed)

        display.clear_output(wait=True)
        generate_and_save_images(generator,epochs, seed)
    return

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

##  CHANGE THIS DIRECTORY TO WHEREVER YOU UNZIP YOUR FILES
directory = '/home/paulylydia/code/LimesAndCrimes/project_liminal/ml_logic/Basic_stable_model/test_set_1000/test_1000_set'

batch_size = 8 #Change this to adjust how many images it sees at once (also change somewhere else???)
noise_dim = 100
epochs = 100 #Change these to adjust how long it trains for
num_examples_to_generate = 16

##  USE THIS FUNCTION TO UNZIP OR USE 'UNZIP' FUNCTION IN TERMINAL IN CORRECT DIRECTORY
# with zipfile.ZipFile('test_1000_set.zip', 'r') as zip_ref:
#    zip_ref.extractall('LimesAndCrimes/project_liminal/ml_logic/Basic_stable_model/test_1000')

seed = normal([num_examples_to_generate, noise_dim])

ds = utils.image_dataset_from_directory(
    directory,
    labels=None,
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(112, 112),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False,
)

plt.figure(figsize=(10, 10))
for images in ds.take(1):
    for i in range(batch_size):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.axis("off")
        #plt.savefig(f'image_{i}.png') #size original images if you want

generator = make_generator_model()
discriminator = make_discriminator_model()

cross_entropy = BinaryCrossentropy(from_logits=True)

generator_optimizer = Adam(learning_rate = 0.0001)
discriminator_optimizer = Adam(learning_rate = 0.0001)

checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = Checkpoint(generator_optimizer=generator_optimizer,
                                 discriminator_optimizer=discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)

train(ds, epochs) #saved generated images will appear in a pop up
