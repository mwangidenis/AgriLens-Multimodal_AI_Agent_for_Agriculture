# Prototype Demo: AgriLens Multimodal Agent

from PIL import Image
from agrilens.image_utils import analyze_image
from agrilens.text_utils import generate_response
import pandas as pd
import matplotlib.pyplot as plt

# Load and analyze image
image = Image.open("maize_leaf.jpg")
image_result = analyze_image(image)
print("Image Analysis:", image_result)

# Run prompt
prompt = "Is this maize leaf healthy?"
response = generate_response(prompt, image_result)
print("LLM Response:", response)

# Load farm records
df = pd.read_csv("farm_records.csv")
maize_df = df[df["Crop"] == "Maize"]
maize_df.plot(x="Date", y="Yield (kg)", kind="line", title="Maize Yield Over Time")
plt.show()