from typing import Tuple

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Model


def create_model(image_size: Tuple[int, int], num_classes: int) -> Model:
    mobilenet_v2 = MobileNetV2(
        input_shape=(*image_size, 3), include_top=False, weights="imagenet"
    )
    for layer in mobilenet_v2.layers:
        layer.trainable = False

    output = mobilenet_v2.output

    x = Flatten()(output)
    x = Dense(1024, activation="relu")(x)
    x = Dropout(0.2)(x)

    prediction = Dense(num_classes, activation="softmax")(x)

    return Model(inputs=mobilenet_v2.input, outputs=prediction)
