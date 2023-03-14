import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow import keras
from liminal.model.model import DiffusionModel
from liminal.params import *
from tensorflow import constant

def load_model(biome, resolution) -> keras.Model:
    """
    Load model and weights
    """

    image_size = resolution

    # Instantiate new model
    model = DiffusionModel(image_size, widths, block_depth)
    model.compile(
        optimizer=keras.optimizers.experimental.AdamW(
            learning_rate=learning_rate, weight_decay=weight_decay
            ),
        loss=keras.losses.mean_absolute_error
        )

    # Load weights depending in chosen biom
    # Manually set the mean and variance for normalization
    if resolution == 256:
        if biome == 'white':
            model_test_path = 'liminal/weights/model_white_199'
            model.load_weights(model_test_path)
            model.normalizer.mean = constant([[0.51309836, 0.52594155, 0.52296096]])
            model.normalizer.variance = constant([[0.1767919, 0.16620675, 0.15951076]])
            print(f"✅ model white and its according weights loaded")
        elif biome == 'yellow':
            model_test_path = 'liminal/weights/model_yellow_200'
            model.load_weights(model_test_path)
            model.normalizer.mean = constant([[0.3249119, 0.30422544, 0.23189466]])
            model.normalizer.variance = constant([[0.11593834, 0.06254298, 0.02535429]])
            print(f"✅ model yellow and its according weights loaded")
        elif biome == 'green':
            model_test_path = 'liminal/weights/model_green_520'
            model.load_weights(model_test_path)
            model.normalizer.mean = constant([[0.14924264, 0.22114924, 0.16808464]])
            model.normalizer.variance = constant([[0.03553014, 0.02721066, 0.01141845]])
            print(f"✅ model green and its according weights loaded")
        elif biome == 'mix':
            model_test_path = 'liminal/weights/model_mix_220'
            model.load_weights(model_test_path)
            model.normalizer.mean = constant([[0.25518528, 0.27833208, 0.229785]])
            model.normalizer.variance = constant([[0.10151546, 0.0598723, 0.03199953]])
            print(f"✅ model mix and its according weights loaded")
    elif resolution == 512:
        model_test_path = 'liminal/weights/model_512_309'
        model.load_weights(model_test_path)
        model.normalizer.mean = constant([[0.2347412, 0.29770762, 0.24761508]])
        model.normalizer.variance = constant([[0.07756928, 0.05185926, 0.03695022]])
        print(f"✅ model 512 and its according weights loaded")

    return model
