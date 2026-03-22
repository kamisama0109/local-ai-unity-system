class LLMManager:
    def __init__(self):
        self.models = {'qwen': 'path/to/qwen_model', 'phi-3': 'path/to/phi3_model'}
        self.current_model = 'qwen'

    def switch_model(self, model_name):
        if model_name in self.models:
            self.current_model = model_name
            print(f'Switched to {model_name}')
        else:
            print(f'Model {model_name} not found!')

    def get_current_model(self):
        return self.current_model

    def run_inference(self, input_data):
        # Logic for running inference based on the current model
        return f'Running inference on {self.current_model} with input: {input_data}.'