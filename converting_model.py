import tensorflow as tf
model = tf.keras.models.load_model("fake_job_detection.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS, 
  tf.lite.OpsSet.SELECT_TF_OPS    
]

converter._experimental_lower_tensor_list_ops = False
tflite_model = converter.convert()

with open("fake_job_detection.tflite", "wb") as f:
    f.write(tflite_model)