from fer import FER
from fer import Video
import pandas as pd

video_file: str = "./videos/momo.mp4"

face_detector: FER = FER(mtcnn=True)

processed_video = Video(video_file)

processing_data = processed_video.analyze(face_detector, display=True)

df = processed_video.to_pandas(processing_data)


