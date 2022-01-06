import subprocess


class Compressor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def compress(self, input_file):
        result = subprocess.run([
            "ffmpeg", "-n", "-i", f"./{self.input_dir}/{input_file}", "-vcodec", "libx264", "-crf", "24", f"./{self.output_dir}/finished_{input_file}"
        ])
