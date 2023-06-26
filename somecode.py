import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"past_user_inputs": ["Which movie is the best ?"],
		"generated_responses": ["It's Die Hard for sure."],
		"text": "Can you explain why ?"
	},
})