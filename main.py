import os

import ffmpeg

def main():
    uncompressed_files = os.listdir("./uncompressed")
    video_bitrate = 5000
    audio_bitrate = 32000
    for filename in uncompressed_files:
        i = ffmpeg.input(f"./uncompressed/{filename}")

        ffmpeg.output(i, os.devnull,
                      **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                      ).overwrite_output().run()
        ffmpeg.output(i, f"./compressed/{filename}_compressed",
                    **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                    ).overwrite_output().run()

        # input_params = {'input_name': f"./uncompressed/{filename}"}
        # output_params = {
        #     f"./compressed/{filename}_compressed": '-vcodec libx264 -crf 20'
        # }
        # ff = ffmpy.FFmpeg(inputs=input_params, outputs=output_params)
        # print(ff.cmd)
        # ff.run()
    print("all done")


if __name__ == "__main__":
    main()