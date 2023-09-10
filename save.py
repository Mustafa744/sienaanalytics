import os, glob
import valohai as vh
import re
import tarfile
import shutil
import zipfile
import time
import tensorflow as tf

# tf.compat.v1.disable_eager_execution()
# meta_file = vh.inputs("trained_model").path("model.ckpt-0.meta")
# checkpoint_dir = vh.inputs("trained_model").path("model.ckpt-0.meta").split("/")[-2]

# saver = tf.compat.v1.train.import_meta_graph(meta_file)

# # checkpoint_dir = "/home/tensorflow/models/research/trained"
# checkpoint = tf.compat.v1.train.latest_checkpoint(checkpoint_dir)

# # Create a TensorFlow 1 session
# with tf.compat.v1.Session() as sess:
#     # Restore the checkpoint variables
#     saver.restore(sess, checkpoint)

#     # Now, the pre-trained weights are loaded into the session

#     # Get the names of all the nodes in the graph
#     all_node_names = [
#         n.name for n in tf.compat.v1.get_default_graph().as_graph_def().node
#     ]

#     # Freeze the entire TensorFlow 1 graph
#     frozen_graph_def = tf.compat.v1.graph_util.extract_sub_graph(
#         sess.graph_def, all_node_names
#     )

#     # Replace 'frozen_graph.pb' with the desired output pb file path
#     pb_file_path = f"""{vh.outputs().path("frozen_graph.pb")}"""
#     with tf.io.gfile.GFile(pb_file_path, "wb") as f:
#         f.write(frozen_graph_def.SerializeToString())


input_path = valohai.inputs("trained_model").path()
with valoha.metadata.logger() as logger:
    logger.log("input path", input_path)
    logger.log("input directory content: ", os.listdir(input_path))
