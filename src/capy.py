from capymoa.datasets import Electricity
from capymoa.evaluation import ClassificationEvaluator
from capymoa.classifier import OnlineBagging

elec_stream = Electricity()
ob_learner = OnlineBagging(schema=elec_stream.get_schema(), ensemble_size=5)
ob_evaluator = ClassificationEvaluator(schema=elec_stream.get_schema())

for instance in elec_stream:
    prediction = ob_learner.predict(instance)
    ob_learner.train(instance)
    ob_evaluator.update(instance.y_index, prediction)

print(ob_evaluator.accuracy())