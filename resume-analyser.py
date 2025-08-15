from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen2.5-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

resume_text = open("resume.txt").read()

prompt = f"""
You are an ATS scoring assistant.
Extract the following from this resume:
- Candidate name
- Contact details
- Skills (group into Technical, Soft, Domain-specific)
- Work experience (company, role, duration, achievements)
- Education
Then generate a rewritten ATS-optimized resume with keywords for 'Full Stack Developer'.

Resume:
{resume_text}
"""

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
