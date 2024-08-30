# CMD = """lm_eval --model hf \
#     --model_args pretrained={model} \
#    --tasks halftruthdetection \
#     --device cuda:0 \
#     --batch_size 8
# """
# yaml_path = "/usr/src/app/lm_eval/tasks/my_dataset/halftruthdetection.yaml"
# models = {
#     "llama3": "meta-llama/Meta-Llama-3-8B" ,
#     "mistrl-v2-base": "mistral-community/Mistral-7B-v0.2",
#     "gemma": "google/gemma-7b",
#     "mistralinstruct": "mistralai/Mistral-7B-Instruct-v0.2",
#     "llama3instruct": "meta-llama/Meta-Llama-3-8B-Instruct",
#     "gemmainstruct": "google/gemma-7b-it"
# }
# lm_eval --model hf \
#     --model_args pretrained=meta-llama/Meta-Llama-3-8B \
#     --tasks halftruthdetection \
#     --device cuda:0 \
#     --apply_chat_template \
#     --batch_size 8
    
# lm_eval --model hf \--model_args pretrained=mistralai/Mistral-7B-Instruct-v0.2 \--tasks halftruthdetectionfewshot \--device cuda:0 \--batch_size 8 > output/gemma/instruct/p1.txt 2>&1

# # INSTRUCT
# lm_eval --model hf \--model_args pretrained=google/gemma-7b-it \--tasks halftruthdetectionfewshot \--device cuda:1 \--batch_size 2 > output/few\(5\)_shot/gemma/instruct/p7.log 2>&1
# lm_eval --model hf \--model_args pretrained=meta-llama/Meta-Llama-3-8B-Instruct \--tasks halftruthdetectionfewshot \--device cuda:1 \--batch_size 2 > output/few\(5\)_shot/llama/instruct/p5.log 2>&1
# lm_eval --model hf \--model_args pretrained=mistralai/Mistral-7B-Instruct-v0.2 \--tasks halftruthdetectionfewshot \--device cuda:0 \--batch_size 2 > output/few\(5\)_shot/mistral/instruct/p7.txt 2>&1
# # BASE
# lm_eval --model hf \--model_args pretrained=google/gemma-7b \--tasks halftruthdetectionfewshot \--device cuda:0 \--batch_size 8 > output/few\(5\)_shot/gemma/base/p3.txt 2>&1
# lm_eval --model hf \--model_args pretrained=mistral-community/Mistral-7B-v0.2 \--tasks halftruthdetectionfewshot \--device cuda:0 \--batch_size 8 > output/few\(5\)_shot/mistral/base/p3.txt 2>&1
# lm_eval --model hf \--model_args pretrained=meta-llama/Meta-Llama-3-8B \--tasks htdetection \--device cuda:1 \--batch_size 8 > output/staticQA2/llama/base 2>&1
# lm_eval --model hf \--model_args pretrained=meta-llama/Meta-Llama-3-8B \--tasks htdetection \--device cuda:1 \--batch_size 8 > output/staticQA2/llama/base 2>&1

# Gemma 27B model

# CUDA_VISIBLE_DIVICES=4,1,6,7 accelerate launch -m lm_eval --model hf \--model_args pretrained=google/gemma-2-27b,parallelize=True \--tasks halftruthdetection \--batch_size 1 > gemma_2_27b_val_P1.log 2>&1
# accelerate launch -m lm_eval --model hf \--model_args pretrained=google/gemma-2-27b,parallelize=True \--tasks halftruthdetection \--batch_size 1 > gemma_2_27b_val_P1.log 2>&1

# Run parallel on all GPU available
# lm_eval --model hf \--model_args pretrained=google/gemma-2-27b,parallelize=True \--tasks halftruthdetection \--batch_size 1 > gemma_2_27b_val_P1.log 2>&1
# normal run on single GPU
# lm_eval --model hf \--model_args pretrained=google/gemma-2-27b \--tasks halftruthdetection \--device cuda:2 \--batch_size 1 > gemma_2_27b_val_P1.log 2>&1