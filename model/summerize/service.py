import json
import bentoml
from bentoml.io import JSON

summerizer = bentoml.transformers.load_runner(tag ="sequenceclassification:latest", tasks='summarization')

svc = bentoml.Service("summarize", runners=[summerizer])

@svc.api(input=JSON(), output=JSON())
def predict(json_input: JSON):
	inp = json.loads(json_input)
	result = summerizer.run(inp['sentence'])
	return result