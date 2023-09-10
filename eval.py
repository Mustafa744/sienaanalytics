import valohai as vh
import tensorflow as tf

# # load frozen graph
# with tf.gfile.GFile("./frozen_graph.pb", "rb") as f:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())

# # print graph information
# for node in graph_def.node:
#     print(node)
# #####################################################################
# import tensorflow as tf


# # Create a summary file to describe the graph
# summary_file_path = "./graph_summary.pbtxt"
# with open(summary_file_path, "w") as summary_file:
#     summary_file.write(str(graph_def))


with vh.metadata.logger() as logger:
    logger.log("attempting to load model", vh.inputs("frozen_model").path())
    try:
        # Load the frozen graph
        with tf.gfile.GFile("./frozen_graph.pb", "rb") as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
        logger.log("model loaded")
    except Exception as e:
        logger.log("failed to load model", str(e))
