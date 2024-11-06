# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from generate_image import ImageGenerator

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Safetensors Image Generator")
        self.root.geometry("400x250")

        # モデルの読み込み
        self.model_path = None

        # モデルファイルの選択ボタン
        self.model_button = tk.Button(root, text="Load safetensors model", command=self.load_model)
        self.model_button.pack(pady=10)

        # プロンプト入力
        self.prompt_label = tk.Label(root, text="Enter prompt:")
        self.prompt_label.pack(pady=5)
        self.prompt_entry = tk.Entry(root, width=50)
        self.prompt_entry.pack(pady=5)

        # 出力先ファイル名の入力
        self.output_label = tk.Label(root, text="Output filename:")
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(root, width=50)
        self.output_entry.insert(0, "generated_image.png")
        self.output_entry.pack(pady=5)

        # 生成ボタン
        self.generate_button = tk.Button(root, text="Generate Image", command=self.generate_image)
        self.generate_button.pack(pady=10)

    def load_model(self):
        self.model_path = filedialog.askopenfilename(filetypes=[("safetensors files", "*.safetensors")])
        if self.model_path:
            self.generator = ImageGenerator(self.model_path)
            messagebox.showinfo("Model Loaded", f"Loaded model from {self.model_path}")

    def generate_image(self):
        if not self.model_path:
            messagebox.showerror("Error", "Please load a safetensors model first.")
            return

        prompt = self.prompt_entry.get()
        output_path = self.output_entry.get()

        if not prompt:
            messagebox.showerror("Error", "Prompt cannot be empty.")
            return

        try:
            result_path = self.generator.generate_image(prompt, output_path)
            messagebox.showinfo("Success", f"Image saved to {result_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()
