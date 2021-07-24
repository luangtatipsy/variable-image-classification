from typing import Tuple

from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from tensorflow.keras.models import Model


def create_fixed_input_shape_model(
    image_size: Tuple[int, int], num_classes: int
) -> Model:
    xception = Xception(
        input_shape=(*image_size, 3), include_top=False, weights="imagenet"
    )
    for layer in xception.layers:
        layer.trainable = False

    output = xception.output

    x = Flatten()(output)
    x = Dense(256, activation="relu")(x)
    x = Dropout(0.4)(x)

    prediction = Dense(num_classes, activation="softmax")(x)

    return Model(inputs=xception.input, outputs=prediction)


def create_variable_input_shape_model(num_classes: int) -> Model:
    xception = Xception(
        input_shape=(None, None, 3), include_top=False, weights="imagenet"
    )
    for layer in xception.layers:
        layer.trainable = False

    output = xception.output

    x = GlobalAveragePooling2D()(output)
    x = Dense(256, activation="relu")(x)
    x = Dropout(0.4)(x)

    prediction = Dense(num_classes, activation="softmax")(x)

    return Model(inputs=xception.input, outputs=prediction)
